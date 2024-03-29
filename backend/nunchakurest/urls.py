"""
URL configuration for nunchakurest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

# urls.py in your Django app

# from django.views.generic import TemplateView

# urlpatterns = [
#     # ... other urlpatterns
#     path(
#         "frontend/",
#         TemplateView.as_view(template_name="frontend_template.html"),
#         name="frontend",
#     ),
# ]


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("", include("api.urls", "api")),
                path("", include("menu.urls", "menu")),
            ]
        ),
    ),
    # path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(
        "favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))
    ),
]
