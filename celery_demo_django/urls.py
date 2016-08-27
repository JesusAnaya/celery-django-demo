from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url("^$", TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^uploads/', include('uploads.urls')),
    url(r'^admin/', admin.site.urls),
]
