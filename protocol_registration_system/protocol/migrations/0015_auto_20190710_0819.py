# Generated by Django 2.2 on 2019-07-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0014_auto_20190709_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]