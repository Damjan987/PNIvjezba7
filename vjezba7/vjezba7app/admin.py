from django.contrib import admin
from vjezba7app.models import Projection, Card, UserProfileInfo
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Projection)
admin.site.register(Card)