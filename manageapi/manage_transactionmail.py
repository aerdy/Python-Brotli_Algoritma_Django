import mandrill
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import smtplib
import manage_xXMdi

def send_mail(user, id_user):
	newdata = manage_xXMdi.encrypt_val(id_user)
	msg = EmailMultiAlternatives(subject="Confirm registration kabisat.com", from_email="arthdi@necistudio.com",
	                   to=["aerdy4@gmail.com"], headers={'Reply-To': "arthdi@necistudio.com"})
	#msg.template_name = "kabisat"           # A Mandrill template name
	msg.attach_alternative("<a href=http://127.0.0.1:8080/confirmmail/"+user+"/"+newdata+">Confirm your account kabisat.com</a>"+
		"<img src='http://1.bp.blogspot.com/-yb-o3AwiNXk/T1CfRHAQ_gI/AAAAAAAADLI/JoqANZgbbkE/s1600/29Feb.jpg' alt='Mountain View' style='width:304px;height:228px;'>", "text/html")
	msg.send()
# 	msg.mandrill_response = [
#     {
#         "email": "someone@example.com",
#         "status": "sent",
#         "_id": "abc123abc123abc123abc123abc123"
#     }
# 	]
	return 'Success send mail'

# API_KEY = 'yyC9Ui6hFNPr_xA_qe7R4Q'

# def send_mail():
# 	mandrill_client = mandrill.Mandrill(API_KEY)
#    	template_content = [{'content': 'example content', 'name': 'kabisat'}]
#    	message = {
#      'from_email': 'arthdi@necistudio.com',
#      'from_name': 'Verification Kabisat.com',
#      'important': False,
#      'subject': 'Verification Kabisat.com',
#      'text': 'Verification Kabisat.com',
#      'to': [{'email': 'aerdy4@gmail.com',
#              'name': 'Anna arthdi',
#              'type': 'to'}],}
#    	result = mandrill_client.messages.send_template(template_name='kabisat', template_content=template_content, message=message, async=False)
# 	return result