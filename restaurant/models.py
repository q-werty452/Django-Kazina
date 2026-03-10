from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL-имя")
    icon = models.CharField(max_length=10, blank=True, verbose_name="Иконка (emoji)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Категория меню"
        verbose_name_plural = "Категории меню"
        ordering = ['order']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    TAG_CHOICES = [
        ('', '—'),
        ('top', 'ТОП ВКУС'),
        ('new', 'НОВИНКА'),
        ('fire', 'НА ОГНЕ'),
        ('tea', 'К ЧАЮ'),
        ('fresh', 'СВЕЖЕЕ'),
        ('special', 'ОСОБОЕ'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название блюда")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Цена (сом)")
    image = models.ImageField(upload_to='menu/', verbose_name="Фото")
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, blank=True, verbose_name="Бейдж")
    is_week_special = models.BooleanField(default=False, verbose_name="Блюдо недели?")
    is_active = models.BooleanField(default=True, verbose_name="Активно?")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ['order']

    def __str__(self):
        return f"{self.name} — {self.category}"


class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название зала")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='halls/', verbose_name="Фото зала (карточка)")
    bg_image = models.ImageField(upload_to='halls/bg/', blank=True, null=True,
        verbose_name="Фото фона (при наведении)",
        help_text="Широкоформатное фото для фона секции. Если не задано — используется фото карточки.")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Зал / Атмосфера"
        verbose_name_plural = "Залы / Атмосфера"
        ordering = ['order']

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    ROW_CHOICES = [('top', 'Верхняя строка'), ('bottom', 'Нижняя строка')]

    image = models.ImageField(upload_to='gallery/', verbose_name="Фото")
    alt = models.CharField(max_length=200, blank=True, verbose_name="Подпись")
    row = models.CharField(max_length=10, choices=ROW_CHOICES, default='top', verbose_name="Строка галереи")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "Галерея"
        ordering = ['order']

    def __str__(self):
        return self.alt or f"Фото #{self.pk}"


class SliderSlide(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=200, blank=True, verbose_name="Подзаголовок")
    btn_text = models.CharField(max_length=50, default="Смотреть меню", verbose_name="Текст кнопки")
    btn_link = models.CharField(max_length=100, default="#menu", verbose_name="Ссылка кнопки")
    image = models.ImageField(upload_to='slider/', verbose_name="Фото слайда")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен?")

    class Meta:
        verbose_name = "Слайд баннера"
        verbose_name_plural = "Слайды баннера"
        ordering = ['order']

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    phone = models.CharField(max_length=50, verbose_name="Телефон (текст)", default="+996 555 123 456")
    phone_link = models.CharField(max_length=50, verbose_name="Телефон (для ссылки tel:)", default="996555123456")
    whatsapp = models.CharField(max_length=50, verbose_name="WhatsApp (только цифры)", default="996555123456")
    address = models.CharField(max_length=200, verbose_name="Адрес", default="г. Бишкек, ул. Манаса, 12")
    hours = models.CharField(max_length=100, verbose_name="Режим работы", default="Ежедневно: 10:00 — 00:00")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    about_text = models.TextField(verbose_name="Текст «Философия Казыны»",
        default="Мы не просто готовим еду. Мы воссоздаем историю.")
    hero_image = models.ImageField(upload_to='settings/', blank=True, null=True,
        verbose_name="Фоновое фото (Hero-секция)")
    about_image = models.ImageField(upload_to='settings/', blank=True, null=True,
        verbose_name="Фото секции «Философия» (левый блок)")
    map_embed = models.TextField(blank=True, verbose_name="Ссылка Google Maps (src для iframe)",
        help_text="Вставьте только src из кода встраивания Google Maps")

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
