#Used to generate functions for the MessageBox in messages.ejs
import pyperclip #Copies to clipboard

recpname = "<Leaders of Level Up! Erg>"
msgboxcontent = " "
replydef = "Hi, I would like to ask about your ERG!"
actionallow = "Send"
actiondecline = ""
rowrem = " "
action_msg_allow = "Your Message Has Been Sent!"
statusDeclineButton = 0
showmsgbox = 0

output = "MessageBox('{}', '{}', '{}', '{}', '{}', '{}', '{}' ,{}, {})".format(recpname, msgboxcontent, replydef, actionallow, actiondecline, rowrem, action_msg_allow, statusDeclineButton, showmsgbox)
pyperclip.copy(output)

print(output)