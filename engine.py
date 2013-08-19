#!/usr/bin/python
import os
import imaplib
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from seraph_config import *
#initialization									
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(your_email, your_password)

#Parses the email message to get an email sender 
def get_sender(message):
	#print message 	
	email_check = ""
	from_finder = message.index('From: "') + 7

	while True:
		from_finder += 1
		if message[from_finder] is chr(ord('<')):
			break
			
	while True:
		from_finder += 1
		email_check += str(message[from_finder])
		if message[from_finder + 1] is chr(ord('>')):
			break
	
	return email_check

#checks if trigger subject is found. 
def check_subjects():
	mail.select()
	typ, data = mail.search(None, 'UNSEEN')
	print len(data[0].split()), "unread messages"
	
	#for all the new emails, check for the "trigger subject" 
	for num in data[0].split():
		typ,data = mail.fetch(num, '(RFC822)')
		unseen_message = ''.join(data[0])

		#finds the index of the keyword subject in the message 
		start = unseen_message.index('Subject:') + 9	
		subject_check = ""
		
		#gets the subject
		for i in range(0,len(subject_search)):
			subject_check += str(unseen_message[start + i])
		
		print subject_check
		if subject_check == subject_search:
			print ("SENDER: " + get_sender(unseen_message))
			return unseen_message
		else:
			print "email received, but did not match trigger subject"
	mail.close()

def send_mail(email_to):
	msg = MIMEMultipart()
	msg['Subject'] = reply_subject
	msg['From'] = your_email
	msg['To'] = email_to
	msg.preamble = 'information!'

	s = smtplib.SMTP(smtp_server, smtp_port)	#smtp server
	s.starttls()										#start secure connection
	s.login(your_email, your_password)			#login in to sender 

	s.sendmail(your_email, send_to, msg.as_string()) 	#sends the mail once logged in
	s.quit()				

