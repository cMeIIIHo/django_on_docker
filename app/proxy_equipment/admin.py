from .models import *
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

import os

app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))  # название прило из пути


# @admin.register(TailorRequest)
# class TailorRequestAdmin(admin.ModelAdmin):
#     list_display = ['number', 'created_datetime', 'client']
#     search_fields = ['number', 'client__title', 'seller__full_name', 'responsible_tailor__full_name']
#     list_filter = ['status', 'with_payment', 'shop']
#
# @admin.register(OfflineCashboxOrder)
# class OfflineCashboxOrderAdmin(admin.ModelAdmin):
#     list_display = ['user', 'client', 'number', 'guid', 'date', 'order_total']
#     raw_id_fields = ['user', 'client', 'stock', 'organization', 'division', 'card']
#     list_filter = ['user']
#     search_fields = ['user__full_name', 'client__title', 'stock__name', 'organization__name', 'division__name',
#                      'card__barcode', 'card__name', 'guid', 'number', 'comment', 'promocode',
#                      'offlinecashboxorderitemproduct__product__one_c_code',
#                      'offlinecashboxorderitemproduct__product__product_name']
#     inlines = [OfflineCashboxOrderItemInline]


app_models = apps.get_app_config(app_name).get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
