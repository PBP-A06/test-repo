from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import AddBooksToReadlistForm
from .models import Readlist, Book
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

#show all existing readlists
def show_readlist(request):
    top_5_readlists = Readlist.objects.all()

    context = {
        'top_5_readlists': top_5_readlists,
    }

    return render(request, 'readlist.html', context)

#get readlist details
def readlist_detail(request, readlist_id):
    readlist = get_object_or_404(Readlist, id=readlist_id)
    return HttpResponse(serializers.serialize("json", readlist), content_type="application/json")
    # return render(request, 'readlist_detail.html', {'readlist': readlist})

#TODO: make login required
# @login_required(login_url='/login')
def create_readlist(request):
    if request.method == 'POST':
        form = AddBooksToReadlistForm(request.POST)
        if form.is_valid():
            readlist = form.save(commit=False)
            readlist.user = request.user
            readlist.save()
            form.save_m2m()  # This is needed to save the many-to-many relationship
            return render(request, 'create_readlist.html', {'form': form})
    else:
        form = AddBooksToReadlistForm()
    return render(request, 'create_readlist.html', {'form': form})

#get all readlist
def get_readlists():
    readlists = Readlist.objects.all()
    return HttpResponse(serializers.serialize('json', readlists))

#increment number of likes
def like_a_readlist(request, id):
    updated_readlist = Readlist.objects.get(pk=id)
    updated_readlist.likes += 1
    updated_readlist.save()
    return HttpResponseRedirect(reverse('main:show_main'))


