from django.contrib import admin
from .models import Book, Video, Topic, Entry,Now, New, Tropic, Dentry, Contact, YafContact


admin.site.site_header = "LFC TOTAL GARDEN Admin   DASHBOARD"
admin.site.site_title = "WINNERS' TOTAL GARDEN Portal"
admin.site.index_title = "Welcome to WINNERS'   TOTAL   GARDEN "


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date_added')



class TropicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')


class DentryAdmin(admin.ModelAdmin):
    list_display = ('tropic', 'text', 'date_added', 'testifier')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message', 'date_created' )


class YafContactAdmin(admin.ModelAdmin):
  list_display = ('name','email', 'subject', 'message', 'date_created' )


class NowAdmin(admin.ModelAdmin):
    list_display = ('gallery',  'topic')


class NewAdmin(admin.ModelAdmin):
    list_display = ('top', 'text','date_added' )


admin.site.register(YafContact, YafContactAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Dentry, DentryAdmin)
admin.site.register(Tropic, TropicAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Now,NowAdmin )

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'videofile' )

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf')




admin.site.register(Video, VideoAdmin)
admin.site.register(Book, BookAdmin)
