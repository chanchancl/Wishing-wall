from django.db import models

# Create your models here.

class ServerData(models.Model):
    totalWishing = models.IntegerField()
    
    
def GetTotalObj():
    try:
        obj = ServerData.objects.get(pk=1)
    except:
        obj = ServerData.objects.create(totalWishing=1)
        obj.totalWishing = 0
    return obj
    
def GetCurrentID():
    return GetTotalObj().totalWishing
    
def ModifyTotal(num=1):
    obj = GetTotalObj()
    obj.totalWishing += num
    obj.save()
    return obj.totalWishing
    
class Wishing(models.Model):
    wID = models.IntegerField()
    wText = models.CharField(max_length=100)
    
    def create(self,text,*args, **kwargs):
        id = ModifyTotal()
        obj = super().create(wID=id,wText=text,*arg,**kwargs)
        return obj
        
    def delete(self, using=None, keep_parents=False):
        if GetCurrentID() >= 1:
            ModifyTotal(-1)
        super().delete()
        print('-*-*-*-*-*-*-*-delete-*-*-*-*-*-*-*-')
    
    def __str__(self):
        return '%d : %s' %(self.wID,self.wText)
        
        