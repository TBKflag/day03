from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    #CharField表示varchar
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()
    #URLField也是varchar，默认200
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'publisher'
        verbose_name='出版社'
        verbose_name_plural=verbose_name

# 声明自定义的ｏｂｊｅｃｔｓ
class AuthorManager(models.Manager):
    def aucount(self):
        countnum = self.filter(age__lt=30)
        return countnum
class Author(models.Model):
    # 使用authorManager 覆盖objects
    objects=AuthorManager()
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name="邮箱")
    isactive = models.BooleanField(default=True,verbose_name='启用')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = '作者'
        ordering = ["age","name"]

class Book(models.Model):
    title=models.CharField(max_length=20)
    publicate_date=models.DateField()
    # 增加对Publisher的引用
    publisher=models.ForeignKey(Publisher,null=True)
    author=models.ManyToManyField(Author)

    def __str__(self):
        return self.title
    class Meta:
        db_table='book'
        verbose_name="书籍"
        verbose_name_plural=verbose_name
        ordering=["-publicate_date"]

class wife(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    author=models.OneToOneField(Author)
    def __str__(self):
        return self.name
    class Meta:
        db_table='wife'
        verbose_name='妻子'
        verbose_name_plural=verbose_name
