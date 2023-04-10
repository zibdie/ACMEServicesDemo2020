#Used to generate functions for the MessageBox in messages.ejs
import pyperclip #Copies to clipboard

recpname = "Richard Marbury"
msgboxcontent = "Whats Up Dude! I heard you were on the Panasonic Avionics team for their new inflight theater system. I am also working on the same project so I thought you would be cool getting some coffee & brainstorming about it"
replydef = "Thank you & sure!"
actionallow = "Send"
actiondecline = ""
rowrem = "msg4"
action_msg_allow = "Your Message Has Been Sent"
statusDeclineButton = 0
statusReadExist = 1

output = "MessageBox('{}', '{}', '{}', '{}', '{}', '{}', '{}' ,{}, {})".format(recpname, msgboxcontent, replydef, actionallow, actiondecline, rowrem, action_msg_allow, statusDeclineButton, statusReadExist)
pyperclip.copy(output)

print(output)