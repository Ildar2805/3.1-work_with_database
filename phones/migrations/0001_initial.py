# Generated by Django 3.1.2 on 2022-08-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('image', models.URLField(max_length=300)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
