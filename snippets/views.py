from snippets.models import Snippet, User, Map
# from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer, MapSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import permissions



class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# class UserAuthList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserAuthSerializer
#
#
# class UserAuthDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserAuthSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # permission_classes = (IsOwnerOrReadOnly,)

# class SignInUser(generics.ListCreateAPIView):
#     queryset = User.objects.raw('SELECT * FROM Users')
#     serializer_class = UserSerializer
#
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     permission_classes = (IsOwnerOrReadOnly,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer