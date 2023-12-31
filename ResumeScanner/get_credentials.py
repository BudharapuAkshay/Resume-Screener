from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes required to send emails through the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Authenticate the user and obtain credentials
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

# Save the credentials for future use
with open('token.json', 'w') as token:
    token.write(creds.to_json())