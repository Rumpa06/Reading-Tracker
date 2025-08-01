import requests
from django.conf import settings

def search_google_books(query, max_results=5):
    api_key = settings.GOOGLE_BOOKS_API_KEY
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': query,
        'maxResults': max_results,
        'key': api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    return []
