from django.db import models
from datetime import datetime

# Create your models here.
# from ckeditor.fields import RichTextField
from DjangoUeditor.models import UEditorField

from home.models import UserInfo


class Category(models.Model):
    """
    分类名
    """
    name = models.CharField(max_length=100, verbose_name='分类')

    def __str__(self):
        # 返回类名
        return self.name

    class Meta:
        # 元类
        db_table = "Category"
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Tag"
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    文章模型
    """
    title = models.CharField(max_length=100, verbose_name='标题')

    # 文章简介   blank=True 表示可以不写 没有的话　
    excerpt = models.CharField(max_length=200, null=True, blank=True, verbose_name='简介')

    # 图片上传
    # pic = models.ImageField(upload_to='Article_img/%Y/%m', null=True, blank=True, verbose_name="图片")

    # 富文本
    # content = models.TextField(verbose_name='内容')
    # content = RichTextField(verbose_name="内容")
    # content = UEditorField(verbose_name='内容', width=600, height=300, toolbars="full",
    #                        imagePath="Article_img/%Y/%m/",
    #                        filePath="Article_file/%Y/%m/",
    #                        upload_settings={"imageMaxSize": 1204000},
    #                        settings={}, command=None, blank=True)
    content = UEditorField(verbose_name='内容', height=500, width=1000,
                           default=u'', imagePath="Article_img/",
                           toolbars='full', filePath='Article_file/',
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None,)

    # content = HTMLField(verbose_name='内容')
    # content = MarkdownField(verbose_name='内容')

    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    modified_time = models.DateTimeField(verbose_name='修改时间')  # 修改时间

    # 分类外键
    category = models.ForeignKey(Category, verbose_name='分类')

    # 多对多　文章和标签
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    # 作者 一对多关系一篇文章只有一个作者
    author = models.ForeignKey(UserInfo, verbose_name='作者')

    on_click = models.IntegerField(default=0, verbose_name='点击量')

    comment_num = models.IntegerField(default=0, verbose_name='评论量')

    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.title

    # 元类
    class Meta:
        db_table = "Article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name



if __name__ == '__main__':
    pass
