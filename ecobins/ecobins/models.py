from django.db import models
from autho import models as autho

# Transactions Table
class Transactions(models.Model):
    OrderId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    Invoice = models.CharField(max_length=255)
    Status = models.CharField(max_length=20, choices=[('Received', 'Received'), ('Delivered', 'Delivered'), ('Transit', 'Transit'), ('Paid', 'Paid')])

# Content Creator Module
class Post(models.Model):
    PostID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    Content = models.ImageField(upload_to='posts/')
    Caption = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    FollowID = models.AutoField(primary_key=True)
    FollowerID = models.ForeignKey(autho.User, related_name='follower', on_delete=models.CASCADE)
    FollowingID = models.ForeignKey(autho.User, related_name='following', on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now_add=True)

class Notifications(models.Model):
    NotificationId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    NotificationType = models.CharField(max_length=255)
    Notification = models.TextField()
    TimeStamp = models.DateTimeField(auto_now_add=True)

# Marketplace Module
class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    CartID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=10, choices=[('Hold', 'Hold'), ('Bought', 'Bought')])

# Waste Disposal Service Provider Module
class WasteDisposalProvider(models.Model):
    ProviderID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    BusinessName = models.CharField(max_length=255)
    Address = models.TextField()
    ServicesOffered = models.TextField()
    ContactInformation = models.CharField(max_length=255)

class Booking(models.Model):
    BookingID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    ProviderID = models.ForeignKey(WasteDisposalProvider, on_delete=models.CASCADE)
    Details = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)

# Basic Module
class Profile(models.Model):
    UserID = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    Role = models.CharField(max_length=25, choices=[('content_creator', 'Content Creator'), ('customer', 'Customer'), ('waste_disposal_provider', 'Waste Disposal Provider')])
    Address = models.TextField()
    ProfilePic = models.ImageField(upload_to='profile_pics/')

class Settings(models.Model):
    UserId = models.ForeignKey(autho.User, on_delete=models.CASCADE)
    Setting1 = models.CharField(max_length=255)
    Setting2 = models.CharField(max_length=255)
    # Add more fields as needed
