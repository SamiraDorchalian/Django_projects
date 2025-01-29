from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def notes_list_view(request):
    return render(request, 'notes/notes_list.html')