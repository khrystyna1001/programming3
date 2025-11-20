from django.shortcuts import render, get_object_or_404, HttpResponse
from notes.models import Notes
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import QueryDict

# Create your views here.
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
    success_url = "/notes/"


class NotesUpdateView(UpdateView):
    model = Notes
    fields = ["title", "content"]
    template_name = "note.html"
    context_object_name = "note"
    success_url = "/notes/"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            request.POST = QueryDict(request.body.decode('utf-8'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=204)