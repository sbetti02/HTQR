# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from PatientPortal.models import DocPat

from .forms import DoctorCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignUp(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return self.request.user.user_type == 'A' or self.request.user.is_superuser

    login_url = 'home'
    form_class = DoctorCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'