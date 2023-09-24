from django.core.validators import FileExtensionValidator
from django.db import models

image_ext_validator = FileExtensionValidator(
    allowed_extensions=['png', 'jpg', 'webp', 'jpeg'],
)


# Create your models here.
class File(models.Model):
    file = models.FileField(validators=[
        FileExtensionValidator(['png', 'jpg', 'webp', 'jpeg', 'txt', 'docx', 'doc', 'mp3', 'wav', 'mp4'])])
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    processed = models.BooleanField(default=False, blank=True)
