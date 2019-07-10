from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib import messages
import os
from .form import registerForm
from .form import SMSForm
from .form import EMAILForm
from .form import GMAILForm
from .form import WHATSAPPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from social_django.models import UserSocialAuth
from twilio.rest import Client
from .form import UserUpdateForm,ProfileUpdateForm
from django.core.mail import send_mail
from django.template.loader import get_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import sendgrid
# from django.core.mail import EmailMultiAlternatives


def index(request):
    my_dict = {'insert_me':"hello i am from views.py"}
    return render(request,'register/index.html',context=my_dict)

def login(request):
    login = {'login':"hello i am from views.py"}
    return render(request,'login.html',context=login)


@login_required
def sms(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            account_sid = 'AC6bbcf711c12791e6859dbb27103414d5'
            auth_token = 'd1ed9391046e2712c2e969ac552c4f48'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                                  # from_= form.cleaned_data['from_'],
                                  #  body = form.cleaned_data['message'],
                                  #  to =  form.cleaned_data['to'],

                              ),

            # print(message.sid[0])
            return redirect('profile')


    form = SMSForm()
    return render(request, 'register/sms.html',{'form':form})



@login_required
def mail(request):

    if request.method == 'POST':
        form = EMAILForm(request.POST)
        if form.is_valid():
            message = mail(
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SEND_GRID_API_KEY')),
            from_ = "dankit264@gmail.com",
            to = "dankit264@gmail.com",
            subject = u"Sending with SendGrid is Fun",
            content = ("text/plain", "and easy to do anywhere, even with Python"),
            mail = (from_email, subject, to_email, content),
            response = sg.client.mail.send.post(request_body=mail.get()),
            # print(response.status_code),
            # print(response.body),
            # print(response.headers)
            )
            # subject = 'contact form email'
            # from_email = 'dankit264@gmail.com'
            # to_email = ['dankit264@gmail.com']
            #
            # context = {
            # 'user':name,
            # 'email':email ,
            # 'message':message
            # }
            #
            #contact_message =get_template('contact_message.txt'.render(context))

            # message = Mail(

            # from_email='dankit264@gmail.com',
            # to_emails=['dankit264@gmail.com',],
            # subject='Sending with Twilio SendGrid is Fun',
            # html_content='<strong>and easy to do anywhere, even with Python mr karn</strong>')
            # try:

            # except Exception as e:
            #     print(str(e))




            # send_mail(subject,contact_message,from_email,to_email,fail_silently = True)

            return redirect('profile')
    form = EMAILForm()
    return render(request,'register/mail.html',{'form':form})





@login_required
def whatsapp(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            account_sid = 'AC6bbcf711c12791e6859dbb27103414d5'
            auth_token = 'd1ed9391046e2712c2e969ac552c4f48'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     from_=  form.cleaned_data ['from_'],
                     body= form.cleaned_data['message'],
                     to=  form.cleaned_data ['to'],
                 )

            print(message.sid)

            return redirect('index')
    form = WHATSAPPForm()
    return render(request,'register/whatsapp.html',{'form':form})













def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            #User = authenticate(email=email, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = registerForm()
    return render(request, 'register.html', {'form': form})



@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request, 'register/profile.html')

@login_required
def settings(request):
    user = request.user

    # try:
    #     github_login = user.social_auth.get(provider='github')
    # except UserSocialAuth.DoesNotExist:
    #     github_login = None

    # try:
    #     twitter_login = user.social_auth.get(provider='twitter')
    # except UserSocialAuth.DoesNotExist:
    #     twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        # 'github_login': github_login,
        # 'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})
