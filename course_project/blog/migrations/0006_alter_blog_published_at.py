# Generated by Django 4.2 on 2023-05-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
