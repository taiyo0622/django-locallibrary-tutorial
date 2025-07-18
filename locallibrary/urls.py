"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from catalog.views import oidc_callback, post_login_redirect

urlpatterns = [
    path("admin/", admin.site.urls),
]


urlpatterns += [
    path("catalog/", include("catalog.urls")),
]


# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path("", RedirectView.as_view(url="/catalog/", permanent=True)),
]


# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("post-login-redirect/", post_login_redirect, name="post_login_redirect"),
    path("oidc/callback", oidc_callback, name="oidc-callback-root"),
]
