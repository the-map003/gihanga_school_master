# Generated by Django 5.0.4 on 2024-04-23 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result_report_management.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management.student')),
            ],
        ),
    ]
