from django.shortcuts import render, get_object_or_404
from orders.models import Order

# Create your views here.

def index(request):

    orders = Order.objects.all()
    tr_class_succes = "table-success"
    tr_class_default = "table-info"

    # this is your new view and passing variable
    return render(request, 'index.html', {
        'orders': orders, 
        'tr_class_succes': tr_class_succes,
        'tr_class_default': tr_class_default,
        })
        
def order_detail(request, slugm):
    thing = get_object_or_404(Order, slug=slugm)
#    Order.objects.get(slug=slugm)

    return render(request, 'order/order_detail.html',
        {'thing': thing, }
        )
        
def order_edit(request):
#    thing2 = Order.objects.get(slug=slugm)

    return render(request, 'order/edit_order.html',
#        {'thing2': thing2, }
        )