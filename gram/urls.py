from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.welcome,),
    path('accounts/',include('django_registration.backends.one_step.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('home/',views.home,),
    path('profile/',views.profile,),
    path('update_profile/',views.update_profile, name = "update_profile"),
    path('image_upload/',views.image_upload, name = "update_image"),
    path('single_image/<int:id>', views.get_images,name="get_images"),
    path('comment/<int:id>',views.comment,name='comment'),
    path('like/<int:id>', views.like_image, name ='like_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)