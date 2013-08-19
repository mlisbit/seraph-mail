#!/usr/bin/python

from seraph_config import *
from engine import *

#you dont have to touch this.
while True:
	print 'Connecting to Inbox..'
	trigger_message = check_subjects()
	if trigger_message is not None: 					#if the "trigger subject" is found do this
		action()
		#comment this out if you dont want a confirmation email.
		send_mail(get_sender(trigger_message))
	time.sleep(refresh_rate)							#delay before checking email again