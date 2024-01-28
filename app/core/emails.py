import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def trigger_email_send(
    recipient_email,
    sender_name,
    smtp_server,
    smtp_port,
    smtp_username,
    smtp_password,
    sender_email,
    subject,
    body_html,
):
    """Send the email."""

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS encryption
        server.login(smtp_username, smtp_password)
        print("Server logged in...")

        # Create the email message
        message = MIMEMultipart()
        message["From"] = f"{sender_name} <{sender_email}>"
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body_html, "html"))

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
        server.quit()  # Close the SMTP server connection
        print("Server quit...")
    except Exception as e:
        print(f"Error: {str(e)}")
