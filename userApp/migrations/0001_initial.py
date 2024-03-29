# Generated by Django 2.2.3 on 2019-07-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houseinfo',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('housename', models.CharField(blank=True, max_length=50, null=True)),
                ('houseadd', models.CharField(blank=True, max_length=20, null=True)),
                ('addname', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('housetype', models.CharField(blank=True, max_length=20, null=True)),
                ('housearea', models.FloatField(blank=True, null=True)),
                ('housebound', models.CharField(blank=True, max_length=50, null=True)),
                ('housefloor', models.CharField(blank=True, max_length=20, null=True)),
                ('pricerange', models.CharField(blank=True, max_length=20, null=True)),
                ('arearange', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'houseinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('userpassword', models.CharField(blank=True, max_length=20, null=True)),
                ('usertelephone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'userinfo',
                'managed': False,
            },
        ),
    ]
