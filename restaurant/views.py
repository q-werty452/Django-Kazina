from django.shortcuts import render
from .models import Category, Hall, GalleryImage, SliderSlide, SiteSettings, MenuItem


def get_common_context():
    site = SiteSettings.objects.first()
    categories = Category.objects.prefetch_related('items').all()
    return {
        'categories': categories,
        'halls': Hall.objects.all(),
        'gallery': GalleryImage.objects.all(),
        'gallery_top': GalleryImage.objects.filter(row='top'),
        'gallery_bottom': GalleryImage.objects.filter(row='bottom'),
        'slides': SliderSlide.objects.filter(is_active=True),
        'week_specials': MenuItem.objects.filter(is_week_special=True, is_active=True)[:8],
        'site': site,
    }


def index(request):
    return render(request, 'index.html', get_common_context())


def qr_menu(request):
    return render(request, 'qr_menu.html', get_common_context())
