# Generated by Django 4.2.1 on 2023-05-31 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myacount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activ',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
    ]
