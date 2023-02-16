from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


# Create your models here.
class ContactUs(models.Model):
    Full_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=150)
    Mobile = models.CharField(max_length=20)
    Message = models.TextField(max_length=150)

    def __str__(self):
        return str(self.Full_Name) + ' send mail using ' + str(self.Email)


class UserDetails(models.Model):
    gender = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    }
    Profile_Pic = CloudinaryField('Profile_Pic', folder='nursery/User_Profile_Pics/', use_filename=True,
                                  unique_filename=False)
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Name = models.CharField(max_length=70)
    Date = models.DateField(auto_now=True, )
    Gender = models.CharField(max_length=50, choices=gender)
    Email = models.EmailField(max_length=254)
    Mobile = models.CharField(max_length=20)
    Facebook = models.URLField(max_length=300, blank=True)
    Twitter = models.URLField(max_length=300, blank=True)
    Instagram = models.URLField(max_length=300, blank=True)
    Website = models.URLField(max_length=300, blank=True)
    Pincode = models.CharField(max_length=10)
    Address = models.TextField(blank=True)

    def __str__(self):
        return str(self.User)


class ProductDetail(models.Model):
    planttype = {
        ('Flowering Plant', 'Flowering Plant'),
        ('Harbal Plant', 'Harbal Plant'),
        ('Indoor Plant', 'Indoor Plant'),
        ('Outdoor Plant', 'Outdoor Plant'),
        ('Air Purifier Plant', 'Air Purifier Plant'),
        ('Low Mantenance Plant', 'Low Mantenance Plant')
    }
    Product_Name = models.CharField(max_length=150)
    Plant_Type = models.CharField(max_length=50, choices=planttype)
    Real_Price = models.CharField(max_length=100)
    Discount_Price = models.CharField(max_length=100, blank=True)
    Description = models.TextField()
    Light = models.CharField(max_length=100)
    Watering = models.CharField(max_length=100)
    Where_To_Grow = models.CharField(max_length=100)
    Maintenance = models.CharField(max_length=100)
    Special_Feature = models.CharField(max_length=100)
    Product_Img = CloudinaryField('Product_Img', folder='nursery/Product_Images/', use_filename=True,
                                  unique_filename=False)
    Second_Img = CloudinaryField('Second_Img', folder='nursery/Product_Second_Image/', use_filename=True,
                                 unique_filename=False)

    def __str__(self):
        return str(self.Product_Name)


class Blogs(models.Model):
    planttype = {
        ('Flowering Plant', 'Flowering Plant'),
        ('Harbal Plant', 'Harbal Plant'),
        ('Indoor Plant', 'Indoor Plant'),
        ('Outdoor Plant', 'Outdoor Plant'),
        ('Air Purifier Plant', 'Air Purifier Plant'),
        ('Low Mantenance Plant', 'Low Mantenance Plant')
    }
    Blog_Name = models.CharField(max_length=150)
    Author = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now=True)
    Plant_Type = models.CharField(max_length=50, choices=planttype)
    Small_Info = models.TextField()
    Light = models.CharField(max_length=100)
    Watering = models.CharField(max_length=100)
    Where_To_Grow = models.CharField(max_length=100)
    Maintenance = models.CharField(max_length=100)
    Special_Feature = models.CharField(max_length=100)
    Main_Img = CloudinaryField('Main_Img', folder='nursery/Blog_Images/', use_filename=True, unique_filename=False)
    Second_Img = CloudinaryField('Second_Img', folder='nursery/Blog_Second_Image/', use_filename=True,
                                 unique_filename=False)
    Plant_Essentials = RichTextField(blank=True, null=True)
    Common_Problems = RichTextField(blank=True, null=True)
    Style_and_Decor = RichTextField(blank=True, null=True)

    def __str__(self):
        detail = f'{self.Blog_Name} wrote by {self.Author}'
        return str(detail)


class AddToCart(models.Model):
    Buyer = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    Product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    Product_Amount = models.IntegerField()
    Product_Quantity = models.IntegerField()

    def __str__(self):
        order = f'{str(self.Buyer)} Add To Cart {str(self.Product)}'
        return order


class Order(models.Model):
    Buyer = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    Product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    Order_Date = models.DateTimeField(auto_now=True)
    Product_Amount = models.IntegerField()
    Product_Quantity = models.IntegerField()
    Deliver = models.BooleanField(default=False)
    Order_Cancel_Position = models.BooleanField(default=False)

    def __str__(self):
        order = f'{str(self.Buyer)} Buy {str(self.Product)}'
        return order

    @property
    def showAddress(self):
        full_address = f'Address - {self.Buyer.Address} \nPincode - {self.Buyer.Pincode}'
        return full_address
