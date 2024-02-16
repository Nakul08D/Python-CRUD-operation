from django.contrib import admin
from django.urls import path
from .import views

#To serve media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.log,name='login'),
    path('login_info',views.login_info,name='login_info'),
    path('logout_user/',views.logout_user,name='logout'),
    path('signin/',views.signin,name='signin'),
    path('signin_info/',views.signin_info,name='signin_info'),
    path('home/', views.home,name='home'),
    path('s_list/',views.s_list,name='list'),
    path('submit/',views.submit,name='submit'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)
