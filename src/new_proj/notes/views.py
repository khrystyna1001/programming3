from django.shortcuts import render, get_object_or_404, HttpResponse
from notes.models import Notes, TextBlock
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
def home_page(request):
    return render(request, "home.html")

def user_page(request):
    return render(request, "profile.html")

def notes_page(request):
    notes = Notes.objects.all()
    return render(request, "notes.html", context={"notes": notes})

def note_page(request, id):
    note = get_object_or_404(Notes, pk=id)
    return render(request, "note.html", context={"note": note})

@ensure_csrf_cookie
def note_content(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    text_blocks = TextBlock.objects.filter(note=note)
    return render(request, "note.html", context={"note": note, "text_blocks": text_blocks})

@ensure_csrf_cookie
def add_text_block(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    text_block = TextBlock.objects.create(note=note, content="")
    return render(request, "text_block.html", context={"text_block": text_block})

@ensure_csrf_cookie
def update_text_block(request, block_id):
    if request.method == "POST":
        text_block = get_object_or_404(TextBlock, pk=block_id)
        text_block.content = request.POST.get("content", "")
        text_block.save()
        return render(request, "text_block.html", context={"text_block": text_block})
    return HttpResponse(status=400)

@ensure_csrf_cookie
def delete_text_block(request, block_id):
    text_block = get_object_or_404(TextBlock, pk=block_id)
    text_block.delete()
    return HttpResponse(status=204)
