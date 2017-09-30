from django.shortcuts import render_to_response

from django.shortcuts import render
from django.http import HttpResponse
# This view method handles the request for the root URL /
# See urls.py for the mapping.
def home(request):
    # Render the index.html template with a context dictionary
    # that has a key called 'time' with current time obtained from
    # the datetime module as the value.
    return render(request, "home/index.html")

def quantcast(request):
    # Render the index.html template with a context dictionary
    # that has a key called 'time' with current time obtained from
    # the datetime module as the value.
    return render(request, "home/quantcast.html")

def zynga(request):
    # Render the index.html template with a context dictionary
    # that has a key called 'time' with current time obtained from
    # the datetime module as the value.
    return render(request, "home/zynga.html")


def choice(request):
    # Render the index.html template with a context dictionary
    # that has a key called 'time' with current time obtained from
    # the datetime module as the value.
    return render(request, "home/choice.html")

from django.template import loader
from django.core.mail import send_mail


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def sendemail(request):
    from_email = request.POST['email']
    from_name = request.POST['name']
    FROM = from_email
    subject = request.POST['subject']
    TO = "allu.vivek7@gmail.com"
    SUBJECT = subject
    message = request.POST['message']
    BODY = message

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY, 'text')
    #server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    #server.login(gmail_user, password)
    #server.sendmail(gmail_user, TO, BODY)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login('allu.vivek7@gmail.com','ldpku!23')
    message = """\
    Name: %s
    From: %s
    To: %s
    Subject: %s

        %s
     """ % (from_name, FROM, TO, SUBJECT, BODY)
    #msg.attach(part1)
    msg.attach(MIMEText(message,'plain'))
    '''
    html_message = loader.render_to_string(
            'email-templates/simple.html',
            {
                'name': user,
                'email':  from_email,
                'subject':  'Thank you from' + subject,
                'message' : message

            }
        )
    '''
    print("testing 123 **************8")
    server.sendmail(from_email, 'allu.vivek7@gmail.com', msg.as_string())
    server.quit()
    #to_list = ['allu.vivek7@gmail.com']
    #send_mail(subject,message,from_email,to_list,fail_silently=True,html_message=html_message)
    return HttpResponse('Sent')
