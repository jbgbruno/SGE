import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(metrics.get_daily_sales_data()),
        'daily_sales_quantity_data': json.dumps(metrics.get_daily_sales_quantity_data()),
        'graphic_product_category_metrics': json.dumps(metrics.get_graphic_product_category_metrics()),
        'graphic_product_brand_metrics': json.dumps(metrics.get_graphic_product_brand_metrics())
    }
    print(context)
    return render(request, 'home.html', context)
