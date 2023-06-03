# Generated by Django 4.2 on 2023-05-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='ad soyad')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('message', models.TextField(verbose_name='mətn')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='telefon')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
            ],
            options={
                'verbose_name': 'Müraciət',
                'verbose_name_plural': 'Müraciətlər',
            },
        ),
    ]