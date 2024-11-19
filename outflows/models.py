from django.db import models
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    outflow_cost_price = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="Preço de Custo")
    outflow_selling_price = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Preço de Venda')
    payment_type = models.TextField(null=False, blank=False, verbose_name='Pagamento')

    def __str__(self):
        return str(self.product)
