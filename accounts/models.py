from curses.ascii import NUL
from tabnanny import verbose
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




class devicetypes(models.Model):
    typename= models.CharField(max_length=50)

        # most required fields
    date_purchased = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=False)

    class Meta:
        verbose_name = "devicetype"
        verbose_name_plural = "devicestypes"

    def __str__(self):
        return self.typename



class devices(models.Model):
    serialnum = models.CharField(max_length=50)
    hostname = models.CharField(max_length=100)
    devicemodel = models.CharField(max_length=100)
    purchasedate= models.DateField(auto_now_add=False)
    warrentyperiod = models.CharField(max_length=2)
    vendorid = models.ForeignKey(vendors, on_delete=models.CASCADE)
    devicetypeid = models.ForeignKey(devicetypes, on_delete=models.CASCADE)


        # most required fields
    date_purchased = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=False)
    isavailable = models.BooleanField(default=True)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

    def __str__(self):
        return self.hostname

class issues(models.Model):
    state = models.CharField(max_length=100)
    issuedate = models.DateField()
    returndate = models.DateField()

    deviceid = models.ForeignKey(devices, on_delete=models.CASCADE)
    employeeeid = models.ForeignKey(useraccounts, on_delete=models.CASCADE)
    
    isactive = models.BooleanField(default=False)
    date_recorded = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name ="issue"
        verbose_name_plural = "issues"

    def __str__(self):
        return (str(self.date_recorded))