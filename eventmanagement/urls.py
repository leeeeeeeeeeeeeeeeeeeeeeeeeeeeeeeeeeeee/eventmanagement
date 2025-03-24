
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from event import views

from eventmanagement import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/',include('event.urls')),
    # path('404/', TemplateView.as_view(template_name='404.html')),
    path("register/",views.SignupView.as_view(),name="register"),
    path("signin/",views.SigninView,name="signin"),
    path("signup_manager/",views.signup_manager,name="signup_manager"),
    path("logoutview/",views.logoutview,name="logoutview"),
    path("signin_manager/",views.signin_manager,name="signin_manager"),
    # path("accounts/",include("allauth.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
