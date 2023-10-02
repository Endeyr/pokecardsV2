import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.http import HttpResponse


def send_mail(request):
    if request.method == "GET":
        message = Mail(
            from_email="aaron.thompson42594@gmail.com",
            to_emails=("t.aaron263@gmail.com"),
            subject="Sending with Twilio SendGrid is Fun",
            html_content="<strong>and easy to do anywhere, even with Python</strong>",
        )
        try:
            sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
            response = sg.send(message)
            print(response.headers)
            print(response.body)
            return HttpResponse(response.status_code)
        except Exception as e:
            return HttpResponse(e.message)
