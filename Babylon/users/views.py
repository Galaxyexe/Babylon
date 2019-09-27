from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

@csrf_exempt
def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Accunt created for {username}! Login!')
            return HttpResponse("home")
    else:
        form=UserRegisterForm();
    template = loader.get_template("users/register.html")
    return HttpResponse(template.render({'form': form}, request))
    #return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if (request.method=="POST"):
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Accunt has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    profile=request.user.profile._meta.get_fields()
    templist=[]
    for i in range(len(profile)):
        templist.append(profile[i].value_from_object(request.user.profile))
    profile=templist
    context={
    'profile':profile,
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request, 'users/profile.html', context)

def popup(request):
    return render(request, 'users/login.html')
