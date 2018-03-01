# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignUp(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return self.request.user.user_type == 'A'
    login_url = 'home'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'