# Generated by Django 5.1.1 on 2025-01-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
