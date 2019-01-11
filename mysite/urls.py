from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
