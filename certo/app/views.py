from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'categoria']
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao','preco','marca']

def criar_marca(request, template_name='marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('marca_list')
    return render(request, template_name, {'form': form})
def criar_produto(request, template_name='produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_produto')
    return render(request,template_name,{'form':form})
def listar_marca(request, template_name='marca_list.html'):
    query = request.GET.get('busca')
    if query:
        marca = Marca.objects.filter(nome__icontains=query)
    else:
        marca = Marca.objects.all()
    marcas = {'lista': marca}
    return render(request, template_name, marcas)

def listar_produto(request, template_name='produto_list.html'):
    query = request.GET.get('busca')
    if query:
        produto = Produto.objects.filter(descricao__icontains=query)
    else:
        produto = Produto.objects.all()
    produtos = {'lista': produto}
    return render(request,template_name,produtos)

def editar_marca(request, pk, template_name='marca_form.html'):
    marca = get_object_or_404(Marca, pk = pk)
    form = MarcaForm(request.POST or None, instance=marca)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marca_list')
        else:
            form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})

def editar_produto(request, pk, template_name='produto_form.html'):
    produto = get_object_or_404(Produto, pk = pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_produto')
        else:
            form = ProdutoForm(instance=produto)
    return render(request,template_name,{'form': form})


def deletar_marca(request, pk, template_name="delete_marca.html"):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, template_name, {'marca': marca})

def deletar_produto(request, pk, template_name="produto_delete.html"):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produto')
    return render(request,template_name, {'produto':produto})

def listar_produto_marca(request, pk, template_name='listar_produto_marca.html'):
    produtos = Produto.objects.filter(marca = pk)
    return render(request,template_name,{'produtos':produtos})