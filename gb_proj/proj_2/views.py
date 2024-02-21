from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from .forms import ProductForm


# Представления для клиентов
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'proj_2/client_list.html', {'clients': clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'proj_2/client_detail.html', {'client': client})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'proj_2/client_form.html', {'form': form})


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'proj_2/client_form.html', {'form': form})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'proj_2/client_confirm_delete.html', {'client': client})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'proj_2/add_product.html', {'form': form})
