from django.contrib.auth.models import User  # Use Django's built-in User model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountCreateView(CreateView):
    model = User
    template_name = 'accounts/new.html'
    fields = ['username', 'last_name', 'email', 'password']
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Hash the password
        user.save()
        return super().form_valid(form)

class AccountDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/detail.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return self.request.user