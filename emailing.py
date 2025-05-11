import mimetypes
import smtplib
from email.message import EmailMessage

password = "bjfn pshp choo bbcp"
sender = "teertha.sarker.4@gmail.com"
receiver = "teertha.sarker.3@gmail.com"


def send_mail(image_path):
    print("Sending email...")
    email_message = EmailMessage()
    email_message['Subject'] = "Intruder Alert"
    email_message['From'] = sender
    email_message['To'] = receiver
    email_message.set_content("Intruder detected! Check the attached image.")

    # Guess MIME type
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'
    maintype, subtype = mime_type.split('/')

    # Attach the image
    with open(image_path, 'rb') as f:
        content = f.read()
        email_message.add_attachment(content, maintype=maintype, subtype=subtype, filename=image_path)

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
            gmail.ehlo()
            gmail.starttls()
            gmail.login(sender, password)
            gmail.send_message(email_message)
            print("Email sent successfully.")
    except smtplib.SMTPRecipientsRefused as e:
        print("Recipient address was refused:", e)
    except Exception as e:
        print("An error occurred:", e)



if __name__ == "__main__":
    send_mail("images/20.jpg")
