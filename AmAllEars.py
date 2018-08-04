from requests import get
from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# The website used to get IP address informaiton
# Currently it's returend as palin text.
website="https://api.ipify.org"
response=get(website)

# Email account used to send the informaiton
email="123@gmail.com"
pswd="123456"

# Recipient Email address
recipient="456@gmail.com"

if response.status_code!=200:
	print('Website Response Error..Exiting')
	exit()
	# Exit if response code wasn't success
else:
	# Prepare the message, login, and send it
	address=response.text
	fromaddr = email
	toaddr = recipient
	msg = MIMEMultipart()
	msg['From']= fromaddr
	msg['To']= toaddr
	msg['Subject'] = "Am All Ears"
	msg.attach(MIMEText(address, 'plain'))

	server = SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email,pswd)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit
	