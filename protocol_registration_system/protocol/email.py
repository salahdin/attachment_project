from django.core.mail import send_mail

req_subject = "bhp protocol request "
req_body="your protocol request has been submited successfully"

res_subject_approved="request approved"
res_subject_rejected="request rejected"
res_body_approved="your request has been approved"
res_body_rejected="your request has been rejected"


def send_email(email,response=False,approved=False):
    if approved==True and response==True:
        send_mail(
            res_subject_approved,
            res_body_approved,
            "postmaster@sandboxceec9532622a40f297ed91245b14cb8c.mailgun.org",
            [email,],
            fail_silently=False
        )
    elif approved==False and response==True:
        send_mail(
            res_subject_rejected,
            res_body_rejected,
            "postmaster@sandboxceec9532622a40f297ed91245b14cb8c.mailgun.org",
            [email,],
            fail_silently=False
            )
    elif approved==True and response==False:
        send_mail(
            req_subject,
            req_body,
            "postmaster@sandboxceec9532622a40f297ed91245b14cb8c.mailgun.org",
            [email,],
            fail_silently=False
        )
        

        

            