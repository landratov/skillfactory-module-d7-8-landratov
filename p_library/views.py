from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

from .models import Book, Publisher, Author, Friend
from .forms import AuthorForm, FriendForm, ProfileCreationForm


class RegisterView(FormView):

    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)


class CreateUserProfile(FormView):

    form_class = ProfileCreationForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('p_library:main')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('p_library:login'))
        return super(CreateUserProfile, self).dispatch(request, *args,
                                                       **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorEdit(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'


class FriendEdit(UpdateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


def friend_delete(request, pk):
    if request.method == 'POST':
        if not pk:
            return redirect(reverse_lazy('p_library:friend_list'))
        else:
            friend = Friend.objects.filter(id=pk).first()
            if not friend:
                return redirect(reverse_lazy('p_library:friend_list'))
            friend.delete()
            return redirect(reverse_lazy('p_library:friend_list'))
    else:
        return redirect(reverse_lazy('p_library:friend_list'))


def index(request):
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку",
                   "books": books}
    if request.user.is_authenticated:
        biblio_data['username'] = request.user.username
    return render(request, 'index.html', biblio_data)


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect(reverse_lazy('main'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect(reverse_lazy('main'))
            book.copy_count += 1
            book.save()
        return redirect(reverse_lazy('main'))
    else:
        return redirect(reverse_lazy('main'))


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect(reverse_lazy('main'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect(reverse_lazy('main'))
    else:
        return redirect(reverse_lazy('main'))


def publishers(request):
    publishers_data = {"publishers": Publisher.objects.order_by('title')}
    return render(request, 'publishers.html', publishers_data)


def bookview(request, pk):
    book = {"book": Book.objects.filter(id=pk).first()}
    return render(request, 'book_view.html', book)

