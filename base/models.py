from django.db import models
       

class Taglines(models.Model):
    tagline = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.tagline}"
  

class Education(models.Model):
    course_title = models.CharField(max_length=200)
    university = models.CharField(max_length=200, null=True)
    enrolled_date = models.DateField('from')
    graduation_date = models.DateField('to')
    currently_enrolled = models.BooleanField(default=False)
    achivements = models.JSONField()

    def __str__(self):
        return f"{self.course_title} at {self.university}"

class SocialMedia(models.Model):
    social_title = models.CharField(max_length=200, null=True)
    social_link = models.CharField(max_length=200, null=True)
    social_icon = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.social_title

class About(models.Model):
    summary = models.TextField(max_length=500)
    address = models.CharField(max_length=200, null=True) 
    title = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(default="ifahadullahkhan@gamil.com")
    website = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    birthday = models.DateField('birthday')
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=200)
    prcentage = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    to = models.DateField('from')
    date_from = models.DateField('to')
    employer = models.CharField(max_length=200, null=True)
    responsibility = models.JSONField()


    def __str__(self):
        return self.title

class Services(models.Model):
    service_name = models.CharField(max_length=200)
    more = models.TextField()
    icon_class = models.CharField(max_length=30)


    def __str__(self):
        return self.service_name

 

    


class Me(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.JSONField(null=True)
    education = models.ManyToManyField(Education)
    social_media = models.ManyToManyField(SocialMedia)
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    experience = models.ManyToManyField(Experience)
    services = models.ManyToManyField(Services)


    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    subject = models.CharField(max_length=90)
    message = models.TextField()


    def __str__(self):
        return f"{self.name} : {self.message}"
    

