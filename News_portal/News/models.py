from django.db import models
from django.contrib.auth.models import  User
from django.db.models import Sum

class Author(models.Model):
    authorUser= models.OneToOneField(User, on_delete=models.CASCADE)
    raiting_author = models.SmallIntegerField(default=0)

    def update_raiting(self):
        postRat = self.post_set.aggregate(postRaiting=Sum('raiting'))
        postR= 0
        postR += postRat.get('postRaiting')

        commentRat = self.authorUser.comment_set.aggregate (commentRating= Sum('raiting'))
        cRat = 0
        cRat+=commentRat.get ('commentRating')
        self.raiting_author = postR + cRat
        self.save()

class Category(models.Model:
    name = models.CharField(max_length=64, unique= True)


class Post(models.Model):
    author_post=models.ForeignKey(Author, on_delete= models.CASCADE)
    NEWS='NW'
    ARTICLE='AR'
    CATEGORY_CHOICES = ((NEWS, 'Новость'), (ARTICLE, 'Статья' ),)

    category_postType=models.CharField(max_length=2, choices= CATEGORY_CHOICES, default= ARTICLE)
    postCategory = models.ManyToManyField( Category, through='PostCategory')
    date_post = models.DateTimeField(auto_now_add=True)
    post_tytle = models.CharField(max_length=32)
    post_text = models.TextField()
    raiting = models.SmallIntegerField(default=0)

    def like(sel):
        self.raiting+=1
        self.save

    def dislike(self):
        self.raiting += -1
        self.save

    def preview(self)
        return self.post_text[0:123]+'...'

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    pass

class Comment(models.Model):
    comment_Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=256)
    comment_date=models.DateTimeField(auto_now_add=True)
    raiting = models.SmallIntegerField(default=0)

    def like(sel):
        self.raiting += 1
        self.save

    def dislike(self):
        self.raiting += -1
        self.save

    pass