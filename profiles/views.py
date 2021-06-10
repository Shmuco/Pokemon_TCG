from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,User
from .models import *
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy




# Create your views here.
def signup(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('login')
    return render(request, 'registration/signup.html', {'form':form})


def profile(request, user_id):

    profile = Profile.objects.get(user_id = user_id)
    print(profile.id)

    return render(request, 'registration/profile.html', {'user_id':profile})


class UpdateProfile(generic.UpdateView):
    template_name = 'registration/profile_update.html'
    model = Profile
    fields = ('username','team', 'image')
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)