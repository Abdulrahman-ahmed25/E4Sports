from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class SportNewQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

class SportNewManager(models.Manager):
    def get_queryset(self):
        return SportNewQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    # def get_related(self, instance):
    #     products_one = self.get_queryset().filter(category__in=instance.category.all())
    #     products_two = self.get_queryset().filter(default=instance.default)
    #     qs = (products_one | products_two).exclude(id = instance.id).distinct()
    #     return qs

class SportNew(models.Model):
    title = models.CharField(max_length=400, null=False, blank=False)
    writer = models.CharField(max_length=120, null=False, blank=False)
    details = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    active = models.BooleanField(default=True)

    #category and default
    category = models.ManyToManyField('Category', blank=True)
    default  = models.ForeignKey('Category',on_delete=models.CASCADE, related_name='default_category', null=True, blank=True)

    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return reverse("sportnew:news_detail", kwargs = {"pk": self.pk})

        #for getting image from db
    def get_image_url(self):
        img = self.sportnewimage_set.first()
        if img:
            return img.image.url
        return img #None
        
def image_upload_to(instance, filename):
    title = instance.sportnew.title[:10]
    slug  = slugify(title)
    file_extension = filename.split(".")
    # new_filename = "%s-%s.%s" %(slug, instance.id, file_extension) = 
    new_filename = f'{slug}-{instance.id}.{file_extension}' 
    return f'SportNew/{slug}/{new_filename}'

class SportNewImage(models.Model):
    sportnew = models.ForeignKey(SportNew, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to = image_upload_to)

    def __str__(self):
        return self.sportnew.title


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug  = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    time_published = models.DateTimeField(auto_now_add=True, auto_now=False)


    image =  models.ImageField(upload_to = 'image-category/', null=True)
    background = models.ImageField(upload_to='background-category')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("categories:category_details", kwargs = {"slug": self.slug})