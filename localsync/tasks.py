import time
from django.utils import timezone
from django.db.models import  Q
from celery import task,chain

import redis

from django.conf import settings

from . import models




def createRedisConection():
    return redis.StrictRedis(host=settings.REDIS_IP, port=settings.REDIS_PORT, db=0)



@task(name="select-Issue-records")
def selectIssueRecords():
    c = createRedisConection()
    timestamp = c.get("timestamp")
    objects = models.Issue1.objects.using('branch').filter(timestamp_system__gte=timestamp)
    splitRecords.delay(objects=objects)
    c.set("timestamp",timezone.now())


@task(name="select-Reciept-records")
def selectRecieptRecords():
    c = createRedisConection()
    timestamp = c.get("timestamp_reciept")
    objects = models.Reciept1.objects.using('branch').filter(timestamp_system__gte=timestamp)
    splitRecordsRecipt1.delay(objects=objects)
    c.set("timestamp_reciept",timezone.now())



#mymodels.Issue2.objects.using('branch').filter(Q(code=obj.code) & Q(pcenter__pk=obj.pcenter.pk) & Q(bilno=obj.bilno)).count()

@task(name="split-records")
def splitRecords(objects):
    for object in objects:
        saveRecords.delay(object=object)



@task(name="split-records-Issue1")
def splitRecordsIssue1(objects):
    for object in objects:
        saveRecords.delay(object=object)
        result = models.Issue2.objects.using('branch').filter(Q(code=object.code) & Q(pcenter__pk=object.pcenter.pk) & Q(bilno=object.bilno))
        splitRecords.delay(result)



@task(name="split-records-recipt1")
def splitRecordsRecipt1(objects):
    for object in objects:
        saveRecords.delay(object=object)
        result = models.Reciept2.objects.using('branch').filter(Q(code=object.code) & Q(pcenter__pk=object.pcenter.pk) & Q(bilno=object.bilno))
        splitRecords.delay(result)

@task(name="save-records")
def saveRecords(object):
    try:
        object.save(using="master")
    except Exception as exc:
        raise saveRecords.retry(exc=exc, countdown=60)


