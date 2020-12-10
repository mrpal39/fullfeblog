from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm,UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile

# User registration and user profiles


def register(request):
    if request.method == 'POST':

        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():            
    # create new user form request
            new_user = user_form.save(commit=False)
            # set the choose pasword
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # Profile.objects.create(user=new_user)
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})



    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method =='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES    )


        if user_form.is_valid()and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)


    return render(request,'registration/edit.html',{'user_form':user_form,
    'profile_form':profile_form})             



def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'}
                  )


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:

                    login(request, user)
                    return HttpResponse('Authenticated '
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
