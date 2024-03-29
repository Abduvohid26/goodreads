from django.urls import path
from .views import BooksView, BookDetailView, BooksReview, BookReviewEditView, BookReviewDeleteConfirm, BookReviewDelete
app_name = 'books'

urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:id>/reviews/', BooksReview.as_view(), name='book_review'),
    path('<int:book_id>/review/<int:review_id>/edit/', BookReviewEditView.as_view(), name='edit_review'),
    path(
        '<int:book_id>/review/<int:review_id>/delete-confirm/',
        BookReviewDeleteConfirm.as_view(),
        name='delete_review_confirm'),
    path('<int:book_id>/review/<int:review_id>/delete/', BookReviewDelete.as_view(), name='delete_review'),

]