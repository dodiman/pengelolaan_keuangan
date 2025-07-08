from django.db import models
from core.models import BaseModel

class Pengeluaran(BaseModel):
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


