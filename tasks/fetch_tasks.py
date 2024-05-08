# tasks/fetch_tasks.py
import requests
from config import TRELLO_API_KEY, TRELLO_API_SECRET
from auth import get_trello_oauth_session
from googleapiclient.discovery import build
from auth import get_google_credentials

def fetch_trello_tasks(board_id):
    """
    Fetches tasks from a specified Trello board.

    Args:
    board_id (str): The ID of the Trello board from which to fetch tasks.

    Returns:
    list: A list of tasks from the specified Trello board.
    """
    oauth = get_trello_oauth_session()
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    response = oauth.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch Trello tasks: " + response.text)

def fetch_google_tasks(tasklist_id):
    """
    Fetches tasks from a specified Google Tasks list.

    Args:
    tasklist_id (str): The ID of the Google Tasks list from which to fetch tasks.

    Returns:
    list: A list of tasks from the specified Google Tasks list.
    """
    credentials = get_google_credentials()
    service = build('tasks', 'v1', credentials=credentials)
    results = service.tasks().list(tasklistId=tasklist_id).execute()
    items = results.get('items', [])
    return items

if __name__ == '__main__':
    # Example usage:
    # Replace 'your_trello_board_id' and 'your_google_tasklist_id' with actual IDs.
    trello_tasks = fetch_trello_tasks('your_trello_board_id')
    google_tasks = fetch_google_tasks('your_google_tasklist_id')
    print("Fetched Trello Tasks:", trello_tasks)
    print("Fetched Google Tasks:", google_tasks)
