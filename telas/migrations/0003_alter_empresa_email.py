# Generated by Django 5.0.6 on 2024-06-08 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas', '0002_alter_empresa_cnae_principal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
