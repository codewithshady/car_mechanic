from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Banner(models.Model):
    image=models.ImageField(upload_to="images/banner")
    title=models.CharField(max_length=100)
    heading1=models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    description1 = RichTextField()
    description2 = RichTextField()
    description3 = RichTextField()
    points=RichTextField(max_length=1000)


class About_details(models.Model):
    description3=RichTextField()


class Services(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/services')
    description=RichTextField(null=True)

    def __str__(self):
        return self.title

class Services_details(models.Model):
    service=models.ForeignKey(Services,on_delete=models.CASCADE, null=True)
    image1 = models.ImageField(upload_to='images/services')
    description2 = RichTextField(null=True)

class Mission(models.Model):
    title=models.CharField(max_length=100)
    details=RichTextField()
    details1 = RichTextField()
    details2 = RichTextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    message = models.TextField()

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    gallery = models.ImageField(upload_to='images/gallery')



