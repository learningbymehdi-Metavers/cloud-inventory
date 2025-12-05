from django.urls import path
from .views import export_stock_csv
from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Inventory app is running. Try /export/ or /admin/")

urlpatterns = [
    path("", home, name="home"),
    path("export/", export_stock_csv, name="export_stock_csv"),
]
