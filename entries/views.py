import imp
import re
from django.shortcuts import render  , redirect

# Create your views here.

from .models import Entry
from .forms import AddEntryForm

def index(request):
    entries = Entry.objects.order_by('-date_added')
    return render(request , 'entries/index.html', {
        'entries': entries
    })

def add(request):
    if request.method == 'POST':
        form = AddEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entries:index')
    else:

        form = AddEntryForm()
    return render(request , 'entries/add.html', {
        'form': form
    })