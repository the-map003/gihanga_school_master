# Generated by Django 5.0.4 on 2024-05-06 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0015_alter_stock_in_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock_in',
            options={'ordering': ['stocked_at']},
        ),
    ]
