#...
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import render,redirect
#from .models import Product, Order, LineItem


def checkout(request):
    if request.method == 'POST':
        return redirect('process_payment')
 
    else:
        return render(request, 'payments/checkout.html')
 
def process_payment(request):
    host = request.get_host()
 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '105',
        'item_name': 'testProduct',
        'invoice': '112',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }
 
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payments/payment.html', {'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'payments/payment_done.html')
 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payments/payment_cancelled.html')