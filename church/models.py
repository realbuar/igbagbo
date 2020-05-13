from django.db import models
from django.forms import ModelForm, Textarea, TextInput


class Video(models.Model):
    name = models.CharField(max_length=555)
    videofile = models.FileField(upload_to='Videos/', null=True,)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=222)
    author = models.CharField(max_length=222)
    pdf = models.FileField(upload_to='Books/Month/')


    class Meta:
        verbose_name_plural = "WSF"


    def __str__(self):
        return self.title







class Bookshop(models.Model):
    title = models.CharField(max_length=222)
    author = models.CharField(max_length=222)
    pdf = models.FileField(upload_to='Books/Month/')


    def __str__(self):
        return self.title


class Topic(models.Model):
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'LIVING FAITH PASTORATE HEADLINES'


    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'LIVING FAITH PASTORATE'

        def __str__(self):
            return self.text[:50] + "..."


class Tropic(models.Model):
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'TESTIMONY HEADLINE'

    def __str__(self):
        return self.text


class Dentry(models.Model):
    tropic = models.ForeignKey(Tropic, on_delete=models.CASCADE)
    text = models.TextField()
    testifier = models.CharField(max_length=234)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'TESTIMONY'

        def __str__(self):
            return self.text[:50] + "..."


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class YafContact(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Read'),
    )
    name = models.CharField(max_length=222)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Youth Alive Contact'
        verbose_name_plural = 'Youth Alive Contacts'


class YafContactForm(ModelForm):
    class Meta:
        model = YafContact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname....'}),
            'subject' : TextInput(attrs={'class': 'input', 'placeholder': 'Your HeadLine......'}),
            'email' : TextInput(attrs={'class': 'input', 'placeholder': 'realbuar@gmail.com'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message........'}),
        }






class Now(models.Model):
    gallery = models.FileField(upload_to='photo/%Y/%m/%d', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=234)

    def __str__(self):
        return self.topic


class New(models.Model):
    top = models.ForeignKey(Now, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + "..."


class One(models.Model):
    name = models.CharField(max_length=333)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
