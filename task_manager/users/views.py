from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.models import User
from task_manager.users.forms import UserRegistrationForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            msg_text = _('User is successfully created')
            messages.success(request, msg_text) 
            return redirect('users_index')
        return render(request, 'users/create.html', {'form': user_form})


class EditUserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserRegistrationForm(instance=user)
        return render(request,
                      'users/update.html',
                      {'form': form,
                       'user_id': user_id})

class UserFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        full_username = f'{user.first_name} {user.last_name}'
        return render(request,
                      'users/delete.html',
                      context={'user_id': user_id,
                          'full_username': full_username})


        '''def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Article.objects.get(id=article_id)
        if user:
            user.delete()
        return redirect('users_index')'''
