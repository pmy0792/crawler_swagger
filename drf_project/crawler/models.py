from django.db import models

class Project(models.Model):
    title = models.CharField('NAME',max_length=100, unique=True)
    mode = models.CharField('MODE',max_length=20)
    keyword = models.TextField('KEYWORD') # save 시: list-> json, read 시: json->list
    state = models.CharField('STATE',max_length=20, default='initialized')
    total_image = models.IntegerField('TOTAL IMAGE',default=0)
    collected_image = models.IntegerField('COLLECTED IMAGE',default=0)
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    class Meta:
        ordering = ('create_dt',)

    def __str__(self):
        return self.title
    
class Crawler(models.Model):
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
    mode = models.CharField('MODE',max_length=20)
    keyword = models.TextField('KEYWORD') # list 아니고 string
    state = models.CharField('STATE',max_length=20, default='initialized')
    total_image = models.IntegerField('TOTAL IMAGE',default=0)
    collected_image = models.IntegerField('COLLECTED IMAGE',default=0)
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    website = models.TextField('WEBSITE')
    pid = models.IntegerField('PID', default=-1)
    
    def __str__(self):
        return self.project +" > "+self.keyword + " > "+self.website
    
class Image(models.Model):
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
    crawler = models.ForeignKey('Crawler', on_delete=models.DO_NOTHING)
    url = models.TextField('URL') #img src url
    save_path = models.TextField('SAVE PATH', default='/')
    
    cut = models.CharField('CUT', max_length=20,blank=True)
    part = models.CharField('PART',  max_length=20,blank=True)
    direction = models.CharField('DIRECTION', max_length=20,blank=True)
    pose = models.CharField('POSE',  max_length=20,blank=True)
    is_head = models.CharField('IS HEAD',  max_length=20,blank=True)
    person_count = models.CharField('PERSON COUNT', max_length=20, blank=True)
    
    def __str__(self):
        return self.url
    
