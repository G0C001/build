from django.db import models

class get_mens(models.Model):
    product_img = models.CharField(max_length=100)
    product_Name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_details = models.CharField(max_length=100)

class get_women(models.Model):
    product_img = models.CharField(max_length=100)
    product_Name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_details = models.CharField(max_length=100)

class get_kids(models.Model):
    product_img = models.CharField(max_length=100)
    product_Name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_details = models.CharField(max_length=100)

class create_user(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
