# Generated by Django 2.1.7 on 2019-03-22 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0002_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
