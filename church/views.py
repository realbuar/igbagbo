from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm, ContactForm, YafContactForm
from .models import Book, Video, Topic, Tropic,Dentry, Bookshop, Contact, Now, YafContact

from django.contrib import messages


class Home(TemplateView):
    template_name = 'church/home.html'


"""
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = url = fs.url(name)
    return render(request, 'church/upload.html', context)

"""

def upload(request):
    videos = Video.objects.all()
    return render(request, 'church/upload.html', {
        'videos': videos
    })





def wsf(request):
    books = Book.objects.all()
    return render(request,'church/wsf_list.html', {
        'books': books
    })

"""
def book_month(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('church:wsf_list')
    else:
        form = BookForm()
    return render(request,'church/book_list.html', {
        'form': form
    })

"""


def shop(request):
    bookshops = Bookshop.objects.all()
    return render(request,'church/book_list.html', {
        'bookshops': bookshops
    })



def contact(request):
    if request.method == 'POST':
        email_d = request.POST.get('email')
        subject_e = request.POST.get('subject')
        message_f = request.POST.get('message')

        a = Contact(email=email_d, subject=subject_e, message=message_f)
        a.save()
        return redirect(request, 'church/back.html', {})
    else:
        return render(request, 'church/back.html')



def yafcontact(request):
    if request.method == 'POST':
        email_a = request.POST.get('email')
        name_b = request.POST.get('name')
        subject_c = request.POST.get('subject')
        message_d = request.POST.get('message')

        d = YafContact(email=email_a, name=name_b, subject=subject_c, message=message_d)
        d.save()
        return render(request, 'church/alayo.html', {})
    else:
        return render(request, 'church/alayo.html')








def studio(request):
    return render(request, 'church/nice.html')

"""
def ict(request):
    return render(request, 'church/upload.html')

"""



def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'church/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'church/good.html', context)




def tropics(request):
    tropics = Tropic.objects.order_by('date_added')
    context = {'tropics': tropics}
    return render(request, 'church/wonder.html', context)


def tropic(request, tropic_id):
    tropic = Tropic.objects.get(id=tropic_id)
    dentries = tropic.dentry_set.order_by('-date_added')
    context = {'tropic': tropic, 'dentries': dentries}
    return render(request, 'church/no.html', context)


def Yaf(request):
    return render(request, 'church/amen.html')







def tops(request):
    tops = Now.objects.order_by('date_added')
    context = {'tops':tops}
    return render(request, 'church/new.html', context)


def top(request, top_id):
    top = Now.objects.get(id=top_id)
    news = top.new_set.order_by('-date_added')
    context = {'top':top, 'news':news}
    return render(request, 'church/news.html', context)
