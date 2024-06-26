# Generated by Django 5.0.4 on 2024-04-24 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='pnotice',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='registered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_reg', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('Teacher_id', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teach_class', to='student_management.class')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_reg', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
        migrations.DeleteModel(
            name='Pnotice',
        ),
    ]
