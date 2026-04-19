from celery import shared_task
from django.utils import timezone


@shared_task
def send_product_notification(product_name, product_price):
    print(f"✌️ New product created!")
    print(f"    Name:{product_name}")
    print(f"    Price:{product_price}")
    print(f"    Time:{timezone.now()}")
    return f"Notification sent for {product_name}"
