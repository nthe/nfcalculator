import os
from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import misaka
from jk.settings import MEDIA_DIR, BASE_DIR
from django.contrib.auth import get_user_model
# manx = get_user_model()
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Document(models.Model):

    user = models.ForeignKey(User) # <=== user_id
    name = models.CharField(max_length=200)
    doc_file = models.FileField(upload_to=user_directory_path)
    date_upload = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("accounts:list_documents", kwargs={'pk': self.id})

    # NEW CODE!

    def remove_on_file_update(self):
        try:
            # is the object in the database yet?
            obj = Document.objects.get(id=self.id)
        except Document.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.doc_file and self.doc_file and obj.doc_file != self.doc_file:
            # delete the old image file from the storage in favor of the new file
            obj.doc_file.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.doc_file.delete()
        return super(Document, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_file_update()
        return super(Document, self).save(*args, **kwargs)


class ProcessedDocument(models.Model):

    user = models.ForeignKey(User)
    display_name = models.CharField(max_length=256)
    path_to_processed_file = models.CharField(max_length=256)
    date_upload = models.DateField(auto_now=True)
    # slug = models.SlugField(allow_unicode=True, unique=True)

    def __str__(self):
        return self.display_name

        # NEW CODE!

    def remove_on_file_update(self):
        try:
            # is the object in the database yet?
            obj = ProcessedDocument.objects.get(id=self.id)
        except ProcessedDocument.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.path_to_processed_file and self.path_to_processed_file and obj.name != self.path_to_processed_file:
            # delete the old image file from the storage in favor of the new file
            obj.display_name.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        # self.name = self.name.split('media/')[1]
        # print('tu sa nachadzam: {}'.format(os.getcwd()))
        # print('tot sa snazim odmazat: {}'.format(BASE_DIR + self.name))
        os.remove(BASE_DIR + self.path_to_processed_file)
        return super(ProcessedDocument, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_file_update()
        return super(ProcessedDocument, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("accounts:list_processed_documents", kwargs={'pk': self.id})

    class Meta():
        ordering = ['path_to_processed_file']


# class UserProfileSpecification(models.Model):
#     user = models.ForeignKey(manx, related_name='user_profile')
#     # additional
#
#     company = models.CharField(max_length=70, blank=True)
#     portfolio_site = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
#
#     def __str__(self):
#         return self.user.username


class NutritionFact(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class Allergen(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class Extra(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=False)
    allergens = models.ManyToManyField(Allergen)
    may_contain = models.ManyToManyField(Extra)


class Product(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product)
    ingredient = models.ForeignKey(Ingredient)
    weight = models.FloatField(null=False, default=0)


class IngredientNutritionFact(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    nutrition_fact = models.ForeignKey(NutritionFact)
    weight = models.FloatField(null=False, default=0)
