# Generated by Django 3.0.6 on 2020-12-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouse', '0003_lighthouse_scheduled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lighthouse_result',
            name='result',
            field=models.TextField(max_length=10),
        ),
    ]
