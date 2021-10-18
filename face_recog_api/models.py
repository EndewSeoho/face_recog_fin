from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class FaceRecogApi(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=1000)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=100)  # Field name made lowercase.
    gender = models.IntegerField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=100)  # Field name made lowercase.
    datetime = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACE_RECOG_API'



