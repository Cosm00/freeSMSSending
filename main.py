import smtplib
#error "smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials w7-20020a05622a190700b002f9399ccefasm19808308qtc.34 - gsmtp')"
#to fix follow these directions and update the password on this script

#     Go to your Google Account.
#     Select Security.
#     Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because:
#     2-Step Verification is not set up for your account.
#     2-Step Verification is only set up for security keys.
#     Your account is through work, school, or other organization.
#     You turned on Advanced Protection.
#     At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
#     Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
#     Tap Done.

def sendText(text, phoneNumber):
    gmail_user = 'GMAIL ADDRESS HERE'
    gmail_password = 'GMAIL PASSWORD HERE'

    sent_from = gmail_user
    to = [
        "number@txt.att.net",
        "number@mms.att.net",
        "number@tmomail.net",
        "number@vtext.com",
        "number@vzwpix.com",
        "number@messaging.sprintpcs.com",
        "number@pm.sprint.com",
        "number@vtext.com",
        "number@mypixmessages.com",
        "number@vmobl.com",
        "number@vmpix.com",
        "number@mmst5.tracfone.com",
        "number@mymetropcs.com",
        "number@sms.myboostmobile.com ",
        "number@myboostmobile.com",
        "number@sms.cricketwireless.net",
        "number@mms.cricketwireless.net",
        "number@text.republicwireless.com",
        "number@msg.fi.google.com",
        "number@email.uscc.net",
        "number@mms.uscc.net",
        "number@message.ting.com",
        "number@mailmymobile.net",
        "number@cspire1.com",
        "number@vtext.com"
    ]

    rec = []
    for num in to:
        rec.append(num.replace('number', phoneNumber))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, rec, text)
        server.close()
        print('Email sent!')
    except Exception as e:
        print('Error sending email.\n{}'.format(str(e)))
