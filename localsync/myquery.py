import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)


import django
from localsync.models import *
obj = Issue1.objects.using('other').get(pk=33233)
obj.save(using='default')
obj.save(using='other')

def saveDeeply(obj,target_db='default'):
    try:
        for f in obj._meta.get_fields():
            if  isinstance(f,django.db.models.fields.related.ForeignKey):
                logging.info(f)
                if getattr(obj,f.name):
                    val = getattr(obj,f.name)
                    logging.debug(val)
                    #saveDeeply(val)
        obj.save(using=target_db)
    except Exception, err:
        print Exception, err
saveDeeply(obj)



from autosync import models
myclass  = dict([(name, cls) for name, cls in models.__dict__.items() if isinstance(cls, type)])

for k in myclass:
    print ("""
    alter table {0}
ADD TIMESTAMP_SYSTEM TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

create trigger {1}_t_up_ts
before update on {2}
for each row
begin
    select systimestamp into :new.TIMESTAMP_SYSTEM from dual;
end;
/
    """.format(getattr(models,k)._meta.db_table,getattr(models,k)._meta.db_table,getattr(models,k)._meta.db_table))