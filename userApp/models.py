# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Houseinfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    housename = models.CharField(max_length=50, blank=True, null=True)
    houseadd = models.CharField(max_length=20, blank=True, null=True)
    addname = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    housetype = models.CharField(max_length=20, blank=True, null=True)
    housearea = models.FloatField(blank=True, null=True)
    housebound = models.CharField(max_length=50, blank=True, null=True)
    housefloor = models.CharField(max_length=20, blank=True, null=True)
    pricerange = models.CharField(max_length=20, blank=True, null=True)
    arearange = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houseinfo'


class Userinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    userpassword = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'
