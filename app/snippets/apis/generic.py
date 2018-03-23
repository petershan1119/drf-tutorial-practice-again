from rest_framework import generics

from ..serializers import SnippetSerializer
from ..models import Snippet


__all__ = (
    'SnippetList',
    'SnippetDetail',
)

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer