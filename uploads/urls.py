from django.conf.urls import url
from .views import AddImageView, ImageRetriveView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ImageRetriveView.as_view(), name='image-detail'),
    url(r'add/', AddImageView.as_view(), name='image-add')
]
