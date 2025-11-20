from django.shortcuts import render, get_object_or_404, HttpResponse
from notes.models import Notes, TextBlock
from django.views.decorators.http import require_http_methods


# Create your views here.
def home_page(request):
    return render(request, "home.html")

def user_page(request):
    return render(request, "profile.html")

def notes_page(request):
    notes = Notes.objects.all()
    return render(request, "notes.html", context={"notes": notes})

def note_page(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    text_blocks = TextBlock.objects.filter(note=note)
    return render(request, "note.html", context={
        "note": note,
        "text_blocks": text_blocks
    })


def add_text_block(request, note_id):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=note_id)
        new_block = TextBlock.objects.create(
            note=note, 
            content=''
        )
        context = {
            'note': note,
            'new_block': new_block
        }
        return render(request, '_text_block.html', context)
    return HttpResponse(status=405)

def update_block(request, block_id):
    if request.method == 'POST' and request.content_type == 'text/plain':
        try:
            block = get_object_or_404(TextBlock, pk=block_id)
            new_content = request.body.decode('utf-8').strip() 

            if new_content == '':
                block.content = '' 
            else:
                block.content = new_content
            
            block.save()
            return HttpResponse(status=204) 

        except Exception as e:
            return HttpResponse(status=500, content=f"Error: {e}")
            
    return HttpResponse(status=405)

@require_http_methods(["DELETE"])
def delete_block(request, block_id):
    try:
        block = TextBlock.objects.get(pk=block_id)
        note = block.note
        if TextBlock.objects.filter(note=note).count() > 1:
            block.delete()
            return HttpResponse('', status=200, content_type='text/html')
        else:
            block.content = ''
            block.save()
            return HttpResponse('', status=200, content_type='text/html')
    except (TextBlock.DoesNotExist, Notes.DoesNotExist):
        return HttpResponse(status=404)