# Generated by Django 5.1.1 on 2024-10-04 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreDocs', '0004_alter_basedocs_tipo_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='basedocs',
            name='FIN_VIGENCIA',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='basedocs',
            name='INICIO_VIGENCIA',
            field=models.DateField(blank=True, null=True),
        ),
    ]
