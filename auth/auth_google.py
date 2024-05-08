# auth_google.py
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Constants for Google API
SCOPES = ['https://www.googleapis.com/auth/tasks', 'https://www.googleapis.com/auth/tasks.readonly']

def get_google_credentials():
    """Get Google API credentials using OAuth2.
    
    This function handles the full OAuth2 flow. It checks for existing credentials in a
    token file. If none are found or they are invalid/expired, it initiates the flow to
    acquire new credentials from the authorization server.
    
    Returns:
        Credentials: The OAuth2 credentials for the Google API.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

if __name__ == '__main__':
    # Example usage
    credentials = get_google_credentials()
    print("Google OAuth2 authentication successful. Credentials are ready to use.")
