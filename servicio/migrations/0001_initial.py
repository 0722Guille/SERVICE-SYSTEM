# Generated by Django 5.1 on 2024-09-04 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('codigoServices', models.AutoField(primary_key=True, serialize=False)),
                ('nameServices', models.CharField(max_length=255)),
                ('descriptionServices', models.CharField(max_length=255)),
                ('gmailServicesgmail', models.CharField(max_length=255)),
                ('princeServices', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
