from django.shortcuts import render
from notes.models import Notes
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import QueryDict
from django_htmx.http import HttpResponseClientRedirect


# Create your views here.

def redirect_view():
    return HttpResponseClientRedirect("notes.html")

def home_page(request):
    return render(request, "home.html")

def user_page(request):
    return render(request, "profile.html")

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes.html"

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "note.html"

class NotesCreateView(CreateView):
    model = Notes
    fields = ["title", "content"]
    template_name = "create_note.html"
    success_url = '/notes/'


class NotesUpdateView(UpdateView):
    model = Notes
    fields = ["title", "content"]
    template_name = "note.html"
    context_object_name = "note"
    success_url = '/notes/'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            request.POST = QueryDict(request.body.decode('utf-8'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return redirect_view()


class NotesDeleteView(DeleteView):
    model = Notes
    template_name = "note.html"
    context_object_name = "note"
    success_url = '/notes/'

    def get_success_url(self):
        return redirect_view()
