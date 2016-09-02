from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# custom a manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', "Draft"),
        ('published', "Published"),
    )
    title = models.CharField(max_length=250)

    # require that this field be unique for the value of
    # the 'publish' date field.
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # The name to use for the relation from the related
    # object back to this one.
    author = models.ForeignKey(User, related_name='blog_posts')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # DateField.auto_now_add
    # Automatically set the field to now when the object is first created.
    created = models.DateTimeField(auto_now_add=True)

    # DateField.auto_now
    # Automatically set the field to now every time the object is saved.
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    # default manager and published manager:
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug
                                                 ])
