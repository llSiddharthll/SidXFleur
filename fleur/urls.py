from fleur import views
from django.urls import path

urlpatterns = [
     path('',views.home,name='home'),
     path('roms/', views.roms, name='roms'),
     path('mods/', views.mods, name='mods'),
     path('upload',views.upload,name='upload'),
     path('upload_roms',views.upload_roms,name='upload_roms'),
     path('upload_mods',views.upload_mods,name='upload_mods'),
     path('roms/twrp', views.twrp, name="twrp"),
     path('roms/rom_details/<int:id>', views.rom_details, name='rom_details'),
     path('mods/mod_details/<int:id>', views.mod_details, name='mod_details'),
     path("register", views.register_request, name="register"),
     path("login", views.login_request, name="login"),
     path("logout", views.logout_request, name= "logout"),
     path('contact',views.contact,name='contact'),
     path('comment/',views.comment,name='comment'),
]
handler500 = 'fleur.views.error_500'
