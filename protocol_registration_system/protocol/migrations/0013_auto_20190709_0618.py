# Generated by Django 2.2 on 2019-07-09 06:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0012_auto_20190708_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocolresponse',
            name='response',
        ),
        migrations.AddField(
            model_name='protocol',
            name='response',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='protocol.ProtocolResponse'),
        ),
        migrations.AddField(
            model_name='protocolresponse',
            name='protocolrequest',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='protocol.ProtocolRequest'),
        ),
        migrations.AddField(
            model_name='protocolresponse',
            name='response_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date of response'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='protocolrequest',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='protocolrequest',
            name='pi_email',
            field=models.EmailField(max_length=200, verbose_name='PI email'),
        ),
    ]
