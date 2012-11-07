from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from notes.models import Note

notes = Note.objects.all()

urlpatterns = patterns('',
  url(r'^$', ListView.as_view(queryset=notes, template_name="note_list.html")),
  url(r'^note/(?P<slug>[-\w]+)/$', 'django.views.generic.list_detail.object_detail', dict(queryset=notes, slug_field='slug')),
  url(r'^create/$', 'notes.views.create_note'),
  url(r'^note/(?P<slug>[-\w]+)/update/$', 'notes.views.update_note'),
)
