from django.urls import path, include
from .views import CreateRecord, MainPage, SearchPage, IssuedBooks

urlpatterns = [
    path('create/', CreateRecord.as_view(), name="create"),
    path('', MainPage.as_view(), name="mainpage"),
    path('search/', SearchPage.as_view(), name='search'),
    path('issued/<int:pk>/', IssuedBooks.as_view(), name='addBooks'),
]