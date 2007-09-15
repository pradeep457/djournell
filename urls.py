from django.conf.urls.defaults import *
from cornell.notes.models import Note,Courses

info_dict = {
        'queryset': Note.objects.all().order_by('-pub_date'),
        'paginate_by':10,
}

detail_dict = {
        'queryset': Note.objects.all(),
}
urlpatterns = patterns('',
        (r'^admin/', include('django.contrib.admin.urls')),
        (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
        (r'^note/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', detail_dict),
        (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'f:/media/code/python/cornell/public'}),
        (r'^course/(?P<course_id>\d+)/$', 'cornell.notes.views.notes_for_course'),
)
