# Generated by Django 5.1.4 on 2024-12-07 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grades', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='school.student'),
        ),
        migrations.AddField(
            model_name='homework',
            name='school_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='school.class'),
        ),
    ]
