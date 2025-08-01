import json
import requests
from django.conf import settings
from django.db.models import Count
from django.db.models.functions import ExtractYear, TruncDate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets 

from .models import Book
from .serializers import BookSerializer
from .utils import search_google_books

# CRUD API ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# API Integration - Google Books API
@api_view(['GET'])
def google_books_search(request):
    query = request.GET.get('q')
    if not query:
        return Response({'error': 'No query provided'}, status=400)

    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={settings.GOOGLE_BOOKS_API_KEY}'
    response = requests.get(url)
    return Response(response.json())


# Dashboard View - Data Visualization from DB

def dashboard(request):
    total_books = Book.objects.count()

    # Books read per year
    book_counts = Book.objects.annotate(
        year=ExtractYear('published_date')
    ).values('year').annotate(count=Count('id')).order_by('year')

    # Most read authors
    most_read_authors = Book.objects.values('author').annotate(
        count=Count('id')
    ).order_by('-count')[:5]  # Top 5 authors

    chart_data = json.dumps(list(book_counts))
    author_data = json.dumps(list(most_read_authors))

    return render(request, 'books/dashboard.html', {
        'total_books': total_books,
        'chart_data': chart_data,
        'author_data': author_data
    })

# Google Books Search HTML View
def book_search(request):
    results = []
    query = request.GET.get('q')
    if query:
        results = search_google_books(query)
    return render(request, 'books/book_search.html', {'results': results, 'query': query})

@csrf_exempt
def save_book(request):
    if request.method == 'POST':
        title = request.POST.get('title') or "Untitled"
        author = request.POST.get('author') or "Unknown"
        thumbnail = request.POST.get('thumbnail') or ""

        Book.objects.get_or_create(
            title=title,
            author=author,
            defaults={'thumbnail': thumbnail}
        )

    return redirect('search_books')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

