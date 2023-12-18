from django.urls import URLPattern, path

from . import views

urlpatterns =[path('',views.index,name="index"),path('adlogin3.html',views.admin,name="admin"),
              path('adminfunctions.html',views.adfun,name="adfun"),
              path('add.html',views.ad,name="ad"),
              path('delete.html',views.de,name="de"),
              path('update.html',views.upd,name="upd"),path('user_login_new.html',views.login,name="login")]