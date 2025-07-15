from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.http import FileResponse

import pandas as pd
import io

@login_required
def index(request):
    context = {}
    return render(request, "pengeluaran/index.html", context)

# class PengeluaranListView(LoginRequiredMixin, ListView):
#     model = Pengeluaran
#     template_name = "pengeluaran/pengeluaran/list.html"
#     context_object_name = 'pengeluaran_list'

@login_required
def pengeluaran_list(request):
    # pencarian
    q = request.GET.get("q")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    # data = Pengeluaran.objects.all()
    data = request.user.pengeluaran_set.all()
    
    if q:
        data = data.filter(Q(nama__icontains=q))

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

    data = data.order_by("-created_at")
    paginator = Paginator(data, 10) # 10 adalah data per halaman
    page_number = request.GET.get('page')
    pengeluaran_list = paginator.get_page(page_number)

    template_name = "pengeluaran/pengeluaran/list.html"
    context = {
        "pengeluaran_list": pengeluaran_list,
    }
    return render(request, template_name, context)

# class PengeluaranCreateView(LoginRequiredMixin, CreateView):
#     model = Pengeluaran
#     form_class = PengeluaranForm
#     template_name = "pengeluaran/pengeluaran/form.html"
#     success_url = reverse_lazy("pengeluaran:pengeluaran_list")

@login_required
def pengeluaran_create(request):
    form = PengeluaranForm(request.POST or None)
    success_url = "pengeluaran:pengeluaran_list"
    template_name = "pengeluaran/pengeluaran/form.html"

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

class PengeluaranUpdateView(LoginRequiredMixin, UpdateView):
    model = Pengeluaran
    form_class = PengeluaranForm
    template_name = "pengeluaran/pengeluaran/form.html"
    success_url = reverse_lazy("pengeluaran:pengeluaran_list")

class PengeluaranDeleteView(LoginRequiredMixin, DeleteView):
    model = Pengeluaran
    template_name = "pengeluaran/pengeluaran/konfirmasi_hapus.html"
    success_url = reverse_lazy("pengeluaran:pengeluaran_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        return context

# class PengeluaranDetailView(DetailView):
#     model = Pengeluaran
#     template_name = "pengeluaran/pengeluaran_detail.html"
#     context_object_name = "pengeluaran"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['detail_pengeluaran_list'] = DetailPengeluaran.objects.all()
#         return context

@login_required    
def pengeluaran_detail(request, pk):
    
    pengeluaran = get_object_or_404(Pengeluaran, pk=pk)
    data = pengeluaran.detailpengeluaran_set.all()

    # pencarian
    q = request.GET.get("q")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if q:
        data = data.filter(Q(nama__icontains=q))

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

    # end pencarian

    data = data.order_by("-created_at")
    paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    detail_pengeluaran_list = paginator.get_page(page_number)

    context = {
        "pengeluaran": pengeluaran,
        "detail_pengeluaran_list": detail_pengeluaran_list,
    }
    return render(request, "pengeluaran/pengeluaran/detail.html", context)


# ----------------------PengeluaranDetail-----------------------------------------

# class PengeluaranDetailListView(ListView):
#     model = DetailPengeluaran
#     template_name = "pengeluaran/pengeluaran_detail/list.html"
#     context_object_name = 'pengeluaran_detail_list'

@login_required
def pengeluaran_detail_list(request):
    # pencarian
    q = request.GET.get("q")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    data = DetailPengeluaran.objects.all()
    # data = DetailPengeluaran.objects.all().order_by("-created_at")
    if q:
        data = data.filter(Q(nama__icontains=q))

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

    data = data.order_by("-created_at")
    paginator = Paginator(data, 10) # 10 adalah data per halaman
    page_number = request.GET.get('page')
    pengeluaran_detail_list = paginator.get_page(page_number)

    context = {
        "pengeluaran_detail_list": pengeluaran_detail_list,
    }
    return render(request, "pengeluaran/pengeluaran_detail/list.html", context)

@method_decorator(login_required, name="dispatch")
class PengeluaranDetailCreateView(CreateView):
    model = DetailPengeluaran
    form_class = PengeluaranDetailForm
    template_name = "pengeluaran/pengeluaran_detail/form.html"
    success_url = reverse_lazy("pengeluaran:pengeluaran_detail_list")

@login_required
def pengeluaran_detail_create(request, pengeluaran_id=None, pengeluaran_detail_id=None):
    pengeluaran = get_object_or_404(Pengeluaran, pk=pengeluaran_id)

    if pengeluaran_detail_id:
        pengeluaran_detail = get_object_or_404(DetailPengeluaran, pk=pengeluaran_detail_id)
    else:
        pengeluaran_detail = None

    form = PengeluaranDetailForm(request.POST or None, instance=pengeluaran_detail)

    form.fields['pengeluaran'].widget = forms.HiddenInput()
    form.fields['pengeluaran'].initial = pengeluaran

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pengeluaran:pengeluaran_detail", pk=pengeluaran.id)
    
    

    context = {
        "form": form,
        "pengeluaran": pengeluaran,
    }
    return render(request, "pengeluaran/pengeluaran_detail/tambah.html", context)

# class PengeluaranDetailUpdateView(LoginRequiredMixin, UpdateView):
#     model = DetailPengeluaran
#     form_class = PengeluaranDetailForm
#     template_name = "pengeluaran/pengeluaran_detail/form.html"
#     success_url = reverse_lazy("pengeluaran:pengeluaran_detail_list")

@login_required
def pengeluaran_detail_update(request, pk):
    obj = get_object_or_404(DetailPengeluaran, pk=pk)
    form = PengeluaranDetailForm(request.POST or None, instance=obj)
    next_url = request.GET.get("next") or request.POST.get("next")

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(next_url or "pengeluaran:pengeluaran_detail_list")
        
    context = {
        "form": form
    }
    return render(request, "pengeluaran/pengeluaran_detail/form.html", context)


@login_required
def pengeluaran_detail_delete(request, pk):
    obj = get_object_or_404(DetailPengeluaran, pk=pk)
    next_url = request.GET.get("next") or request.POST.get("next") or reverse_lazy("pengeluaran:pengeluaran_detail_list")
    
    if request.method == "POST":
        obj.delete()
        return redirect(next_url)
    
    context = {
        "next_url" : next_url,
        "obj": obj
    }
    return render(request, "pengeluaran/pengeluaran_detail/konfirmasi_hapus.html", context)

class PengeluaranDetailDetailView(LoginRequiredMixin, DetailView):
    model = DetailPengeluaran
    template_name = "pengeluaran/pengeluaran_detail/detail.html"
    context_object_name = "pengeluaran_detail"

def download_file(reqeust, pk):
    obj = get_object_or_404(Pengeluaran, pk=pk)
    df = pd.DataFrame(obj.detailpengeluaran_set.all().values())

    # konversi waktu (time zone)
    df['created_at'] = df['created_at'].dt.tz_localize(None)
    df['updated_at'] = df['updated_at'].dt.tz_localize(None)

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="fileku.xlsx")