import datetime
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

class Test(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s %s" % (self.name, self.age, self.email)


class Table_equipment(models.Model):
    Eqm_name = models.CharField(max_length=200)
    Eqm_model = models.CharField(max_length=100)
    Amount = models.IntegerField(default=0)
    Date_add = models.DateField('date published')

    def __str__(self):
        return "%s %s %s" % (self.Eqm_name, self.Eqm_model, self.Amount)

    def was_published_recently(self):
        return self.Date_add >= timezone.now() - datetime.timedelta(days=1)

class Equipment_detail(models.Model):
    Eqm_ID = models.ForeignKey(Table_equipment, on_delete=models.CASCADE, null=True, blank=True)
    Detail = models.TextField()
    Img = ProcessedImageField(upload_to='Eqm_images/',
                                           processors=[ResizeToFill(650, 650)],
                                           format='JPEG',
                                           options={'quality': 60})
    def __str__(self):
        return "%s %s %s" % (self.Detail, self.Img, self.Eqm_ID)

class Borrow(models.Model):
    #users = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE,null=True,default = None)

    First_name = models.CharField(max_length=100,null=True) 
    Last_name = models.CharField(max_length=100,null=True) 
    #Get_username = models.CharField(max_length=100,null=True)
    Get_eqm_id = models.IntegerField(default=0)
    Eqm_name = models.CharField(max_length=200,null=True) 
    Get_Amount = models.IntegerField(default=0)
    Br_code = models.CharField(max_length=100,null=True)
    date_br = models.DateField('date published',default = datetime.now().date())
    Date_repatriate = models.DateField('date published')
    Status_borrow = models.BooleanField(default=0)
    Status_repatriate = models.BooleanField(default=0)


class Borro_order(models.Model):
    users = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE,null=True,default = None)
    Eqm_name = models.ForeignKey(Table_equipment,to_field='id',on_delete=models.CASCADE,null=True,default = None)
    Get_Amount = models.IntegerField(default=0)
    date_br = models.DateField('date published',default = datetime.now().date())
    Date_repatriate = models.DateField('date published')
class News(models.Model):
    head = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    
'''
class User(models.Model):
    Name = models.CharField(max_length=130)
    Email = models.EmailField(blank=True)
    Username = models.CharField(max_length = 60)
    Password = models.CharField(max_length = 60)
    date_regis = models.DateField(("Date"), default=datetime.date.today)
'''