from django.contrib import admin

from data.models import (
    DeliveriesGlobalByQuarter,
    InformationSource,
    StockPrice,
)


class AllFieldsModelAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(DeliveriesGlobalByQuarter)
class DeliveriesGlobalByQuarterAdmin(AllFieldsModelAdmin):
    pass


@admin.register(InformationSource)
class InformationSourceAdmin(AllFieldsModelAdmin):
    pass


@admin.register(StockPrice)
class StockPriceAdmin(AllFieldsModelAdmin):
    pass
