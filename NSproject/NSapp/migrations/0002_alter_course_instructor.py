# Generated by Django 4.1.6 on 2023-12-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NSapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Courses', to='NSapp.instructor'),
        ),
    ]
