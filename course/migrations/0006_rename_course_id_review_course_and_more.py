# Generated by Django 4.2 on 2023-05-06 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_studentcourses_studentcourse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='student_id',
            new_name='student',
        ),
    ]