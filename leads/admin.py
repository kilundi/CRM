from django.contrib import admin

# Register your models here.
from .models import Lead, Agent, User, UserProfile,Category

admin.site.register(User)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
