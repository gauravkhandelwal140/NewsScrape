# Generated by Django 3.2.6 on 2021-09-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapenews',
            name='description',
            field=models.TextField(),
        ),
    ]