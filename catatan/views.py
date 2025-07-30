from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.dateparse import parse_date

from .models import Catatan
from .forms import CatatanForm

@login_required
def catatan_list(request):
    # pencarian
    q = request.GET.get("q")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    # list
    data = request.user.catatan_set.all()

    if q:
        data = data.filter(Q(tag__icontains=q) | Q(judul__icontains=q))
    
    if start_date and end_date:
        start = parse_date(start_date)
        end = parse_date(end_date)
        if start_date and end_date:
            data = data.filter(created_at__date__range=(start, end))
    elif start_date:
        start = parse_date(start_date)
        if start:
            data = data.filter(created_at__date__gte=start)
    elif end_date:
        end = parse_date(end_date)
        if end:
            data = data.filter(created_at__date__lte=end)

    # sort
    data = data.order_by("-created_at")

    # paginator
    paginator = Paginator(data, 10) # 10 adalah data per halaman
    page_number = request.GET.get('page')
    obj_list = paginator.get_page(page_number)

    template_name = "catatan/list.html"
    context = {
        "catatan_list": obj_list,
        "key_list": ["judul", "isi_catatan"],
        "kolom_list": ["tanggal", "Judul", "Catatan", "#"],
        "nama_url_delete": "catatan:delete",
        "nama_url_update": "catatan:update",
        "nama_url_detail": "catatan:detail",
    }
    return render(request, template_name, context)

@login_required
def catatan_create(request):
    form = CatatanForm(request.POST or None)
    success_url = "catatan:list"
    template_name = "catatan/partials/form.html"

    if request.method == "POST":
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect(success_url)
        
    context = {
        "form": form
    }
    return render(request, template_name, context)

@login_required
def catatan_update(request, pk):
    catatan = get_object_or_404(Catatan, pk=pk)
    success_url = "catatan:list"

    form = CatatanForm(instance=catatan)
    if request.method == "POST":
        form = CatatanForm(request.POST, instance=catatan)
        if form.is_valid():
            form.save()
            return redirect(success_url)

        
    template_name = "catatan/partials/form.html"

    context = {
        "form": form
    }
    return render(request, template_name, context)

@login_required
def catatan_detail(request, pk):
    catatan = get_object_or_404(Catatan, pk=pk)
    template_name = "catatan/detail.html"
    
    context = {
        "catatan": catatan
    }
    return render(request, template_name, context)

@login_required
def catatan_delete(request, pk):
    catatan = get_object_or_404(Catatan, pk=pk)

    template_name = "catatan/konfirmasi_hapus.html"
    success_url = "catatan:list"

    if request.method == "POST":
        catatan.delete()
        return redirect(success_url)
    
    context = {
        "obj": catatan
    }
    return render(request, template_name, context)
