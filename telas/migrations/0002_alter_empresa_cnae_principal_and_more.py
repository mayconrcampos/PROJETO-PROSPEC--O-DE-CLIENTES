# Generated by Django 5.0.6 on 2024-06-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnae_principal',
            field=models.CharField(blank=True, max_length=256, verbose_name='CNAE Principal'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnae_secundario',
            field=models.TextField(blank=True, max_length=1024, verbose_name='CNAE Principal'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fone',
            field=models.CharField(max_length=15, verbose_name='fone'),
        ),
    ]
