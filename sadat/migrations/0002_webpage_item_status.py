# Generated by Django 3.0.1 on 2020-02-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='item_status',
            field=models.CharField(max_length=264, null=True),
        ),
    ]