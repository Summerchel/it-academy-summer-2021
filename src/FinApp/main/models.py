from django.db import models
from datetime import date

from django.urls import reverse


class InputField(models.Model):
    """Class for spends"""
    title = models.CharField('title', max_length=70)
    amount = models.DecimalField("Amount", max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=False, auto_now=False, default=date.today())
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Spend'
        verbose_name_plural = 'Spends'


class Category(models.Model):
    """Category's in spends"""
    name = models.CharField(max_length=70, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

