import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import PyPDF2
import re

# Define the email parameters
sender_email = 'agurlasujith2399@gmail.com'
sender_password = 'lalnpuikkfeqtsub'
subject = 'Your Resume has been shortlisted'
body = 'Congratulations! Your resume has been shortlisted for further consideration.'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Define the shortlisting criteria
keywords = ['python', 'data science', 'machine learning']
threshold = 2  # Minimum number of keywords to be shortlisted

# Open the PDF resume and extract the text
with open('resume.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in range(len(pdf_reader.pages)):
        pageObj = pdf_reader.pages[page]
        text += pageObj.extract_text()
        #text += pdf_reader.pages(page).extractText()

# Extract the email address from the resume
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = re.search(email_regex, text).group(0)

# Count the number of keywords in the resume
count = 0
for keyword in keywords:
    if keyword.lower() in text.lower():
        count += 1

# Shortlist the candidate if they meet the threshold
if count >= threshold:
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the resume to the email
    with open('resume.pdf', 'rb') as file:
        resume_attachment = MIMEApplication(file.read(), _subtype='pdf')
        resume_attachment.add_header('Content-Disposition', 'attachment', filename='resume.pdf')
        message.attach(resume_attachment)

    # Send the email using the Gmail SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        print(f'Sent email to {email}')
else:
    print('Resume does not meet the shortlisting criteria')