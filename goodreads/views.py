from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import BookReview


def landing_page(request):
    print(request.COOKIES.get('landing_page'))
    return render(request, 'landing.html')


def home(request):
    book_review = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 10)
    paginator = Paginator(book_review, page_size)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'home.html', {'page_obj': page_obj})

