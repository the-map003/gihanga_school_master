# Generated by Django 5.0.4 on 2024-04-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0005_course_assignment_discussionthread_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
