import time
from django.utils import timezone
from celery import task,chain
import redis

from . import models




def createRedisConection():
    return redis.StrictRedis(host='192.168.99.100', port=32775, db=0)



@task(name="select-Issue-records")
def selectIssueRecords():
    c = createRedisConection()
    timestamp = c.get("timestamp")
    objects = models.Issue1.objects.using('branch').filter(timestamp_system__gte=timestamp)
    splitRecords.delay(objects=objects)
    objects = models.Issue2.objects.using('branch').filter(timestamp_system__gte=timestamp)
    splitRecords.delay(objects=objects)
    c.set("timestamp",timezone.now())


@task(name="select-Reciept-records")
def selectRecieptRecords():
    c = createRedisConection()
    timestamp = c.get("timestamp_reciept")
    objects = models.Reciept1.objects.using('branch').filter(timestamp_system__gte=timestamp)
    splitRecords.delay(objects=objects)
    objects = models.Reciept1.objects.using('branch').filter(timestamp_system__gte=timestamp)
    splitRecords.delay(objects=objects)
    c.set("timestamp_reciept",timezone.now())



#mymodels.Issue2.objects.using('branch').filter(Q(code=obj.code) & Q(pcenter__pk=obj.pcenter.pk) & Q(bilno=obj.bilno)).count()

@task(name="split-records")
def splitRecords(objects):
    for object in objects:
        saveRecords.delay(object=object)

@task(name="save-records")
def saveRecords(object):
    try:
        object.save(using="master")
    except Exception as exc:
        raise saveRecords.retry(exc=exc, countdown=60)


models.Reciept1.objects.using('master').all()