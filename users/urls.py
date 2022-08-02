from django.urls import path
from .views import UserCreateView, UserDetailsView, UserListView, UserLoginView

urlpatterns = [
    path('signup', UserCreateView.as_view()),
    path('login', UserLoginView.as_view()),
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailsView.as_view()),
]