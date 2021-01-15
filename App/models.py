from django.db import models

class App(models.Model):
    #Uygulama Sahibi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()
    #Uygulama Detayı
    AppHeader = models.CharField(max_length=50)
    AppContent = models.TextField(max_length=1000)
    AppPhoto = models.ImageField(upload_to = 'images/')
    AppLink = models.TextField(max_length=200)
    AppType = models.CharField(max_length=10)
    # Tarih
    UpdateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.AppHeader


class Idea(models.Model):
    #Fikir Sahibi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()
    #Fikir Detayı
    IdeaHeader = models.CharField(max_length=50)
    IdeaContent = models.TextField(max_length=1000)
    IdeaType = models.CharField(max_length=10)
    # Tarih
    UpdateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.IdeaHeader

class Forum(models.Model):
    #Forum Sahibi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()
    #Forum Detayı
    ForumHeader = models.CharField(max_length=50)
    ForumContent = models.TextField(max_length=1000)
    ForumisActive = models.BooleanField(default=True)
    # Tarih
    UpdateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ForumHeader


class SaveDatas(models.Model):
    #Kaydeden Kişi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()
    #Post Detayı
    PostId = models.IntegerField()
    PostType = models.CharField(max_length=10)
    # Tarih
    UpdateDate = models.DateTimeField(auto_now=True)

class LikeDatas(models.Model):
    #Beğenen Kişi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()
    #Post Detayı
    PostId = models.IntegerField()


class CommentDatas(models.Model):
    #Yorum Sahibi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()

    #Post Detayı
    PostId = models.IntegerField()
    PostType = models.CharField(max_length=10)

    #Yorum Detayı
    Comment = models.TextField(max_length=150)
    CommentDate = models.DateTimeField(auto_now_add=True)


class Mails(models.Model):
    #Mail Sahibi
    Owner = models.CharField(max_length=30)
    OwnerId = models.IntegerField()
    OwnerEmail = models.EmailField()
    #Mail Detay
    MailHeader = models.CharField(max_length=100)
    MailContent =models.TextField(max_length=1000)
    #Mail Tarih
    MailDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.MailHeader