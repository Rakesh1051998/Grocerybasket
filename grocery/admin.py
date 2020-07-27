from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from grocery.models import Detail
from grocery.models import FeedbackForm
from grocery.models import MessageForm
from grocery.models import cart


# Register your models here.


class DetailAdmin(ModelAdmin):
    list_display = ["product_name", "type", "brand", "price", "quantity", "units"]
    search_fields = ["product", "brand"]
    list_filter = ["brand", "price"]


admin.site.register(Detail, DetailAdmin)


class MessageFormAdmin(ModelAdmin):
    list_display = ["Name", "Email_id", "Contact_no", "Message", "Date"]
    search_fields = ["Name"]
    list_filter = ["Date"]


admin.site.register(MessageForm, MessageFormAdmin)


class FeedbackFormAdmin(ModelAdmin):
    list_display = ["Name", "Email_id", "Contact_no", "Comment", "Date"]
    search_fields = ["Name"]
    list_filter = ["Date"]


admin.site.register(FeedbackForm, FeedbackFormAdmin)


class cartAdmin(ModelAdmin):
    list_display = ["product_name", "type", "brand", "price", "quantity", "units"]
    search_fields = ["product", "brand"]
    list_filter = ["brand", "price"]


admin.site.register(cart, cartAdmin)
