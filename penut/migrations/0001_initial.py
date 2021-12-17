# Generated by Django 3.2.9 on 2021-11-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HumanStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=26)),
                ('First_name', models.CharField(max_length=22)),
                ('Last_name', models.CharField(max_length=22)),
                ('DOB', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TokenStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=26)),
                ('hash', models.CharField(max_length=64)),
                ('privatekey', models.BinaryField()),
                ('QR', models.BinaryField()),
                ('Qr_Issued', models.BooleanField()),
            ],
        ),
    ]
