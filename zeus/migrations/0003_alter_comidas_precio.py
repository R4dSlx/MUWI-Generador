# Generated by Django 4.0.6 on 2022-07-14 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeus', '0002_alter_comidas_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidas',
            name='precio',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
