# Generated by Django 2.2 on 2019-07-06 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='protocol name')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='protocol description')),
                ('pi_email', models.CharField(max_length=200, verbose_name='PI email')),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], max_length=50, verbose_name='protocol status')),
                ('number', models.IntegerField(blank=True, verbose_name='assigned protocol number')),
                ('pq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='protocol.ProtocolRequest')),
            ],
        ),
        migrations.DeleteModel(
            name='Protocol',
        ),
    ]