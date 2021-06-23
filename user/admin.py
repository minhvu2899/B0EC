from django.contrib import admin
from user.models import Address, Comment, CreditCard, CustomerUser, Response, RewardPoints,Wishlist
# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(Wishlist)
admin.site.register(CreditCard)
admin.site.register(Response)
admin.site.register(RewardPoints)