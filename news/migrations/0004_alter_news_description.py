# Generated by Django 3.2.6 on 2021-09-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_scrapenews_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(),
        ),
    ]