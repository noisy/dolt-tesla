# Generated by Django 3.1.7 on 2021-04-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockprice',
            name='adj_close',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='stockprice',
            name='high',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='stockprice',
            name='low',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]