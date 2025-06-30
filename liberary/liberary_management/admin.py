from django.contrib import admin

# Register your models here.
class FineAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount', 'paid')
    list_filter = ('paid',)
    search_fields = ('loan__member__name', 'loan__book__title')