# Generated by Django 3.1.7 on 2021-03-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20210316_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tagName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
