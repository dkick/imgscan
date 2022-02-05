from django.db import models


def imgpath(__, filename):
    return F'imgscan/{filename}'


class Image(models.Model):
    # The spec calls for a field named 'objects'; rename the default
    # manager to avoid colliding.
    dbobjects = models.Manager()

    id = models.BigAutoField(primary_key=True)
    imgfile = models.FileField(upload_to=imgpath, unique=True)
    detect = models.BooleanField(default=True)
    scanned = models.DateTimeField(null=True)

    # https://amir.rachum.com/blog/2013/06/15/
    #   a-case-for-a-onetomany-relationship-in-django/
    objects = models.ManyToManyField('ImgObject')


class ImgObject(models.Model):
    # class Meta:
    #     unique_together = ('image', 'label')

    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.label
