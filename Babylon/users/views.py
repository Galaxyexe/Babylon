from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from .forms import UserRegisterForm


def register(request):
    print(request.path)
    print("AAHAHAa")
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        #print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect(request.path)
    else:
        context={
        'form':UserRegisterForm(),
        'page':"general/realnavbar.html"
        }
    template = loader.get_template("users/register.html")
    return HttpResponse(template.render(context, request))
    #return render(request, 'users/register.html', context)


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
    context={
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request, 'users/profile.html', context)
