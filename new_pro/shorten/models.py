from django.db import models

# Create your models here.
class bitly(models.Model):
    user = models.CharField(max_length=15,null=True)
    long_url = models.URLField(null=False)
    shortcode = models.CharField(max_length = 6,unique = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    datewise = models.TextField()

    def _str_(self):
        return self.shortcode
