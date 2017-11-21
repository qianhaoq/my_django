from django.db import models
from DjangoUeditor.models import UEditorField

class Article(models.Model):
    # 文章标题
    title = models.CharField("博客标题", max_length = 100)
    # 标签
    category = models.CharField("博客标签", max_length = 50, blank = True)
    # 发布日期
    pub_date = models.DateTimeField("发布日期", auto_now_add = True, editable = True)
    # 更新时间
    update_time = models.DateTimeField("更新日期", auto_now = True, null = True)
    # 博客内容
    #content = models.TextField(blank = True, null = True)
    content = UEditorField("文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",
                            toolbars='besttome',filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"

# Create your models here.
