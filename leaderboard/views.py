from django.shortcuts import render
from book.models import Book
# from readlist.models import Readlist
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from leaderboard.forms import 

@csrf_exempt
def leaderboard_option(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "leaderboard.html", context)

@csrf_exempt
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def get_readlists(request):
#     data = Readlist.objects.all()
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json") 