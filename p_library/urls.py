from django.urls import path, reverse_lazy
from .views import AuthorCreate, AuthorList, AuthorEdit, FriendList, FriendCreate, FriendEdit, \
    book_decrement, book_increment, publishers, index, friend_delete, bookview, RegisterView, CreateUserProfile
from allauth.account.views import login, logout

app_name = 'p_library'

urlpatterns = [
    path('', index, name='main'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorEdit.as_view(), name='author_edit'),
    path('friend/create/', FriendCreate.as_view(), name='friend_create'),
    path('friend/', FriendList.as_view(), name='friend_list'),
    path('friend/<int:pk>/', FriendEdit.as_view(), name='friend_edit'),
    path('friend/<int:pk>/delete/', friend_delete, name='friend_delete'),
    path('book_increment/', book_increment),
    path('book_decrement/', book_decrement),
    path('publishers/', publishers, name='publishers'),
    path('book/<int:pk>/', bookview, name='book'),
    path('register/', RegisterView.as_view(
        template_name='register.html',
        success_url=reverse_lazy('p_library:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(),
         name='profile-create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]