from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.mixins import RulesMixin, DeleteProtectionMixin
from task_manager.users.forms import UserCreation, UserChange


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserCreation
    success_url = reverse_lazy("login")
    template_name = "users/create.html"
    success_message = _('User successfully created')


class ListUsers(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = 'users'


class UpdateUser(RulesMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserChange
    template_name = "users/update.html"
    success_url = reverse_lazy("users")
    success_message = _('User successfully changed')


class DeleteUser(
        RulesMixin,
        DeleteProtectionMixin,
        SuccessMessageMixin,
        DeleteView):
    model = User
    template_name = "users/delete.html"
    context_object_name = 'user'
    success_url = reverse_lazy("users")
    protected_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    protected_message = _("Cannot delete a user because it is in use")
