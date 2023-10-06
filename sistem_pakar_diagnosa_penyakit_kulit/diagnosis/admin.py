from django.contrib import admin
from .models import Penyakit,Pasien,Gejala,basisPengetauan

admin.site.register(Pasien)
admin.site.register(Penyakit)
admin.site.register(Gejala)
admin.site.register(basisPengetauan)

# Register your models here.
