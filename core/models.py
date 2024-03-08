from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=200,null=True)



class Medical(models.Model):
    s1 = models.CharField(max_length=200)
    s2 = models.CharField(max_length=200)
    s3 = models.CharField(max_length=200)
    s4 = models.CharField(max_length=200)
    s5 = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    medicine = models.CharField(max_length=200)
    patient = models.ForeignKey(User, related_name="patient", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease


'''
class Ment(models.Model):
    approved = models.BooleanField(default=False)
    time = models.CharField(max_length=200, null=True)
    patient = models.ForeignKey(User, related_name="pat", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="dor", on_delete= models.CASCADE, null=True)
    ment_day = models.DateTimeField(null=True)
    medical = models.ForeignKey(Medical, related_name="medical", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.approved 
'''


class Ment(models.Model):
    approved = models.BooleanField(default=False)
    time = models.CharField(max_length=200, null=True)
    patient = models.ForeignKey(User, related_name="pat", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="dor", on_delete= models.CASCADE, null=True)
    ment_day = models.DateTimeField(null=True)
    medical = models.ForeignKey(Medical, related_name="medical", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.approved}"


from datetime import date 


 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = '', default = 'profile/avator.png', blank=True)
    birth_date = models.DateField(default='None')
    region = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255) 
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  
    country = models.CharField(max_length=255, default='india') 
    severity = models.CharField(max_length=10, null=True, blank=True)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    def __str__(self):
        return self.country  
    
    def get_gender_numeric(self):
        # Implement logic to convert gender to numeric representation
        if self.gender.lower() == 'male':
            return 1
        elif self.gender.lower() == 'female':
            return 2
        else:
            return 0
 
    def convert_weight_to_numeric(self):  
     if self.weight is not None:
        if self.weight > 60:
            return 0  # Low weight
        elif 60 <= self.weight < 80:
            return 1  # Medium weight
        else:
            return 2  # High weight
     else:
        return 1  # Handle the case where weight is not set


    def convert_severity_to_numeric(self):
        # Implement logic to convert severity label to numeric representation
        if self.severity == 'Low':
            return 1
        elif self.severity == 'Medium':
            return 2
        elif self.severity == 'High':
            return 3
        else:
            return 0
 
   