# Generated by Django 5.0.2 on 2024-03-04 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_category_lead_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
