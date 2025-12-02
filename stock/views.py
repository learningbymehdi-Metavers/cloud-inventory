from django.http import HttpResponse
import csv
from .models import Product

def export_stock_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="stock_report.csv"'

    writer = csv.writer(response)
    writer.writerow(["SKU", "Name", "Supplier", "Unit Price", "Quantity"])

    for p in Product.objects.select_related("supplier").all().order_by("sku"):
        writer.writerow([p.sku, p.name, p.supplier.name, str(p.unit_price), p.quantity])

    return response
