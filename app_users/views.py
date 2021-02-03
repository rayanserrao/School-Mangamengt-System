from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_users.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'home.html')

def registeruser(request):
    registerd = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if UserForm.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registerd = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'register.html',{'registred':registerd,'user_form':user_form,'profile_form':profile_form})


def loginuser(request):
    if not request.user.is_authenticated:



   
        if request.method == 'POST':

                
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/index/')
                else:
                    return HttpResponse("Account deactivated")
            else:
                return HttpResponse("Please use valid id and password")
    else:
        return redirect("/index/")


@login_required
def user_logout(request):
    logout(request)
    return redirect('/index/')
