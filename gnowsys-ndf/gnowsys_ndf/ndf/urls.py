from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from gnowsys_ndf.ndf.views import *

urlpatterns = patterns('gnowsys_ndf.ndf.views.home',
                       url(r'^$', 'homepage', name='homepage'),
)

urlpatterns += patterns('gnowsys_ndf.ndf.views.page',
                        url(r'^gapp/page/(?P<page_id>[\w-]+)$', 'page', name='page'),
                        url(r'^create_page/', 'create_page', name='create_page'),
                        url(r'^resources/page/(?P<node_id>[\w-]+)$', 'display_page', name='display_page'),
)

urlpatterns += patterns('gnowsys_ndf.ndf.views.group',
                        url(r'^gapp/group/(?P<group_id>[\w-]+)$', 'group', name='group'),
                        url(r'^create_group/', 'create_group', name='create_group'),
)

urlpatterns += patterns('gnowsys_ndf.ndf.views.doc',



                        url(r'^gapp/doc/(?P<doc_id>[\w-]+)$', 'doc', name='doc'),
                        url(r'^uploadDoc/$', TemplateView.as_view(template_name='ndf/UploadDoc.html')), #Direct ot html template
                        url(r'^submitDoc/', 'submitDoc', name='submitDoc'),
                        url(r'^submit/', 'submitDoc', name='submitDoc'),
                        url(r'^documentList/', 'GetDoc', name='documentList'),
                        url(r'^readDoc/(?P<_id>[\w-]+)$', 'readDoc', name='read_file'),
)
                       
urlpatterns += patterns('gnowsys_ndf.ndf.views.ajax-views',
                        url(r'^ajax/edit_content/', 'edit_content', name='edit_content'),
)