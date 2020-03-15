from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=255)
    image = models.FilePathField(path="/img")
    # todo: either change technology to a list of technologies or add a keywords field or just use a comma seperated string for technologies...
    # todo: add a start and end date
    # todo: add company name
    # todo: change title to (project) name
    # todo: is an image needed?
