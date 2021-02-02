from django.shortcuts import render
from django.http import HttpResponse
from app_users.forms import UserForm,UserProfileForm

# Create your views here.
def index(request):
    return HttpResponse("hello word")

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


# def loginuser(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = UserForm(request=request,data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
