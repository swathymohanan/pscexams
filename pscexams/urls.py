from django.conf.urls import patterns, url, include
from pscexams.views import *
from pscexams.tutor.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^outsource/', include('outsource.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),


    # URL for index pages
    (r'^$',index),
    (r'^login/$',login_view),
    (r'^home/$',home),
    (r'^tutor/questions/add/$',tutor_questions_add),
    (r'^state/ajax/exam/$',state_ajax_exam),
    (r'^exam/ajax/subject/$',exam_ajax_subject),
    (r'^subject/ajax/topic/$',subject_ajax_topic),
    (r'^subtopic/ajax/oneword/$',subtopic_ajax_oneword),
    (r'^tutor/questions/edit/$', tutor_questions_edit),
    (r'^logout/$', logout_view),
    (r'^register/$', register),
    (r'^registration/$', registration_add),
    (r'^about/$',about),
    (r'^smartindia/$',smartindia),
    (r'^keralapsc/$',keralapsc),
    (r'^topic/ajax/subtopic/$',topic_ajax_subtopic),
    (r'^subtopic/ajax/question/$',subtopic_ajax_question),
    (r'^tutor/myaccount/$',tutor_myaccount),
    (r'^about/previous/year/question/$',about_previous_year_question),
    (r'^about/modelexams/$',about_model_exams),
    (r'^about/tipsandtricks/$',about_tipsandtricks),
    (r'^about/readandlearn/$',about_readandlearn),
    (r'^about/new/$',about_new),
    (r'^about/examcategory/$',about_examcategory),
    (r'^about/subject/topics/$',about_subject_topics),
    (r'^about/topic/subtopic/$',about_topic_subtopic),
    
    
    
    


   
    # Student Urls
    url(r'^student/', include('pscexams.student.urls')),
    url(r'^publisher/', include('pscexams.publisher.urls')),
    url(r'^siteadmin/', include('pscexams.admin.urls')),
    url(r'^tutor/', include('pscexams.tutor.urls')),


)