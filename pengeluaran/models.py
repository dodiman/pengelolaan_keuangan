from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

class Pengeluaran(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=100, null=True, blank=True)
    deskripsi = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.nama}"

class DetailPengeluaran(BaseModel):
    pengeluaran = models.ForeignKey(Pengeluaran, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    jumlah = models.PositiveIntegerField(default=0)
    keterangan = models.CharField(max_length=200)
    total_harga = models.PositiveIntegerField(default=0)


