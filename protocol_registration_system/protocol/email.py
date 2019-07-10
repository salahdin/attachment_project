from django.core.mail import send_mail

req_subject = "bhp protocol request "
req_body="your protocol request has been submited successfully"

res_subject_approved="approved"


def send_email(email):
    send_mail(
        req_subject,
        req_body,
        "postmaster@sandboxceec9532622a40f297ed91245b14cb8c.mailgun.org",
        [email,],
        fail_silently=False
    )