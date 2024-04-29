"""
URL configuration for hello_world project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hello_world.core import views as core_views

urlpatterns = [
    path("", core_views.start, name='start'),
    path("Dashboard/", core_views.Dashboard, name='Dashboard'),
    path("resume/", core_views.HomeView.as_view(), name='resume'),  # Moved before "Document/"
    path("upload_document/", core_views.upload_document, name='upload_document'),
    path("uploaded_documents/", core_views.uploaded_documents, name='uploaded_documents'),
    path("image_upload/",core_views.image_upload,name='image_upload'),
    path("admin/", admin.site.urls),
    path('<int:pk>', core_views.CandidateView.as_view(), name='candidate'),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
