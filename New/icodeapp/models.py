from django.db import models
from django.utils import timezone

from django.shortcuts import reverse



class Category(models.Model):
    title= models.CharField('title',max_length=255,db_index=True)
    slug = models.SlugField('slug', max_length=20, unique=True)
    
    


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField("title", max_length=255,db_index=True)
    slug = models.SlugField('slug', max_length=20, unique=True)
    description = models.TextField('comment', blank=True,db_index=True)
    image = models.ImageField('image',db_index=True)
    date = models.DateTimeField("date_pub",default=timezone.now)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,null=True,related_name = 'categories')
    popular = models.IntegerField('popular', default = 1)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True,related_name='comments')
    author_name = models.CharField('author_name', max_length = 50)
    comment_text = models.TextField('comment', max_length=1000)

    def __str__(self):
        return ' USER:' +  self.author_name + '-- ' +   self.comment_text

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

