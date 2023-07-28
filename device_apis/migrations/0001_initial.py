# Generated by Django 4.2.3 on 2023-07-27 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('LAPTOP', 'Laptop'), ('MOBILE', 'Mobile'), ('Tablet', 'Tablet')], default='MOBILE', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ram', models.CharField(max_length=50)),
                ('internal_storage', models.CharField(max_length=50)),
                ('battery', models.CharField(max_length=50)),
                ('camera', models.CharField(max_length=50)),
                ('processor', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_at', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_apis.devices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
