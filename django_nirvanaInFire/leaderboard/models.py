from django.db import models

# Create your models here.
class Leaderboard(models.Model):
    boardtitle=models.CharField(max_length=50,verbose_name='榜单名称')
    bpub_time=models.DateTimeField(verbose_name='更新时间')
    def __str__(self):
        return '%d'%self.pk
class HeroInfo(models.Model):
    hname=models.CharField(max_length=20,verbose_name='姓名')
    hgender=models.BooleanField(verbose_name='男')
    hcontent=models.CharField(max_length=1000,verbose_name='简介')
    hboard=models.ForeignKey('Leaderboard',on_delete=models.CASCADE,verbose_name='所属榜单')
    def __str__(self):
        return '%d'%self.pk
    @property
    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'
    @property
    def hbtitle(self):
        if self.hboard:
            return self.hboard.boardtitle

