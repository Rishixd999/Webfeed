from django.urls import path
from .views import home, signup_view, login_view, logout_view, like_post
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path("add_news/", views.add_news, name="add_news"),
]
