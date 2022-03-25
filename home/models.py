from django.db import models

#  models here.
# About model
class About(models.Model):
    short_description= models.Textfield()
    description=models.ImageField(upload_to="about")

    class Meta:
        verbose_name="About me"
        verbose_name_plural="About me"

    def __str__(self):
        return "About me"

#service model
class Service(models.Model):
    name=models.Charfield(max_length=100, verbose_name="Service name")
    description =models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name

#Recent Work model
class RecentWork(models.Model):
    title=models.Charfield(max_length=100, verbose_name=" Work title")
    image=models.ImageField(upload_to="Works")

    def __str__(self):
        return self.title

#Client model
class Client(models.Model):
    name=models.CharField(max_length=100,verbose_name="Client name")
    description =models.TextField(verbose_name="Client say")
    image=models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
