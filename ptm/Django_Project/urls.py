"""Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include ,re_path
from django.conf import settings
from django.conf.urls.static import static
from mysite.admin import my_admin_site
from functionality import views as funcviews

urlpatterns = [
    path('admin/', my_admin_site.urls),
    url(r'', include('mysite.urls')),
    path('search', funcviews.search2 , name='search'),
    path('new-property', funcviews.createproperty , name='new-property'),
    path('property-detail/<int:id>', funcviews.propertydetail , name='property-detail'),
    path('add-to-list/<int:listid>/<int:objid>', funcviews.addtolist , name='add-to-list'),
    path('delete-list/<int:id>', funcviews.deletelist , name='delete-list'),
    path('remove-from-list/<int:listid>/<int:objid>', funcviews.removefromlist , name='remove-from-list'),
    path('manage-lists', funcviews.managelists , name='manage-lists'),
    path('create-list', funcviews.createlist , name='create-list'),
    path('name-list/<str:name>/<int:proid>', funcviews.namelist, name='name-list'),
    path('show-list/<int:id>', funcviews.showlist , name='show-list'),
    path('request-tour/<int:listid>/<int:proid>/<int:reqid>', funcviews.requesttour , name='request-tour'),
    path('submit-request/<int:reqid>', funcviews.submitrequest, name='submit-request'),
    path('remove-from-tour/<int:proid>/<int:reqid>', funcviews.removefromtour, name='remove-from-tour'),
    path('show-tour/<int:reqid>', funcviews.showtour, name='show-tour'),
    path('add-note/<int:id>', funcviews.addnote , name='add-note'),
    path('tour-requests', funcviews.toursrequested , name='tour-requests'),
    path('add-to-tour/<int:tid>/<int:proid>', funcviews.addtotour, name='add-to-tour'),
    path('show-notes', funcviews.shownotes , name='show-notes'),
    path('reply-to-note/<int:id>', funcviews.replytonote, name='reply-to-note'),
    path('listnotechange/<int:id>', funcviews.listnotechange, name='listnotechange'),
    path('addfromlist/<int:listid>/<int:proid>/<int:currentid>', funcviews.addfromlist, name='addfromlist'),
    path('listofbuyers', funcviews.listofbuyers, name='listofbuyers'),
    path('approve-tour/<int:id>', funcviews.approvetour, name='approve-tour'),
    path('cancel-tour/<int:id>', funcviews.canceltour, name='cancel-tour'),
    path('createtour', funcviews.createtour , name='create-tour'),
    path('delete-tour/<int:id>', funcviews.deletetour , name='delete-tour'),
    path('offer/<int:id>', funcviews.offer , name='offer'),
    path('offers', funcviews.agent_offercheck , name='offers'),
    path('tour/<int:id>', funcviews.tour, name='tour'),
    path('changestatus/<str:id>/<int:id2>', funcviews.changeofferstatus),
    path('profile/<str:usr>', funcviews.profilepage, name='profile'),
    path('share-list/<str:usr>/<int:id>', funcviews.sharelist),
    path('share-list-buyer/<str:usr>/<int:id>', funcviews.sharelistbuyer),
    path('unlink/<int:id>', funcviews.unlinklist),
    path('rate/<int:listid>/<int:proid>/<int:rating>', funcviews.ratepro),
]


if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)