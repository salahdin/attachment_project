# Generated by Django 2.2 on 2019-07-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0004_auto_20190707_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocolrequest',
            name='pq',
        ),
        migrations.AddField(
            model_name='protocolrequest',
            name='response',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='protocol.ProtocolResponse'),
            preserve_default=False,
        ),
    ]