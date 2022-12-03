from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

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
path('hackathon/addto',views.addto,name='addto'),
path('cart',views.cart,name='cart'),
path('pluscart/<int:product_id>',views.plus_cart,name='plus_cart'),
path('minuscart/<int:product_id>',views.minus_cart,name='minus_cart'),
path('removecart/<int:remove_id>',views.remove_cart,name='remove_cart'),
path('removeall',views.removeall,name='removeall'),
path('dine',views.dine,name='dine'),
path('dinein',views.dinein,name='dinein'),
path('pluscartd/<int:product_id>',views.plus_cartd,name='plus_cartd'),
path('minuscartd/<int:product_id>',views.minus_cartd,name='minus_cartd'),
path('removecartd/<int:remove_id>',views.remove_cartd,name='remove_cartd'),
path('removealld',views.removealld,name='removealld'),
path('dineto',views.dineto,name='dineto'),
path('checkout',views.checkout,name='checkout'),
path('paymentdone', views.paymentdone, name='paymentdone'),
path('dineinch',views.dineinch,name='dineinch'),
path('paymentdone1', views.paymentdone1, name='paymentdone1'),
path('aboutus', views.aboutus, name='aboutus'),
path('hackathon/aboutus', views.aboutus, name='aboutus'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)