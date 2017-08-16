from django.db import models

class Folder(models.Model):
    photographer = models.CharField(max_length=100)
    dslr = models.BooleanField(default=True)
    folder_name = models.CharField(max_length=100)
    folder_logo = models.CharField(max_length=100)

    def __str__(self):
        return self.folder_name + ' - ' + self.photographer

class Photo(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    photo_name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.photo_name
