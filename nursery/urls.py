from django.urls import path
from nursery import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('product/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('product/productdetail/<int:myid><str:type>', views.productdetails, name='productdetail'),
    path('blog/readblog/<int:myid><str:type>', views.readblog, name='readblog'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('writeblog/', views.writeblog, name='writeblog'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('order/', views.orders, name='order'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('changepassword/', views.changepassword, name='changepassword'),
]
