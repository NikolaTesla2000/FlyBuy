# Generated by Django 3.0.5 on 2020-06-15 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=200)),
                ('apartment_address', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('save_info', models.BooleanField(default=False)),
                ('use_default', models.BooleanField(default=False)),
                ('default', models.BooleanField(default=False)),
                ('payment_option', models.CharField(choices=[('S', 'Stripe'), ('P', 'Paypal')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
