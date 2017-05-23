## Тестовое задание
 Есть 2 модели (Блог)


        class Categories(models.Model):
            name = models.CharField('Название', max_length=200)
            h1 = models.CharField('H1', max_length=200, blank=True, null=True)
            slug = models.SlugField('Адрес в url', max_length=200)


        class Articles(models.Model):
            name = models.CharField('Название', max_length=200)
            h1 = models.CharField('H1', max_length=200, blank=True, null=True)
            slug = models.SlugField('Адрес в url', max_length=200)
            img = models.ImageField(upload_to='articles/', blank=True)
            text = models.TextField('Описание', blank=True, null=True)
            category = models.ForeignKey(Categories, verbose_name='Категория')

#### Требуется:
- написать автогенерацию уникального slug для категории
- написать view для вывода списка статей категории
- написать адаптивный (на бутстрапе) псевдошаблон
- предложить, что еще можно внедрить или улучшить в данном псевдокоде для пользователей и для проекта в целом (словами)

Что нужно вывести:
<header>Шапка</header><div class=`container`>
Картинка
Заголовок (ссылка)
Короткое описание (200 символов)
</div><footer>Футер</footer>

#### Пояснительная записка.
- автогенерация поля slug для категории находиться в файле webteam_test/webteam/models.py.
- view для вывода списка статей категории находится в фале webteam_test/webteam/views.py