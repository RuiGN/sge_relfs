from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Outflow


@receiver(pre_save, sender=Outflow)
def get_product_values(sender, instance, **kwargs):
    if instance.product is not None:
        instance.outflow_cost_price = instance.product.cost_price
        if instance.payment_type == 'À VISTA':
            instance.outflow_selling_price = instance.product.cash_selling_price
        else:
            instance.outflow_selling_price = instance.product.selling_price
    else:
        raise ValueError("O produto associado não pode ser None.")


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()
