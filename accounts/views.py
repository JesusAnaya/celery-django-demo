from django.views.generic import CreateView, DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.pk})


class UserDetailView(DetailView):
    template_name = 'accounts/retrive.html'
    model = User
    context_object_name = 'user'
