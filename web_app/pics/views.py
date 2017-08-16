from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Folder, Photo


def index(request):
    all_folders = Folder.objects.all()
    return render(request, 'pics/index.html', {'all_folders': all_folders})


def detail(request, album_id):
    # the below is using get_object shortcut to write this: folder = Folder.objects.get(pk=album_id) as a try, except.
    folder = get_object_or_404(Folder, pk=album_id)

    return render(request, 'pics/detail.html', {'folder': folder})


def favorite(request, album_id):
    folder = get_object_or_404(Folder, pk=album_id)
    try:
        selected_photo = folder.photo_set.get(pk=request.POST['photo'])
    except (KeyError, Photo.DoesNotExist):
        return render(request, 'pics/detail.html', {
            'folder': folder,
            'error_message': "You did not select a valid photo"
        })
    else:
        selected_photo.is_favorite = True
        selected_photo.save()
        return render(request, 'pics/detail.html', {'folder': folder})