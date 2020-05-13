from django import forms
from .models import Book, Topic,  Tropic,  Contact, YafContact



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf')



class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class TropicForm(forms.ModelForm):
    class Meta:
        model = Tropic
        fields = ['text']
        labels = {'text': ''}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class YafContactForm(forms.ModelForm):
    class Meta:
        model = YafContact
        fields = "__all__"
