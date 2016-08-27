from django.conf.urls import url
from .views import RegisterUserView, UserDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^create/$', RegisterUserView.as_view(), name='user-create')
]
