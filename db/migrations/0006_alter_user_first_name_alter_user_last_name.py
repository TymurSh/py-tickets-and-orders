# Generated by Django 4.0.2 on 2024-09-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_alter_ticket_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]