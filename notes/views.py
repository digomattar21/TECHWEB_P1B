from django.shortcuts import render
from django.shortcuts import redirect

from .models import Note, Tag


def index(request):
    if request.method == 'POST':
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
            tag = Tag.objects.filter(name=tagName)
            notes = Note.objects.filter(tag__in=tag)
            if len(notes)<=1: 
                tag.delete()
            note.delete()

        else:
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            tagName = request.POST.get('tagName')
            existingTag = Tag.objects.filter(name=tagName)
            if existingTag:
                tag = Tag.objects.get(name=tagName)
                note=Note(title=title,content=content,tag = tag)
                note.save()
                tag.save()
                
            else:
                tag = Tag(name=tagName)
                tag.save()
                note = Note(title=title,content=content, tag=tag)
                note.save()
                
                
            

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes, 'tags': all_tags})

def edit(request):
    if request.POST.get('edit'):
        noteToEdit = Note.objects.get(id=request.POST.get('id'))
        return render(request, 'notes/edit.html', {'noteToEdit':noteToEdit})

def tagDetails(request):
    if request.method == 'POST':
        tag = Tag.objects.get(name=request.POST.get('tagName'))
        tags = Tag.objects.all()
        notes = Note.objects.filter(tag=tag)
        print(tag)
        print(notes)
        return render(request, 'notes/tagDetails.html', {'notes':notes, 'tags':tags})
