from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"

class Info(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    judul = models.CharField(max_length=100)
    body = models.TextField()
    kategory = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Info"
    
