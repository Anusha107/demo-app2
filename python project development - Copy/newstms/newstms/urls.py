
"""newstms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.views.generic import TemplateView
from django.views.generic import ListView
from app.models import Add_company
from django.conf.urls.static import static
from newstms import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index.html')),
    path('home/',TemplateView.as_view(template_name='homepage.html')),
    path('aboutus/',TemplateView.as_view(template_name='aboutus.html')),
    path('contactus/',TemplateView.as_view(template_name='contactus.html')),
    path('carriers/',TemplateView.as_view(template_name='carriers.html')),
    path('company_login/',views.companylogin),
    path('add_company/',TemplateView.as_view(template_name='add_company.html')),
    path('addcomp/',views.add_company),
    path('view_allcompanies/',ListView.as_view(template_name='views_companies.html',model=Add_company))

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
