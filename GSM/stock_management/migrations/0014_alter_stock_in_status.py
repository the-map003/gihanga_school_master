# Generated by Django 5.0.4 on 2024-05-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0013_alter_supplier_contact1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_in',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
