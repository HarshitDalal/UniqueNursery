# Generated by Django 4.0.1 on 2022-05-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Plant_Type',
            field=models.CharField(choices=[('Indoor Plant', 'Indoor Plant'), ('Air Purifier Plant', 'Air Purifier Plant'), ('Low Mantenance Plant', 'Low Mantenance Plant'), ('Flowering Plant', 'Flowering Plant'), ('Harbal Plant', 'Harbal Plant'), ('Outdoor Plant', 'Outdoor Plant')], max_length=50),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='Plant_Type',
            field=models.CharField(choices=[('Indoor Plant', 'Indoor Plant'), ('Air Purifier Plant', 'Air Purifier Plant'), ('Low Mantenance Plant', 'Low Mantenance Plant'), ('Flowering Plant', 'Flowering Plant'), ('Harbal Plant', 'Harbal Plant'), ('Outdoor Plant', 'Outdoor Plant')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=50),
        ),
    ]
