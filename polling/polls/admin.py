from django.contrib import admin
from polling.polls.models import Poll, Category


class PollAdmin(admin.ModelAdmin):
    
    list_display = ["title", "is_public", "created_at", "creator"]
    fields = ["title", "body", "is_public", "category", "creator"]


class CategoryAdmin(admin.ModelAdmin):

    list_display = ["name"]


admin.site.register(Poll, PollAdmin)
admin.site.register(Category, CategoryAdmin)
