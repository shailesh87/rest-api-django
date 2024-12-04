from django.urls import path
from .views import AudioSnippetAPIView, HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('audio-snippets/', AudioSnippetAPIView.as_view(), name='audio-snippets'),
]
