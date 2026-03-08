from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, MenuItem, Hall, GalleryImage, SliderSlide, SiteSettings


class MenuItemInline(TabularInline):
    model = MenuItem
    extra = 0
    fields = ('name', 'price', 'tag', 'is_week_special', 'is_active', 'order')


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ('name', 'category', 'price', 'tag', 'is_week_special', 'is_active', 'order')
    list_filter = ('category', 'tag', 'is_week_special', 'is_active')
    list_editable = ('price', 'is_week_special', 'is_active', 'order')
    search_fields = ('name', 'description')
    fieldsets = (
        ('Основное', {
            'fields': ('category', 'name', 'description', 'price', 'image'),
        }),
        ('Параметры', {
            'fields': ('tag', 'is_week_special', 'is_active', 'order'),
        }),
    )


@admin.register(Hall)
class HallAdmin(ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ('alt', 'order')
    list_editable = ('order',)


@admin.register(SliderSlide)
class SliderSlideAdmin(ModelAdmin):
    list_display = ('title', 'btn_text', 'is_active', 'order')
    list_editable = ('is_active', 'order')


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    fieldsets = (
        ('Контакты', {
            'fields': ('phone', 'phone_link', 'whatsapp', 'address', 'hours'),
        }),
        ('Социальные сети', {
            'fields': ('instagram_url', 'facebook_url'),
        }),
        ('Контент', {
            'fields': ('about_text', 'map_embed'),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
