from celery import shared_task
from .models import File
import os


@shared_task()
def process(file_id):
    try:
        fileobj = File.objects.get(id=file_id)
        ext = fileobj.file.name.split('.')[-1]
        filetype = {('png', 'jpg', 'webp', 'jpeg'): "Image_", ('txt', 'docx', 'doc'): "Text_",
                    ('mp3', 'wav'): "Audio_", 'mp4': "Video_"}
        filename = next(v for k, v in filetype.items() if ext in k) + str(file_id) + '.' + ext
        os.rename('media/' + str(fileobj.file.name), 'media/' + filename)
        fileobj.file.name = filename
        fileobj.processed = True
        fileobj.save()
    except Exception as e:
        raise e
    return "File processing started!"


