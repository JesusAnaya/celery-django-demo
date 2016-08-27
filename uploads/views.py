from django.views.generic import CreateView, DetailView
from .models import UploadImage
from .forms import UploadImageForm


class AddImageView(CreateView):
    template_name = 'uploads/add.html'
    model = UploadImage
    form_class = UploadImageForm


class ImageRetriveView(DetailView):
    template_name = 'uploads/retrive.html'
    model = UploadImage
    context_object_name = 'upload'
