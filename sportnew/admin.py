from django.contrib import admin
from .models import SportNew, SportNewImage, Category
# Register your models here.

class SportNewImageInline(admin.TabularInline):
    model = SportNewImage
    extra = 0
class SportNewAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer','created_at', 'updated_at')

    inlines = [
        SportNewImageInline,
    ]
    class Meta:
        model = SportNew

admin.site.register(SportNew, SportNewAdmin)
admin.site.register(Category)
