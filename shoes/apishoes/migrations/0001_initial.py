# Generated by Django 5.1.6 on 2025-02-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chauss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prix', models.FloatField()),
                ('quantite', models.IntegerField()),
                ('image', models.CharField(max_length=25096)),
            ],
        ),
    ]
