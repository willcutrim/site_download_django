# Generated by Django 3.2 on 2021-04-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteconversor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]