from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'register.html', context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def home(request):
    return render(request, 'index.html')


def roms(request):
    link = Rom.objects.all().values()
    context = {
        'link': link
    }

    return render(request, 'roms.html', context)


def mods(request):
    link = Mod.objects.all().values()
    context = {
        'link': link
    }
    return render(request, 'mods.html', context)


def upload(request):
    form = Upload()
    if request.method == "POST":
        form = Upload(request.POST)
        uploads = request.POST.get('upload')
        print(uploads)
        if uploads == 'rom':
            return redirect('upload_roms')
        elif uploads == 'mod':
            return redirect('upload_mods')
        elif uploads == 'none':
            messages.error(request, 'Choose a Correct  Option !!')
    return render(request, 'upload.html', {'upload_form': form})


def upload_mods(request):
    if request.method == 'POST':
        name = request.POST.get('mod_name')
        link = request.POST.get('mod_link')
        android = request.POST.get('mod_android')
        mod_credit = request.POST.get('mod_credit')
        purpose = request.POST.get('purpose')
        r = Mod.objects.create(mod_name=name, mod_link=link,
                               mod_credits=mod_credit, mod_android=android, purpose=purpose)
        r.save()
        return redirect("/mods/")

    return render(request, 'upload_mods.html')


def upload_roms(request):
    if request.method == "POST":
        name = request.POST.get('rom_name')
        android = request.POST.get('android')
        link = request.POST.get('rom_link')
        version = request.POST.get('version')
        bugs = request.POST.get('bugs')
        credit = request.POST.get('credit')
        fw = request.POST.get('fw_cat')
        boot = request.POST.get('boot_cat')
        e = Rom.objects.create(rom_name=name, rom_link=link, android=android,
                               version=version, bugs=bugs, credit=credit, fw=fw, boot=boot)
        e.save()
        return redirect("/roms/")
    return render(request, 'upload_roms.html')


def rom_details(request, id):
    data = Rom.objects.filter(id=id)
    return render(request, 'rom_details.html', {'data': data})


def mod_details(request, id):
    data = Rom.objects.filter(id=id)
    return render(request, 'mod_details.html', {'data': data})


def twrp(request):
    return render(request, 'twrp.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.FILES.get('subject')
        message = request.POST.get('message')
        r = Contact.objects.create(name=name, email=email,
                                   subject=subject, message=message)
        r.save()
        return redirect("/mods/")
    return render(request, 'contact.html')


def comment(request):

    if request.method == "POST":
        n = request.POST.get('Name')
        mess = request.POST.get('Message')
        e = Comment.objects.create(name=n, message=mess)
        e.save()
        return redirect('/comment/')

    data = Comment.objects.all().values()
    return render(request, 'comment.html', {'data': data})


def error_500(request):
    return render(request, '500.html', status=500)
