from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url("^$", TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^uploads/', include('uploads.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
