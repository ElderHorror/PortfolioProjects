import smtplib  # Import the smtplib library

# Email credentials (replace with your own)
my_email = "1231234241@outlook.com"
password = "298348723681"

# Connect to the SMTP server for Office 365 using a secure connection (port 587)
with smtplib.SMTP("smtp.office365.com", 587) as connection:
    print("Connected to server.")  # Optional, Print confirmation message

    # Start TLS encryption for secure communication
    connection.starttls()
    print("Started TLS encryption.")  # Optional

    # Login with email address and password
    connection.login(user=my_email, password=password)
    print("Login successful.")  # Optional

    # Prepare the email content
    message = "Subject: Hello\n\n This is the body of the mail"

    # Send the email from the specified sender address to the recipient address
    connection.sendmail(
        from_addr=my_email,
        to_addrs="3718923791@gmail.com",
        msg=message,
    )
    print("Email sent!")  # Optional
