# Generated by Django 4.1.6 on 2023-02-04 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okpo', models.CharField(max_length=100)),
                ('employees', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('pin', models.IntegerField()),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('cause', models.CharField(max_length=222)),
                ('okpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('pin', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('okpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=222)),
                ('pin', models.IntegerField()),
                ('age', models.IntegerField()),
                ('work', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('okpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Chiefphysician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('pin', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
                ('work', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('okpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
        ),
    ]
