from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class packagemodel(models.Model):
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=10000)
    photo1=models.CharField(max_length=400,default="")
    photo2=models.CharField(max_length=400,default="")
    photo3=models.CharField(max_length=400,default="")
    photo4=models.CharField(max_length=400,default="")
    # type=models.CharField(max_length=400,default="")
    PLOG=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"
        
    def __str__(self):
        return self.title






class feedback(models.Model):
    a=models.CharField(max_length=10000)
    FDLOG= models.ForeignKey(User, on_delete=models.CASCADE)

class cmplnt(models.Model):
    time=models.CharField(max_length=100)
    c=models.CharField(max_length=1000)
    re=models.CharField(max_length=1000)
    CLOG=models.ForeignKey(User, on_delete=models.CASCADE)

class appointments(models.Model):
    location=models.CharField(max_length=100,default="")
    date=models.CharField(max_length=100)
    details=models.CharField(max_length=10000,default="")
    status=models.CharField(max_length=100)
    amount=models.CharField(max_length=100,default="")
    estimate=models.CharField(max_length=100,default="")
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    ALOG=models.ForeignKey(packagemodel,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "appointments"
        verbose_name_plural = "appointments"
        
    def __str__(self):
        return self.title


class payments(models.Model):
    REQ_MAIN=models.ForeignKey(appointments,on_delete=models.CASCADE,default="")
    p_date=models.CharField(max_length=500)
    amnt=models.CharField(max_length=500)
    p_status=models.CharField(max_length=500)

    class Meta:
        verbose_name = "payments"
        verbose_name_plural = "payments"
        
    def __str__(self):
        return self.title

