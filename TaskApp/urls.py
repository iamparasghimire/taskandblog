from django.urls import path
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    PasswordResetCompleteView,
    TaskListView,
    BlogListView,
    LoginView,
    CustomLogoutView,
    SignupView,
    TaskCreateView,
    BlogCreateView,
    TaskUpdateView,
    BlogUpdateView,
    TaskDeleteView,
    BlogDeleteView,
    UserProfileView,
)
from . import views

app_name = "taskapp"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("blog/", BlogListView.as_view(), name="blog"),
    path('add-comment/', views.add_comment, name='add_comment'),
    path('comment-list/<int:pk>/', views.comment_list, name='comment_list'),

    path(
        "user_profile/<slug:username>/", UserProfileView.as_view(), name="user-profile"
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    
    path(
        "password_reset/", CustomPasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset_done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("bcreate/", BlogCreateView.as_view(), name="blog_create"),
    path("update/<slug:slug>/", TaskUpdateView.as_view(), name="task_update"),
    path("bupdate/<slug:slug>/", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<slug:slug>/", TaskDeleteView.as_view(), name="task_delete"),
    path("bdelete/<slug:slug>/", BlogDeleteView.as_view(), name="blog_delete"),
]
