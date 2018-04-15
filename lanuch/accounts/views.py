from django.shortcuts import render, redirect
from .forms import RegistrationForm, EditProfileForm, AddInfo
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Author
from blog.models import waste
from django.contrib.auth.models import User

def ViewProfile(request, author_pk):
    if author_pk == request.user.id:
        if request.user.is_authenicated():
            user = User.objects.get(user=request.user)
            #print('suceess')
            return render(request, 'accounts/profile.html', {'user':user})
    else:
        user = User.objects.get(pk=author_pk)
        #user.author_set.views += 1
        #user.views += 1
        #user.save()
        return render(request, 'accounts/profile.html', {'user':user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
            #return render(request, 'blog/home.html', context)
        else: return redirect('/accounts/register')

    else:
        form = RegistrationForm()
        title = 'Change Your Password'
        btnName = 'Register'
        context = {'form':form, 'title':title, 'btnName':btnName}
        return render(request, 'accounts/edit.html', context)

'''
def jregister(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
'''
def EditProfile(request):
    if request.Method == 'POST':
        form = EditProfileForm(request.Post, instance=request.User)

        if form.is_valid():
            form.save()
            return re
    else:
        form = EditProfileForm(instance=request.user)
        title = 'Edit Your Profile'
        btnName = 'Done editing'
        context = {'form':form, 'title':title, 'btnName':btnName}
        return render(request, 'accounts/edit.html', context)


def AddInfo(request):

    if request.Method == 'POST' and request.user.is_authenicated():
        form = AddInfo(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance = form.cleaned_data['description']
            instance = form.cleaned_data['link']
            form.save()
            return redirect('/home/')
        else:
            return redirect('/accounts/add')
    else:
        form = RegistrationForm
        title = 'Tell Us More'
        btnName = 'Finish'
        context = {'form':form, 'title':title, 'btnName':btnName}
        return render(request, 'accounts/edit.html', context)


def Changepassword(request):
    if request.Method == 'POST':
        form = PasswordChangeForm(data=request.Post, user=request.User)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/Changepassword')
    else:
        form = PasswordChangeForm(instance=request.user)
        title = 'Change Your Password'
        btnName = 'Change Password'
        context = {'form':form, 'title':title, 'btnName':btnName}
        return render(request, 'accounts/edit.html', context)
