from django.db import models
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class ServerData(models.Model):
    totalWishing = models.IntegerField()
    
    def __str__(self):
        return 'Current ID %d' % self.totalWishing
    
    
'''
    return the id 1,2,3,4....n
'''
def AddCurrentID():
    count = ServerData.objects.count()
    if count == 0:
        obj = ServerData.objects.create(pk=1,totalWishing=0)
    else:
        obj = ServerData.objects.get(pk=1)
    ret = obj.totalWishing = obj.totalWishing + 1
    obj.save()
    return ret
    
    '''def AddCurrentID():
    obj = ServerData.objects.all[0]
    if not obj:
        obj = ServerData.objects.create(totalWishing=0)
    ret = obj.totalWishing = obj.totalWishing + 1
    obj.save()
    return ret'''
    
def GetCurrentID():
    ret=0
    obj,created = ServerData.objects.get_or_create(pk=1)
    if not created:
        ret = obj.totalWishing
    return ret
    
class Wishing(models.Model):
    wID = models.IntegerField()
    wText = models.CharField(max_length=100)
    wData = models.DateTimeField(default=timezone.now)
    #only save the md5 checksum of the password
    wPass = models.CharField(max_length=32,default=0)
    wPassword = models.CharField(max_length=32,default=0)
    
    def __str__(self):
        #return '%d : %s %s' % (self.wID,self.wText,self.wData.strftime('%b-%d-%y %H:%M:%S'))
        return '%d : %s %s' % (self.wID,self.wText,timezone.localtime(self.wData).strftime('%Y-%m-%d %H:%I:%S'))


@receiver(post_save,sender=Wishing)
def callback(sender,**kwargs):
    #确认是create动作，然后把ID改为AddCurrentID
    if kwargs['created']:
        obj = kwargs['instance']
        oldID = obj.wID
        obj.wID = AddCurrentID()
        obj.save()
        print('modify ID from %d to %d' % (oldID,obj.wID))
    
    
    
    
    
