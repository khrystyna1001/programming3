from django.shortcuts import render
from notes.models import Notes
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django_htmx.http import HttpResponseClientRedirect
from notes.forms import NotesForm


# Create your views here.

def home_page(request):
    return render(request, "home.html")

def user_page(request):
    return render(request, "profile.html")


def notes_listing(request):
    template_name = "notes.html"
    if request.htmx:
        template_name += "#notes-table"

    notes = Notes.objects.all()

    return render(
        request,
        template_name,
        {
            "notes": notes,
        },
    )

def note_detail(request, pk):
    template_name = "note.html"
    if request.htmx:
        template_name += "#card-body"

    note = Notes.objects.get(pk=pk)

    return render(
        request,
        template_name,
        {
            "note": note,
        },
    )

def note_create(request):
    template_name = "create_note.html"
    if request.htmx:
        template_name += "#note-form"

    return render(
        request,
        template_name,
    )

def note_update(request, pk):
    template_name = "note.html"
    if request.htmx:
        template_name += "#note-form"

    note = Notes.objects.get(pk=pk)

    return render(
        request,
        template_name,
        {
            "note": note,
        },
    )

def note_delete(request, pk):
    template_name = "note.html"
    if request.htmx:
        template_name += "#note-form"

    note = Notes.objects.get(pk=pk)

    return render(
        request,
        template_name,
        {
            "note": note,
        },
    )