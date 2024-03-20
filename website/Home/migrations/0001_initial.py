# Generated by Django 5.0.2 on 2024-03-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
