# auth_trello.py
import requests
from requests_oauthlib import OAuth1Session
import webbrowser

# Constants for Trello API
TRELLO_API_KEY = 'your_trello_api_key_here'
TRELLO_API_SECRET = 'your_trello_api_secret_here'
TRELLO_REQUEST_TOKEN_URL = 'https://trello.com/1/OAuthGetRequestToken'
TRELLO_AUTHORIZE_URL = 'https://trello.com/1/OAuthAuthorizeToken'
TRELLO_ACCESS_TOKEN_URL = 'https://trello.com/1/OAuthGetAccessToken'

def get_trello_oauth_session():
    """Create an OAuth session for Trello and authenticate the user.

    This function handles the OAuth1 authentication flow for Trello:
    - Fetching a request token
    - Redirecting the user to the authorization URL
    - Fetching an access token after user authorization

    Returns:
        OAuth1Session: An authenticated OAuth session that can be used to make requests to Trello API.
    """
    # Create an OAuth1Session object
    oauth = OAuth1Session(client_key=TRELLO_API_KEY, client_secret=TRELLO_API_SECRET)

    # Fetch the request token
    oauth.fetch_request_token(TRELLO_REQUEST_TOKEN_URL)

    # Get the authorization URL and direct the user there
    authorization_url = oauth.authorization_url(TRELLO_AUTHORIZE_URL)
    print('Please go to the following URL and authorize the application:', authorization_url)
    webbrowser.open(authorization_url)

    # Ask user to confirm authorization
    input('Press Enter after you have authorized the application.')

    # Fetch the access token
    oauth.fetch_access_token(TRELLO_ACCESS_TOKEN_URL)

    return oauth

if __name__ == '__main__':
    # Example usage
    session = get_trello_oauth_session()
    print("Trello OAuth1 authentication successful. Session is ready to use.")
