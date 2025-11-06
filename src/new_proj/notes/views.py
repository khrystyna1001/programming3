from django.shortcuts import render, get_object_or_404
from notes.models import Notes

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def user_page(request):
    return render(request, "profile.html")

def notes_page(request):
    notes = Notes.objects.all()
    return render(request, "notes.html", context={"notes": notes})

def note_page(request, id):
    note = get_object_or_404(Notes, pk=id)
    return render(request, "note.html", context={"note": note})