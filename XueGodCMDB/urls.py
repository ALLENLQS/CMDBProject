from django.conf.urls import include, url
from django.contrib import admin
from XueGodCMDB.views import *
from Server.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    # Examples:
    # url(r'^$', 'XueGodCMDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^user/',include('User.urls')),
    url(r'^$',index),
    # url(r'^base/',base),
    url(r'^index/',index),
    url(r'^login/',login),
    url(r'^logout/',logout),
    url(r'^API/',csrf_exempt(API.as_view())),

]
urlpatterns += [
    url(r'^serverList/',serverList),
    url(r'^serverData/',serverData),
    url(r'^gateConnection/',gateoneConnection),
    url(r'^gateConnectionV2/',gateoneConnectionV2),
    url(r'^gateValid/',gateValid),
]