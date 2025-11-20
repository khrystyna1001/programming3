from django.shortcuts import render, get_object_or_404, HttpResponse
from notes.models import Notes


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
        
    return render(request, "note.html", context={
        "note": note,
    })

def update_note(request, note_id):
    if request.method == 'POST':
        try:
            note = get_object_or_404(Notes, pk=note_id)
            new_content = request.body.decode('utf-8').strip()
            
            if new_content:
                note.content = new_content
                note.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=400)
                
        except Exception as e:
            return HttpResponse(status=500, content=f"Error: {e}")
    
    return HttpResponse(status=405)
