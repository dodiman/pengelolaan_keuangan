from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

class Catatan(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100, null=True, blank=True)
    isi_catatan = models.TextField()
    kategori = models.CharField(max_length=50, default="lainnya", blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.judul}"
