from django.db import models


class Pasien(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50, null=True)
    jenisKelamin = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Penyakit = models.CharField(max_length=50)
    gejala = models.TextField()

    def __str__(self):
        return self.nama

class Penyakit(models.Model):
    namaPenyakit = models.CharField(max_length=50)
    solusi = models.TextField()

    def __str__(self):
        return self.namaPenyakit

class Gejala(models.Model):
    namaGejala = models.CharField(max_length=500)
    
    def __str__(self):
        return self.namaGejala

class basisPengetauan(models.Model):
    Penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
    gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Penyakit)+' : '+str(self.gejala)
    
    