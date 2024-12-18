# Generated by Django 5.1.4 on 2024-12-18 13:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ganho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ganho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ganho.animal')),
            ],
        ),
    ]
