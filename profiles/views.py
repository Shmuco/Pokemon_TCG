from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,User
from .models import *
from django.views import generic



# Create your views here.
def signup(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'registration/signup.html', {'form':form})


def profile(request, user_id):

    profile = Profile.objects.get(user_id = user_id)
    print(profile.id)

    return render(request, 'registration/profile.html', {'user_id':profile})


# class UpdateProfile(generic.UpdateView):
#     template_name = 'registration/profile_update.html'
#     model = Profile
#     fields = '__all__'
#     success_url = 'homepage'