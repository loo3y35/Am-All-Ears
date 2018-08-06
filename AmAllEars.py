from requests import get
from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from cryptography.fernet import Fernet
from os import walk,getcwd

def check_config():
	# Check if email configrations are present
	flag_key=False
	flag_sender=False
	flag_passwd=False
	flag_recep=False
	for root, dirs, files in walk(getcwd()):
		for name in files:
			if root==getcwd():
				if name=='aae_data_key':
					flag_key=True
				elif name=='aae_data_sender':
					flag_sender=True
				elif name=='aae_data_passwd':
					flag_passwd=True
				elif name=='aae_data_recep':
					flag_recep=True

	if flag_key==False or flag_sender==False or flag_passwd==False or flag_recep==False:
		answer=raw_input("Data files are incomplete..\nDo you want to generate new ones? Yes/No\n")
		# answer='yes'
		if answer.upper()=='YES':
			print('Generating...')
			gen_config()
		else:
			print('Exiting...')
			exit()


def gen_config():
	# Generate configuraiton files and ecnrypt them
	FID_Key=open('aae_data_key','w')
	FID_Sender=open('aae_data_sender','w')
	FID_Passwd=open('aae_data_passwd','w')
	FID_Recep=open('aae_data_recep','w')

	clear_sender=raw_input('Enter the sender email: ')
	clear_passwd=raw_input('Enter the sender password: ')
	clear_recept=raw_input('Enter the recipient email: ')

	key = Fernet.generate_key()
	cipher_suite = Fernet(key)

	cipher_sender=cipher_suite.encrypt(clear_sender)
	cipher_passwd=cipher_suite.encrypt(clear_passwd)
	cipher_recep=cipher_suite.encrypt(clear_recept)

	FID_Key.write(key)
	FID_Sender.write(cipher_sender)
	FID_Passwd.write(cipher_passwd)
	FID_Recep.write(cipher_recep)

def read_config():
	# Read and decrypt configuraiton files
	FID_Key=open('aae_data_key','r')
	FID_Sender=open('aae_data_sender','r')
	FID_Passwd=open('aae_data_passwd','r')
	FID_Recep=open('aae_data_recep','r')

	key = FID_Key.read()
	cipher_suite = Fernet(key)
	
	email=cipher_suite.decrypt(FID_Sender.read())
	pswd=cipher_suite.decrypt(FID_Passwd.read())
	recipient=cipher_suite.decrypt(FID_Recep.read())

	return email, pswd, recipient


def main():
	# Before attempting to send the emial, check and generate required encrypted configuraiton
	check_config()
	email, pswd, recipient = read_config()
	
	# The website used to get IP address informaiton
	# Currently it's returend as palin text.
	website="https://api.ipify.org"
	response=get(website)

	# I've used Gmail here
	mail_domain='smtp.gmail.com'
	mail_port=587

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

		server = SMTP(mail_domain, mail_port)
		server.starttls()
		server.login(email,pswd)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit
main()