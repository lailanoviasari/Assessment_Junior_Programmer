from django.db import models

# Create your models here.
class Mobil(models.Model):
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.IntegerField()
    harga_dasar = models.FloatField(max_length=20)
    dana_pinjaman_bank = models.FloatField(max_length=20, null=True, blank=True)
    suku_bunga = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.merk} | {self.model} | {self.tahun}"
    
    
class Service(models.Model):
    mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE)
    tanggal = models.DateField()
    deskripsi = models.CharField(max_length=200)
    biaya = models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.tanggal} | {self.deskripsi}"