# Generated by Django 4.0.2 on 2024-09-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_alter_ticket_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
