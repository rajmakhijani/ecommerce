# Generated by Django 2.1.7 on 2019-03-20 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vender',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='vender', to='vender.Vender'),
        ),
    ]
