from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from books.forms import ReviewForm
from books.models import Book, BookReview
from django.views import generic


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q')
        if search_query:
            books = Book.objects.filter(title__icontains=search_query)
        paginator = Paginator(books, 2)
        page = request.GET.get('page', 1)
        page_obj = paginator.get_page(page)
        return render(request, 'books/list.html', {'page_obj': page_obj})


# class BooksView(generic.ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = ReviewForm()
        return render(request, 'books/detail.html', {'book': book, 'form': review_form})


class BooksReview(View):

    def post(self, request, id):
        book = get_object_or_404(Book, id=id)
        form = ReviewForm(data=request.POST, instance=book)
        if form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=form.cleaned_data['stars_given'],
                comment=form.cleaned_data['comment']

            )
            return redirect(reverse('books:book_detail', kwargs={'id': book.id}))
        return render(request, 'books/detail.html', {'book': book, 'form': form})


class BooksDetailView(generic.DetailView):
    template_name = 'books/detail.html'
    pk_url_kwarg = 'id'
    model = Book


class Search(View):
    def get(self, request):
        books = Book.objects.all()
        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)
        return render(request, 'books/list.html', {'books': books})


class BookReviewEditView(View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        form = ReviewForm(instance=review)
        return render(request, 'books/review-edit.html', {'book': book, 'review': review, 'form': form})

    def post(self, request,  book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        form = ReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(reverse('books:book_detail', kwargs={'id': book.id}))
        return render(request, 'books/review-edit.html', {'book': book, 'review': review, 'form': form})


class BookReviewDeleteConfirm(View):
    def get(self, request,  book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        return render(request, 'books/delete-review.html', {'book': book, 'review': review})


class BookReviewDelete(View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review.delete()
        messages.success(request, 'You have successfully this review')
        return redirect(reverse('books:book_detail', kwargs={'id': book.id}))

