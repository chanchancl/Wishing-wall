from django.db import models
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.utils.timezone import *
# Create your models here.

class ServerData(models.Model):
    totalWishing = models.IntegerField()
    
    def __str__(self):
        return 'Current ID %d' % self.totalWishing
    
'''
    return the id 1,2,3,4....n
'''
def AddCurrentID():
    obj,created = ServerData.objects.get_or_create(pk=1)
    if created:
        obj.totalWishing=0
    ret = obj.totalWishing = obj.totalWishing + 1
    obj.save()
    return ret
    
class Wishing(models.Model):
    wID = models.IntegerField()
    wText = models.CharField(max_length=100)
    wData = models.DateTimeField(now())
    
    def __str__(self):
        return '%d : %s %s' % (self.wID,self.wText,self.wData.strftime('%b-%d-%y %H:%M:%S'))


@receiver(post_save,sender=Wishing)
def callback(sender,**kwargs):
    #确认是create动作，然后把ID改为AddCurrentID
    if kwargs['created']:
        obj = kwargs['instance']
        oldID = obj.wID
        obj.wID = AddCurrentID()
        obj.save()
        print('modify ID from %d to %d' % (oldID,obj.wID))
    
    
    
    
    