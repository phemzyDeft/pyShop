# Generated by Django 4.0.4 on 2022-04-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('num_pages', models.IntegerField(default=0)),
                ('isbn13', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
