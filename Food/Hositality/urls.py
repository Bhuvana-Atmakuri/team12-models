from django.conf.urls.static import static
from django.urls import path

from . import views
from django.conf import settings
urlpatterns=[
path('orderin',views.home,name='home'),
path('hackathon/<int:store_id>',views.id,name='id'),
path('ko',views.pre,name='pre'),
path('',views.log,name='log'),
path('sign',views.sign,name='sign'),
path('activate/<uidb64>/<token>',views.activate,name='activate'),
path('log',views.login1,name='login1'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)