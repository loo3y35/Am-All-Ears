# Introduction
Am-All-Ears script is designed to share the public IP for the machine it is running on. Then, send this public IP over email. Currently, it acquires the public IP from https://api.ipify.org and it uses GMail. The main goal was to not rely on DNS based services (e.g. DynDNS) to maintain reachability to your devices.

# Description
To be able to use it, you will need to login with en email account you own. The script will generate three four encrypted files the first time you use it to store:
* Encryption and decryption password (i.e. aae_data_key).
* Sender email address (i.e. aae_data_sender).
* Sender password (i.e. aae_data_passwd).	
* Recipient email address (i.e. aae_data_recep).

If any of these files are missing, all files are regenerated (and well, overwritten).
The firs time you run it you will be promoted to enter information mentioned beforehand.
Currently, its’s using Gmail SMTP server. But of course you can change the server domain name and port number.

# How to Keep Yourself Updated
I’ve used two configurations in crontab and rc.local
## Crontab
With he following entry, the email is sent every four hours.
`0 0,4,8,12,16,20 * * *	python /home/user/.custom/AmAllEars.py`
## rc.local
I’ve added the following entry
`python /home/user/.custom/AmAllEars.py`