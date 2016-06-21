
from django.conf.urls import url, include
from django.contrib import admin
from interface.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',"interface.views.show_home"),
    url(r'^questions/$',"interface.views.show_questions_stu"),
    url(r'^questions/addmcq/$',"interface.views.add_mcquestion"),
    url(r'^questions/addcq/$',"interface.views.add_cquestion"),  
    url(r'^questions/(?P<id>\d+)/$',"interface.views.add_comment"),
    url(r'^questions/(?P<id>\d+)/postcomment/$',"interface.views.post_comment"),

    url(r'^moderator/$',"interface.views.show_questions_mod"),
    url(r'^moderator/(?P<id>\d+)/$',"interface.views.approve_questions"),
    url(r'^moderator/(?P<id>\d+)/approve/$',"interface.views.approve_questions_accept"),
    url(r'^moderator/(?P<id>\d+)/postcomment/$',"interface.views.post_comment"),
                      
    url(r'^reviews/$',"interface.views.show_reviews"),
    url(r'^ratings/$',"interface.views.show_ratings"),
]
