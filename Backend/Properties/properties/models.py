from django.db import models


class Property(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=32)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    actual_status = models.ForeignKey('Status', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'property'


class Status(models.Model):
    name = models.CharField(unique=True, max_length=32)
    label = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'status'


class StatusHistory(models.Model):
    property = models.ForeignKey(Property, models.DO_NOTHING)
    status = models.ForeignKey(Status, models.DO_NOTHING)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status_history'
