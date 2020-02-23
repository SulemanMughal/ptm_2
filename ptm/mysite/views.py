from django.shortcuts import render
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .tokens import account_activation_token


from .forms import *
from .models import *

def newfunc2(request,sel,val,usr):
    for i in profileModel.objects.all():
        if i.user.username == usr:
            obj = i
            break
    if (sel == 1):
        obj.minprice = int(val)
    elif (sel == 2):
        obj.maxprice = int(val)
    elif (sel == 3):
        obj.stories = int(val)
    elif (sel == 4):
        obj.minsqft = int(val)
    elif (sel == 5):
        obj.maxsqft = int(val)
    elif (sel == 6):
        obj.minlot = int(val)
    elif (sel == 7):
        obj.maxlot = int(val)
    elif (sel == 8):
        obj.property_type = val
    elif (sel == 9):
        obj.beds = int(val)
    elif (sel == 10):
        obj.bath = int(val)
    else:
        pass
    obj.save()
    return

def newfunc(request,sel,val):
    obj = profileModel.objects.get(user=request.user)
    if (sel == 1):
        obj.minprice = int(val)
    elif (sel == 2):
        obj.maxprice = int(val)
    elif (sel == 3):
        obj.stories = int(val)
    elif (sel == 4):
        obj.minsqft = int(val)
    elif (sel == 5):
        obj.maxsqft = int(val)
    elif (sel == 6):
        obj.minlot = int(val)
    elif (sel == 7):
        obj.maxlot = int(val)
    elif (sel == 8):
        obj.property_type = val
    elif (sel == 9):
        obj.beds = int(val)
    elif (sel == 10):
        obj.bath = int(val)
    else:
        pass
    obj.save()
    return

def home(request):
    # if request.user.is_authenticated and  not request.user.is_superuser:
    if request.method == 'POST':
        obj = User.objects.get(username=request.user.username)
        obj.first_name = request.POST['name']
        obj.email = request.POST['email']
        obj.save()
        obj = profileModel.objects.get(user=request.user)
        try:
            obj.contactNumber = request.POST['phone']
        except:
            pass
        obj.occupation = request.POST['occu']
        obj.any_other = request.POST['any_other']
        obj.save()
    if request.user.is_authenticated:
        try:
            profile = profileModel.objects.get(user=request.user)
        except:
            profile = profileModel.objects.create(user=request.user)
        if profile.approve == True:
            context = {
                'profile': profile,
                'section': 'dashboard'
            }
            if profile.Teacher_or_Parent == 'Buyer':
                context['agentcheck'] = False
                return render(request, 'page_47.html', context)
            if profile.Teacher_or_Parent == 'Agent':
                context['agentcheck'] = True
                return render(request, 'page_47.html', context)
        else:
            return render(request, 'mysite/Approve.html')
    return render(request, 'upclinch.html')


def contact(request):
    if request.method != 'POST':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            mail_subject = 'Contact -- By -- ' + \
                form.cleaned_data.get('userName')
            to_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data.get('body')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')

    context = {'form': form}
    return render(request, 'mysite/contact.html', context)


def login_user(request):
    if request.method != 'POST':
        form = loginForm()
    else:
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(
                    request, 'Usename or password may have been entered incorrectly.')
                return redirect('login')

    return render(request, 'mysite/login.html', {'form': form,'section': 'loginPage'})


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method != 'POST':
        form = registerForm()
        form_2 = profileInformFormRegister()
    else:
        # print(request.POST)
        form = registerForm(request.POST)
        form_2 = profileInformFormRegister(request.POST)
        # print(form.is_valid())
        # print(form_2.is_valid())
        if form.is_valid() and form_2.is_valid():
            # print(request.POST)
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data['password2'])
            user.email = form.cleaned_data['email']
            user.save()
            profile = profileModel.objects.create(user=user, phone=form_2.cleaned_data['phone'], occupation=form_2.cleaned_data['occupation'])
            profile.save()
            """         profile.Price_Range = form_2.cleaned_data['Price_Range']
            profile.occupation = form_2.cleaned_data['occupation']
            profile.has_pre_approval = form_2.cleaned_data['has_pre_approval']
            profile.property_type = form_2.cleaned_data['property_type']
            profile.beds = form_2.cleaned_data['beds']
            profile.bath = form_2.cleaned_data['bath']
            profile.lot_size = form_2.cleaned_data['lot_size']
            profile.stories = form_2.cleaned_data['stories']
            profile.location_preference = form_2.cleaned_data['location_preference']
            profile.looking_to_buy_in_how_many_months = form_2.cleaned_data['looking_to_buy_in_how_many_months']
            profile.How_long_have_you_been_house_hunting = form_2.cleaned_data['How_long_have_you_been_house_hunting']
            profile.Life_style = form_2.cleaned_data['Life_style']
            profile.any_other = form_2.cleaned_data['any_other']"""
            # current_site = get_current_site(request)
            # message = render_to_string('mysite/acc_active_email.html', {
            #     'user':user, 'domain':current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # mail_subject = 'Activate your account.'
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request,user)
            # print(request.user.is_authenticated)
            messages.success(request, 'Thank you for signup')
            return render(request, 'mysite/register.html', {'form': form, 'section' : 'register', 'form_2' : form_2, 'profile' : profile})
            # return redirect('home')
    return render(request, 'mysite/register.html', {'form': form, 'section' : 'register', 'form_2': form_2})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.warning(request, 'User has been activated')
        return redirect('login')
    else:
        messages.warning(request, 'Invalid Activation Link')
        return redirect('register')

# @login_required
# def edit_profile(request):
#     try:
#         profile = profileModel.objects.get(user=request.user)
#     except:
#         profile=None
#     context={
#         'profile' : profile,
#         'section' : "editProfile"
#     }
#     return render(request, 'mysite/editProfile.html', context)


@login_required()
def edit_profile(request):
    if request.method != 'POST':
        form = EditProfileForm(instance=request.user)
    else:
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile has been updated.')
            # return redirect('home')
    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = profileModel.objects.create(user=request.user)
    if request.method != 'POST':
        if profile:
            form_2 = profileInformForm(instance=profile)
        else:
            form_2 = profileInformForm()
    else:
        if profile:
            form_2 = profileInformForm(request.POST, instance=profile)
        else:
            form_2 = profileInformForm(request.POST,)
        if form_2.is_valid():
            form_2.save()
            messages.success(request, 'Profile has been updated.')
            return redirect('home')

    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = None
    context = {
        'profile': profile,
        'section': "editProfile",
        'form': form,
        'form_2':form_2
    }
    return render(request, 'mysite/editProfile.html', context)


@login_required()
def edit_profile_user(request):
    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = profileModel.objects.create(user=request.user)
    if request.method != 'POST':
        if profile:
            form = profileInformForm(instance=profile)
        else:
            form = profileInformForm()
    else:
        if profile:
            form = profileInformForm(request.POST, instance=profile)
        else:
            form = profileInformForm(request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated.')
            return redirect('home')
    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = None
    context = {
        'profile': profile,
        'section': "editProfile",
        'form': form
    }
    return render(request, 'mysite/editProfileUser.html', context)


@login_required()
def change_password(request):
    if request.method != 'POST':
        form = PasswordChangeForm(user=request.user)
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has been updated.')
            return redirect('home')
    return render(request, 'mysite/change_password.html', {'form': form, 'section': "editProfile"})
