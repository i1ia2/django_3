
import phone as phone
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request,):
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = phones.order_by('name')
    if sort == 'min_price':
        phones = phones.order_by('price')
    if sort == 'max_price':
        phones = phones.order_by('-price')
    template = 'catalog.html'
    context = {'phones': phones,}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
