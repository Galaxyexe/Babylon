from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserRegisterForm


def register(request):
    print(request)
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


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
