#!/usr/bin/python
#storing all the constants and configuration settings

#subject of email that will trigger event
subject_search = "this is a test" 			

#subject of the reply you will be getting back
reply_subject = "Your script has been launched!"			

#refresh rate of loop (in seconds)
refresh_rate = 5									

#imap server (for receiving)		
imap_host = 'imap.gmail.com'				

#smtp server (for sending)			
smtp_server = 'smtp.gmail.com'	

#smtp port number					
smtp_port = 587											

#email address (throw away email, make a new random one)
your_email = "<random email>"									

#email password (to your "throw away" account)
your_password = "<random email password>"						

#who to send email to (your mail email address)	
send_to = "<confirmation email>"	

#what the program should do upon discovering trigger subject!
def action():
	print "MUAHAHHAHAHAHA"			

#############################################
#####no need to touch this. Main loop.#######
#############################################
