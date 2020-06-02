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
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)