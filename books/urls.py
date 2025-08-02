from django.urls import path, include
from .views import BookViewSet, dashboard, google_books_search
from rest_framework.routers import DefaultRouter
from .views import book_search
from . import views

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book')

urlpatterns = [
    path('', book_search, name='home'),  # renders on root URL
    path('api/', include(router.urls)),
    path('dashboard/', dashboard),
    path('google-books/', google_books_search),
    path('search/', book_search, name='book_search'),
    path('save/', views.save_book, name='save_book'),
    path('my-books/', views.book_list, name='my_books')

]
