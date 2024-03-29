# Generated by Django 5.0.2 on 2024-02-10 22:48

import core.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='descricao',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_name, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
    ]
