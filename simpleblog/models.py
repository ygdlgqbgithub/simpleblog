#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(u'分类名',max_length=30,unique=True)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'

    @models.permalink
    def get_absolute_url(self):
        return ('simpleblog_category',None,{
            'category_id':self.id
        })

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title   = models.CharField(u'文章标题',max_length=50)
    content = models.TextField(u'文章内容')

    author  = models.ForeignKey(User,verbose_name=u'作者',related_name='add_articles')
    category= models.ForeignKey(Category,verbose_name=u'分类',related_name='articles',
                                blank=True,null=True,on_delete=models.SET_NULL
                                )

    STATUS_CHOICES = ((1,u'发布'),(0,u'草稿'))
    status        = models.SmallIntegerField(u'状态',choices=STATUS_CHOICES,default=1)

    created_at = models.DateTimeField(u'创建于',auto_now_add=True)
    publish_at = models.DateTimeField(u'发布于')
    update_at  = models.DateTimeField(u'更新于',auto_now=True)
    
    num_views  = models.IntegerField(u'浏览次数',default=0)

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
        ordering = ['-publish_at']

    @models.permalink
    def get_absolute_url(self):
        return ('simpleblog_article',None,{
            'year':self.publish_at.year,
            'month':self.publish_at.month,
            'article_id':self.id
        })

    def __unicode__(self):
        return self.title
