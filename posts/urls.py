from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import UserViewsets, PostViewsets
from .views import PostList, PostDetail, UserList, UserDetail

# router = SimpleRouter()
# router.register("users", UserViewsets, basename="users")
# router.register("", PostViewsets, basename="posts")

# urlpatterns = router.urls


urlpatterns = [
    path("users/", UserList.as_view(), name='user_list'),
    path("users/<int:pk>/", UserDetail.as_view(), name='user_detail'),
    path("", PostList.as_view(), name='post_list'),
    path("<int:pk>/", PostDetail.as_view(), name='post_detail'),
]
