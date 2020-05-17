
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views #for register
from django.contrib.auth import views as auth_views #for login/logout

admin.site.site_header = 'tutorialApplication Admin'
admin.site.site_title = 'tutorialApplication Admin Panel'
admin.site.index_title = 'Welcome to tutorialApplication Admin Panel'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

