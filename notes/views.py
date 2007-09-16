from django.views.generic.list_detail import object_list
from cornell.notes.models import *

def notes_for_course(request, course_slug):
    course = Courses.objects.get(slug=course_slug)
    notes  = course.note_set.all()
    return object_list(request, queryset=notes,template_name='Notes/notes_for_course.html',paginate_by=15)
