from django.db.models import TextField, IntegerField, Model, TextChoices, CharField, ForeignKey, CASCADE
from .information_source import InformationSource
YEARS = " ".join(map(str, range(2010, 2022)))  # 2010-2021


class DeliveriesGlobalByQuarter(Model):
    class Meta:
        db_table = "deliveries__global_by_quarter"
        unique_together = ('year', 'quarter', 'models')
        ordering = ('year', 'quarter', 'models')

    year = CharField(max_length=4, choices=TextChoices('year', YEARS).choices)
    quarter = CharField(max_length=2, choices=TextChoices('quarter', 'Q1 Q2 Q3 Q4').choices)
    models = TextField()
    units = IntegerField()
    information_source = ForeignKey(InformationSource, null=True, default=None, on_delete=CASCADE)
    notes = TextField(null=True, default=None, blank=True)
