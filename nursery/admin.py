from django.contrib import admin
from nursery.models import ContactUs,UserDetails,ProductDetail,AddToCart,Order,Blogs

# Register your models here.
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['User','Name','Profile_Pic','Email','Mobile','Pincode','Address']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['Full_Name','Email','Mobile','Message']

@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['Product_Name','Real_Price','Plant_Type','Where_To_Grow']

@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display = ['Buyer','Product','Product_Quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['Buyer','Deliver','Product','Order_Date','showAddress','Order_Cancel_Position']

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display= ['Blog_Name','Author','Plant_Type','Date']