from django.core.mail import EmailMultiAlternatives

def send_email(username, to_email, template, text):
    subject, from_email, to = username, 'from@example.com', to_email
    text_content = text
    html = template
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html , "text/html")
    msg.send()