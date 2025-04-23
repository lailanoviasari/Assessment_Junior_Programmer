from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .form import MobilForm, ServiceForm
from .models import Mobil, Service

# Create views here.
def tambah_mobil(request):
    if request.method == 'POST':
        form = MobilForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = MobilForm()
        return render(request, 'mobil/tambah_mobil.html', {'form':form})
    

# list views here.
def list_mobil(request):
    mobil = Mobil.objects.all()
    return render(request, 'mobil/index.html', {'mobil':mobil})

def detail_mobil(request, pk):
    mobil = Mobil.objects.get(id=pk)

    form = ServiceForm()
    service = mobil.service_set.all()
    return render(request, 'mobil/detail_mobil.html', {'mobil':mobil, 'form':form, 'service': service})

def tambah_service(request, pk):
    mobil = Mobil.objects.get(id=pk)

    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.mobil = mobil
            service.save()
    return redirect('detail_mobil', pk=pk)

# Edit views here
def edit_mobil(request, pk):
    mobil = Mobil.objects.get(id=pk)

    if request.method == 'POST':
        form = MobilForm(request.POST, instance=mobil)

        if form.is_valid():
            form.save()
            return redirect('list')
    
    else:
        form = MobilForm(instance=mobil)
    return render(request, 'mobil/edit_mobil.html', {'form':form, 'mobil':mobil})

def edit_service(request, pk):
    service = Service.objects.get(id=pk)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            return redirect('list')
    
    else:
        form = ServiceForm(instance=service)
    return render(request, 'mobil/edit_service.html', {'form':form})


# Hapus views here
def hapus_mobil(request, pk):
    mobil = Mobil.objects.get(id=pk)

    if request.method == 'POST':
        mobil.delete()
    return redirect('list')

