# Generated by Django 5.0.4 on 2024-04-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='contact2',
            new_name='role',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='email',
        ),
    ]
