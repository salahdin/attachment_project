# Generated by Django 2.2 on 2019-07-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0019_auto_20190710_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='protocol.ProtocolResponse'),
        ),
    ]