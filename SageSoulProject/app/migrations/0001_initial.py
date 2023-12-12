# Generated by Django 5.0 on 2023-12-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herb', models.CharField(max_length=100)),
                ('name', models.TextField()),
                ('hindi_name', models.TextField()),
                ('english_name', models.TextField()),
                ('properties_rasa', models.TextField()),
                ('properties_guna', models.TextField()),
                ('properties_virya', models.TextField()),
                ('properties_vipaka', models.TextField()),
                ('effects_on_dosa', models.TextField()),
                ('caution', models.TextField()),
            ],
        ),
    ]
