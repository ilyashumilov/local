# Generated by Django 3.2.8 on 2022-01-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0004_auto_20220119_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='ETA',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='ETD',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='equip',
            field=models.TextField(max_length=200),
        ),
    ]