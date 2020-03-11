import smtplib

host="smtp.gmail.com"
port=587
username="hazelblake.98@gmail.com"
password="hazel.blake98"
from_email=username
to_list=["hazelblake.98@gmail.com"]

email_conn=smtplib.SMTP(host,port)

email_conn.ehlo()
email_conn.starttls()

email_conn.login(username,password)

email_conn.sendmail(from_email,to_list,
	"Hi there is an email message")

email_conn.quit()



from smtplib import SMTP 

ABC=SMTP(host,port)

ABC.ehlo()
ABC.starttls()

ABC.login(username,password)

ABC.sendmail(from_email,to_list,"Hi there is an email message")

ABC.quit()



from smtplib import SMTP,SMTPAuthenticationError,SMTPException

pass_wrong=SMTP(host,port)

pass_wrong.ehlo()
pass_wrong.starttls()

try:
	pass_wrong.login(username,"wrong password")
	pass_wrong.sendmail(from_email,to_list,"Hi there is an email message")
except SMTPAuthenticationError:
	print("Could not login")
except:
	print("there's an error")

pass_wrong.quit()




