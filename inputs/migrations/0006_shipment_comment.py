# Generated by Django 3.2.8 on 2022-01-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0005_auto_20220125_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='comment',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
