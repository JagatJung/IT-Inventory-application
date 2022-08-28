from curses.ascii import NUL
from django.db import models

# Create your models here.
class useraccounts(models.Model):
        email = models.CharField(max_length=100)
        EmployeeName = models.CharField(max_length=100)
        Employee_id = models.CharField(max_length=50)
        DepartmentName = models.CharField(max_length=50)
        ManagerID = models.CharField(max_length=50)
        password=models.CharField(max_length=50)
        isManager = models.BooleanField(default=False)

        # most required fields
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(auto_now_add=True)
        isadmin = models.BooleanField(default=False)
        isactive = models.BooleanField(default=False)
        issuperadmin = models.BooleanField(default=False)

        class Meta:
            verbose_name = "useraccount"
            verbose_name_plural = "useraccounts"

        def __str__(self):
            return self.EmployeeName

class vendors(models.Model):
    vendorId = models.CharField(max_length=50)
    vendorName = models.CharField(max_length=100)
    vendorLoaction = models.CharField(max_length=100)
    vendorPhone = models.CharField(max_length=100)
    vendorEmail = models.CharField(max_length=100)

        # most required fields
    date_started = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=False)

    class Meta:
        verbose_name = "vendor"
        verbose_name_plural = "vendors"

    def __str__(self):
        return self.vendorName

