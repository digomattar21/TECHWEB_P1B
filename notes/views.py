from django.shortcuts import render
from django.shortcuts import redirect

from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        if request.POST.get('edit'):
            title = request.POST.get('title')
            content = request.POST.get('content')
            tag = request.POST.get('tag')
            note = Note.objects.get(id=request.POST.get('id'))
            if title: note.title=title
            if content: note.content=content
            if tag: note.tag=tag
            note.save()
            
        elif request.POST.get('id'):
            note = Note.objects.get(id=request.POST.get('id'))
            tagName = request.POST.get('tagName')
            print('tagName', tagName)
            tag = Tag.objects.filter(name=tagName)
            if len(tag)<=1: tag.delete()
            note.delete()

        else:
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            tagName = request.POST.get('tagName')
            existingTag = Tag.objects.filter(name=tagName)
            if existingTag:
                note=Note(title=title,content=content,tagName=tagName)
                existingTag.note_set.add(note)
                note.save()
                tag.save()

                tag.save()
                print('exstingtag')
            else:
                note = Note(title=title,content=content, tagName=tagName)
                note.save()
                tag = Tag(name=tagName, note=note)
                tag.save()
            

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes, 'tags': all_tags})

def edit(request):
    if request.POST.get('edit'):
        noteToEdit = Note.objects.get(id=request.POST.get('id'))
        return render(request, 'notes/edit.html', {'noteToEdit':noteToEdit})