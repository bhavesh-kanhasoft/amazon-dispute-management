# Generated by Django 5.0.1 on 2024-01-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispute',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Pending', 'Pending'), ('Close', 'Close')], default='Open', max_length=50),
        ),
    ]
