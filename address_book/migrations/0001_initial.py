# Generated by Django 3.1.2 on 2020-11-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=40)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]
