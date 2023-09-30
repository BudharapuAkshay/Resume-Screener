# Resume Screener App

The Resume Screener App is a tool designed to streamline the resume screening process during recruitment. It leverages keyword matching and machine learning techniques to identify suitable candidates based on specific criteria.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Keyword-based Resume Screening:** Automatically identifies resumes that match predefined keywords or criteria.
- **Customizable Shortlisting:** Allows recruiters to set their own shortlisting criteria, including the number of keywords required for consideration.
- **PDF Resume Parsing:** Extracts text from PDF resumes for analysis.
- **Email Notifications:** Notifies candidates about their application status via email.
- **Data Privacy:** Implements security measures to protect candidate data and ensure compliance with data privacy regulations.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Required Python libraries (e.g., `smtplib`, `PyPDF2`, `re`, etc.)
- Gmail account (for sending email notifications)

You can install the necessary libraries using pip:


pip install smtplib PyPDF2


#Installation
Clone the repository:

git clone https://github.com/BudharapuAkshay/resume-screener-app.git 
cd resume-screener-app
Configure the application by updating the following variables in the code:

sender_email: Your Gmail email address for sending notifications.
sender_password: Your Gmail password or an app-specific password.
smtp_server: SMTP server details (e.g., 'smtp.gmail.com').
smtp_port: SMTP server port (e.g., 587).
#Usage
Place the PDF resumes you want to screen in the project directory.

Run the application:

python resume_screener.py
Follow the on-screen instructions to set shortlisting criteria, keyword matching, and email notifications.

The application will process the resumes and send email notifications to shortlisted candidates.

#Project Structure
resume_screener.py: The main application script.
sample_resumes/: Directory for storing sample PDF resumes for testing.
requirements.txt: List of Python dependencies.
README.md: This README file.
Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Create a pull request to the main repository.
#License
This project is licensed under the MIT License. See the LICENSE file for details.
