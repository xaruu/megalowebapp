# Generated by Django 2.1.10 on 2019-07-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=2000)),
                ('video_url', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Episodio',
                'verbose_name_plural': 'Episodios',
            },
        ),
    ]
