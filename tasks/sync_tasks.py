# tasks/sync_tasks.py
from .fetch_tasks import fetch_trello_tasks, fetch_google_tasks
from googleapiclient.discovery import build
from auth import get_google_credentials
from config import TRELLO_API_KEY
from auth import get_trello_oauth_session

def synchronize_tasks(trello_board_id, google_tasklist_id):
    """
    Synchronizes tasks between a Trello board and a Google Task list.

    Args:
    trello_board_id (str): The ID of the Trello board.
    google_tasklist_id (str): The ID of the Google Tasks list.

    This function fetches tasks from both platforms, compares them, and updates
    each platform to reflect changes made in the other. This is a basic implementation
    and might require more complex conflict resolution strategies depending on requirements.
    """
    # Fetch tasks from both platforms
    trello_tasks = fetch_trello_tasks(trello_board_id)
    google_tasks = fetch_google_tasks(google_tasklist_id)

    # Create Google Tasks service
    credentials = get_google_credentials()
    google_service = build('tasks', 'v1', credentials=credentials)

    # Create Trello session
    trello_session = get_trello_oauth_session()

    # Example sync logic: Add missing Trello tasks to Google Tasks
    google_task_titles = [task['title'] for task in google_tasks]
    for task in trello_tasks:
        if task['name'] not in google_task_titles:
            # This task is in Trello but not in Google Tasks, so add it
            new_task = {
                'title': task['name'],
                'notes': task.get('desc', ''),
                'due': task.get('due', None)
            }
            google_service.tasks().insert(tasklist=google_tasklist_id, body=new_task).execute()

    # Similarly, add missing Google tasks to Trello
    # This part is left as an exercise or can be customized based on specific needs

    print("Synchronization complete.")

if __name__ == '__main__':
    # Example usage
    trello_board_id = 'your_trello_board_id'
    google_tasklist_id = 'your_google_tasklist_id'
    synchronize_tasks(trello_board_id, google_tasklist_id)
