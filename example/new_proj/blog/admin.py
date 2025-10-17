from django.contrib import admin
from blog.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "title_len",
        "created_at",
        "updated_at"
    ]

    def title_len(self, obj):
        return len(obj.title)

    actions = ["print_title"]
    def print_title(self, obj, qs):
        for item in qs:
            print(item)

admin.site.register(Blog, BlogAdmin)