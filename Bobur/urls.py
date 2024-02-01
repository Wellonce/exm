from django.urls import path
from .views import *

app_name = 'Bobur'

urlpatterns =  [
    path('', HomePageView.as_view(), name = 'home-page'),
    path('about/', AboutView.as_view(), name = 'about-page'),
    path('login/', LoginView.as_view(), name = 'login-page'),
    path('about/', AboutView.as_view(), name = 'about-page'),
    path('post_delete/', Post_Delete_View.as_view(), name = 'delete-page'),
    path('detail/', Post_detailView.as_view(), name = 'detail-page'),
    path('form/', Post_formvView.as_view(), name = 'form-page'),
    path('register/', RegisterView.as_view(), name = 'register-page'),
    path('user/', UserView.as_view(), name = 'user-page'),
    path('create/post', create_post, name = 'create-page'),
    path('update/post', update_post, name = 'update-page'),
]