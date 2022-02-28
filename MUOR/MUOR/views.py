from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email',)

    def save(self, commit=True):
        return super().save(commit)


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

