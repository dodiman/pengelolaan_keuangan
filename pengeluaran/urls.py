from django.urls import path
from . import views

app_name = 'pengeluaran'

urlpatterns = [
    path("pengeluaran/", views.pengeluaran_list, name="pengeluaran_list"),
    path("pengeluaran/tambah/", views.PengeluaranCreateView.as_view(), name="pengeluaran_create"),
    path("pengeluaran/<str:pk>/edit/", views.PengeluaranUpdateView.as_view(), name="pengeluaran_update"),
    path("pengeluaran/<str:pk>", views.pengeluaran_detail, name="pengeluaran_detail"),
    path("pengeluaran/<str:pk>/hapus/", views.PengeluaranDeleteView.as_view(), name="pengeluaran_delete"),

    # path("pengeluaranDetail/", views.PengeluaranDetailListView.as_view(), name="pengeluaran_detail_list"),
    path("pengeluaranDetail/", views.pengeluaran_detail_list, name="pengeluaran_detail_list"),
    path("pengeluaranDetail/tambah/", views.PengeluaranDetailCreateView.as_view(), name="pengeluaran_detail_create"),
    path("pengeluaranDetail/<str:pengeluaran_id>/tambah/", views.pengeluaran_detail_create, name="pengeluaran_detail_tambah"),
    path("pengeluaranDetail/<str:pengeluaran_id>/tambah2/<str:pengeluaran_detail_id>", views.pengeluaran_detail_create, name="pengeluaran_detail_tambah2"),
    path("pengeluaranDetail/<str:pk>/edit/", views.pengeluaran_detail_update, name="pengeluaran_detail_update"),
    path("pengeluaranDetail/<str:pk>", views.PengeluaranDetailDetailView.as_view(), name="pengeluaran_detail_detail"),
    path("pengeluaranDetail/<str:pk>/hapus/", views.pengeluaran_detail_delete, name="pengeluaran_detail_delete"),

    path("", views.index, name="landing_page"),
]

