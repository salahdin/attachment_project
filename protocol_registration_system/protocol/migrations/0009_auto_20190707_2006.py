# Generated by Django 2.2 on 2019-07-07 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0008_auto_20190707_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolrequest',
            name='response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='protocol.ProtocolResponse'),
        ),
    ]