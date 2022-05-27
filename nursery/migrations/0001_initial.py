# Generated by Django 4.0.1 on 2022-05-25 16:35

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_Img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Main_Img')),
                ('Blog_Name', models.CharField(max_length=150)),
                ('Author', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Plant_Type', models.CharField(choices=[('Low Mantenance Plant', 'Low Mantenance Plant'), ('Indoor Plant', 'Indoor Plant'), ('Flowering Plant', 'Flowering Plant'), ('Outdoor Plant', 'Outdoor Plant'), ('Air Purifier Plant', 'Air Purifier Plant'), ('Harbal Plant', 'Harbal Plant')], max_length=50)),
                ('Small_Info', models.TextField()),
                ('Light', models.CharField(max_length=100)),
                ('Watering', models.CharField(max_length=100)),
                ('Where_To_Grow', models.CharField(max_length=100)),
                ('Maintenance', models.CharField(max_length=100)),
                ('Special_Feature', models.CharField(max_length=100)),
                ('Second_Img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Second_Img')),
                ('Intro', models.TextField()),
                ('Evolution', models.TextField(blank=True)),
                ('Medicine', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=150)),
                ('Mobile', models.CharField(max_length=20)),
                ('Message', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Product_Img')),
                ('Product_Name', models.CharField(max_length=150)),
                ('Plant_Type', models.CharField(choices=[('Low Mantenance Plant', 'Low Mantenance Plant'), ('Indoor Plant', 'Indoor Plant'), ('Flowering Plant', 'Flowering Plant'), ('Outdoor Plant', 'Outdoor Plant'), ('Air Purifier Plant', 'Air Purifier Plant'), ('Harbal Plant', 'Harbal Plant')], max_length=50)),
                ('Real_Price', models.CharField(max_length=100)),
                ('Discount_Price', models.CharField(blank=True, max_length=100)),
                ('Description', models.TextField()),
                ('Light', models.CharField(max_length=100)),
                ('Watering', models.CharField(max_length=100)),
                ('Where_To_Grow', models.CharField(max_length=100)),
                ('Maintenance', models.CharField(max_length=100)),
                ('Special_Feature', models.CharField(max_length=100)),
                ('Second_Img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Second_Img')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('Profile_Pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Profile_Pic')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=70)),
                ('Date', models.DateField(auto_now=True)),
                ('Gender', models.CharField(choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(max_length=20)),
                ('Facebook', models.URLField(blank=True, max_length=300)),
                ('Twitter', models.URLField(blank=True, max_length=300)),
                ('Instagram', models.URLField(blank=True, max_length=300)),
                ('Website', models.URLField(blank=True, max_length=300)),
                ('Pincode', models.CharField(max_length=10)),
                ('Address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Date', models.DateTimeField(auto_now=True)),
                ('Product_Amount', models.IntegerField()),
                ('Product_Quantity', models.IntegerField()),
                ('Deliver', models.BooleanField(default=False)),
                ('Order_Cancel_Position', models.BooleanField(default=False)),
                ('Buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursery.userdetails')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursery.productdetail')),
            ],
        ),
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Amount', models.IntegerField()),
                ('Product_Quantity', models.IntegerField()),
                ('Buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursery.userdetails')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursery.productdetail')),
            ],
        ),
    ]
