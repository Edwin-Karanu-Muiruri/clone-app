from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.welcome,),
    path('accounts/',include('django_registration.backends.one_step.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/'),
        name='django_registration_register'),
    path('accounts/login', LoginView.as_view(redirect_field_name ='/',success_url = '/'), name = 'login'),
    path('accounts/logout',LogoutView.as_view(redirect_field_name ='/accounts/login')),
    path('home/',views.home,),
    path('profile/',views.profile,),
    path('update_profile/',views.update_profile, name = "update_profile"),
    path('post/',views.image_upload, name = "update_image"),
    path('single_image/<int:id>', views.get_images,name="get_images"),
    path('comment/<int:id>',views.comment,name='comment'),
    path('like/<int:id>', views.like_image, name ='like_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)