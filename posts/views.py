from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.versioning import AcceptHeaderVersioning
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer
from .pagination import CustomPagination


'''
class PostViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ScopedRateThrottle]
    http_method_names = "get"
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields =['title', 'author']
    search_fields = ["title"]
    ordering_fields=['created_at', 'author']
'''


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ScopedRateThrottle]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields =['title']
    search_fields = ["title"]
    ordering_fields=['created_at', 'author']
    versioning_class = AcceptHeaderVersioning


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ScopedRateThrottle]
    versioning_class = AcceptHeaderVersioning


'''
class UserViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ScopedRateThrottle]
    http_method_names = "get"
'''

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ScopedRateThrottle]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields =['name']
    search_fields = ["author"]
    ordering_fields=['author']
    versioning_class = AcceptHeaderVersioning


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ScopedRateThrottle]
    versioning_class = AcceptHeaderVersioning
