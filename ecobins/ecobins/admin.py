from django.contrib import admin
from .models import Product, Follow, Notifications, Post, Cart, Profile, Settings, Transactions, WasteDisposalProvider, Booking

admin.site.register(Product)
admin.site.register(Follow)
admin.site.register(Notifications)
admin.site.register(Post)
admin.site.register(Cart)
admin.site.register(Profile)
admin.site.register(Settings)
admin.site.register(Transactions)
admin.site.register(WasteDisposalProvider)
admin.site.register(Booking)
