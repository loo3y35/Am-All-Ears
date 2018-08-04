# Am-All-Ears
This python scripts acquires the public IP from https://api.ipify.org and sends it over email.

It's intended to reomve the requireiment of using services such as DynDNS.

You will only need to register an email address to login and send it.

I've used it with GMail but I needed to Enable Access for Less Secure Apps.

To keep myself updated, I schedueled sending running the script every 4 hours and whenever my homeserver boots.

user@vm:~$ cat /etc/rc.local | grep AmAllEars

python /home/user/.custom/AmAllEars.py

user@vm:~$ crontab -l | grep AmAllEars

0 0,4,8,12,16,20 * * *	python /home/user/.custom/AmAllEars.py