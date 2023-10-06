from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import basisPengetauan,Gejala,Penyakit
from .fungsi import dict, chainFowarding



def home(request):

    return render(request, 'main/main.html')
    
def form(request):
    if request.method == 'POST':
        inputGejala = None
        if inputGejala:
            inputGejala.pop()
        else:
            rules = basisPengetauan.objects.all()
            gejala = Gejala.objects.all()
            rule = str(rules)
            #rule = {a.Penyakit: a.gejala for a in rules}
            inputGejala = request.POST.getlist('input_gejala')
            dict.dict(rule)
            print(inputGejala)
            chainFowarding.chainFowarding(dict.getDict(),inputGejala)
            request.session['penyakit'] = chainFowarding.getPenyakit()

            return HttpResponseRedirect("/sistem-pakar-diagnosa-penyakit-kulit/hasil/")

    gejala = Gejala.objects.all()
    return render(request, "main/form.html.",{'gejala': gejala})

def hasil(request):
    penyakit_hasil = str(request.session.get('penyakit', None))
    data = penyakit_hasil
    penyakit = Penyakit.objects.filter(namaPenyakit = penyakit_hasil )

    return render(request, "main/hasil.html.",{'penyakit': penyakit, 'data': data})


