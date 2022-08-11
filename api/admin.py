from django.contrib import admin
from .models import Account, Destination, Headers
# Register your models here.


# class AccountAdmin(admin.ModelAdmin):
# readonly_fields = ['account_id', 'account_name', 'app_secret_token']


admin.site.register(Account)
admin.site.register(Destination)
admin.site.register(Headers)
