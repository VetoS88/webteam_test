from django.db import models
from django.utils import timezone


class UniqueSlug(models.SlugField):
    def pre_save(self, model_instance, add):
        if add:
            last = Categories.objects.last()
            last_pk = last.pk if last else 0
            slug = 'n{n}d{d}id{pk}'.format(n=model_instance.name,
                                           d=timezone.now().strftime('%d%m%Y'),
                                           pk=last_pk + 1)
            setattr(model_instance, self.attname, slug)
            return slug
        else:
            slug = 'n{n}d{d}id{pk}'.format(n=model_instance.name,
                                           d=timezone.now().strftime('%d%m%Y'),
                                           pk=model_instance.pk)
            setattr(model_instance, self.attname, slug)
            return slug


class Categories(models.Model):
    name = models.CharField('Название', max_length=200)
    h1 = models.CharField('H1', max_length=200, blank=True, null=True)
    slug = UniqueSlug('Адрес в url', max_length=200)

    def __str__(self):
        return self.slug


class Articles(models.Model):
    name = models.CharField('Название', max_length=200)
    h1 = models.CharField('H1', max_length=200, blank=True, null=True)
    slug = models.SlugField('Адрес в url', max_length=200)
    img = models.ImageField(upload_to='articles/', blank=True)
    text = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(Categories, verbose_name='Категория')
