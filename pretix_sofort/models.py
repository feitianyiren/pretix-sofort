from django.db import models


class ReferencedSofortTransaction(models.Model):
    reference = models.CharField(max_length=190, db_index=True, unique=True)
    order = models.ForeignKey('pretixbase.Order')
    payment = models.ForeignKey('pretixbase.OrderPayment', null=True, on_delete=models.CASCADE)
