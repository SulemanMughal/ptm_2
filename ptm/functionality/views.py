from django.shortcuts import render,redirect
from .models import properties,shortlist,notes,tourrequests,offers,propertyrating
from .forms import propertyform
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from mysite.models import profileModel
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from Django_Project.settings import EMAIL_HOST_USER

@login_required
def search2(request):
    template = 'search2.html'
    context = {}
    obj = profileModel.objects.get(user=request.user).Teacher_or_Parent
    if obj == 'Agent':
        context['agentcheck'] = True
    else:
        context['agentcheck'] = False
    try:
        if request.method == 'GET':
            probjs = []
            a = request.GET['city']
            b = request.GET['area']
            objs = properties.objects.all()
            for i in objs:
                if a.lower() in i.city.lower():
                    if b == '':
                        probjs.append(i)
                    else:
                        if b.lower() in i.area.lower():
                            probjs.append(i)
                        else:
                            pass
            context['listofproperty'] = probjs
    except:
        pass
    return render(request,template,context)

@login_required
def createproperty(request):
    template = 'new-property.html'
    form = propertyform(request.POST)
    if form.is_valid():
        a = form.cleaned_data
        b = properties()
        b.user = request.user
        b.price = a['price']
        b.sqft = a['sqft']
        b.beds = a['beds']
        b.baths = a['baths']
        b.family_type = a['family_type']
        b.year_built = a['year_built']
        b.heating = a['heating']
        b.cooling = a['cooling']
        b.parking = a['parking']
        b.lot = a['lot']
        b.description = a['description']
        b.save()
        try:
            image = a['image1']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image1 = fs.url(filename)
            b.save()
            image = a['image2']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image2 = fs.url(filename)
            b.save()
            image = a['image3']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image3 = fs.url(filename)
            b.save()
            image = a['image4']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image4 = fs.url(filename)
            b.save()
            image = a['image5']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image5 = fs.url(filename)
            b.save()
        except:
            pass
    else:
        form = propertyform()
    context = {'form':form}
    return render(request,template,context)

@login_required
def propertydetail(request,id):
    template = 'page_51.html'
    obj = properties.objects.get(pk=id)
    objs = shortlist.objects.filter(user=request.user)
    objs1 = tourrequests.objects.filter(user=request.user)
    context = {'obj':obj,'lists':objs,'tours':objs1}
    obj = profileModel.objects.get(user=request.user).Teacher_or_Parent
    if obj == 'Agent':
        context['agentcheck'] = True
    else:
        context['agentcheck'] = False
    return render(request,template,context)

@login_required
def addtolist(request,listid,objid):
    listobj = shortlist.objects.get(pk=listid)
    obj = properties.objects.get(pk=objid)
    listobj.relproperties.add(obj)
    listobj.save()
    obj1 = propertyrating()
    obj1.linklist = listobj
    obj1.relproperty = obj
    obj1.save()
    return redirect('/property-detail/'+str(objid))

@login_required
def deletelist(request,id):
    listobj = shortlist.objects.get(pk=id)
    listobj.delete()
    return redirect('/manage-lists')

@login_required
def deletetour(request,id):
    tourobj = tourrequests.objects.get(pk=id)
    tourobj.delete()
    return redirect('/tour-requests')

@login_required
def removefromlist(request,listid,objid):
    listobj = shortlist.objects.get(pk=listid)
    obj = properties.objects.get(pk=objid)
    listobj.relproperties.remove(obj)
    listobj.save()
    for i in propertyrating.objects.all():
        if i.linklist == listobj and i.relproperty == obj:
            i.delete()
    return redirect('/show-list/'+str(listid))

@login_required
def managelists(request):
    if request.method == 'POST':
        a = request.POST
        obj = shortlist.objects.get(pk=a['id'])
        obj.name = a['listname']
        obj.save()
    template = 'page_24_End.html'
    lists = []
    for i in shortlist.objects.all():
        if i.user == request.user or request.user in i.shared_with.all():
            lists.append(i) 
    context = {'lists':reversed(lists)}
    context['agentlist'] = profileModel.objects.filter(Teacher_or_Parent = 'Agent')
    context['buyerlist'] = profileModel.objects.filter(Teacher_or_Parent = 'Buyer')
    obj = profileModel.objects.get(user=request.user).Teacher_or_Parent
    if obj == 'Agent':
        context['agentcheck'] = True
    else:
        context['agentcheck'] = False
    return render(request,template,context)

@login_required
def createlist(request):
    obj = shortlist()
    obj.user = request.user
    obj.save()
    return redirect('/manage-lists')

@login_required
def createtour(request):
    obj = tourrequests()
    obj.user = request.user
    obj.save()
    return redirect('/tour-requests')

@login_required
def namelist(request,name,proid):
    obj = shortlist()
    obj.name = name
    obj.user = request.user
    obj.save()
    obj.relproperties.add(properties.objects.get(pk=proid))
    obj.save()
    return redirect('/manage-lists')

@login_required
def showlist(request,id):
    template = 'page_30_End.html'
    obj = shortlist.objects.get(pk=id)
    if request.method == 'POST':
        a = request.POST['id']
        b = stripspace(request.POST['propertynote'])
        for i in notes.objects.all():
            if i.user == request.user and (i.relproperty == properties.objects.get(pk=a) and i.relshortlist == obj):
                i.delete()
                break
        note = notes()
        note.user = request.user
        note.relproperty = properties.objects.get(pk=a)
        note.relshortlist = obj
        note.note = b
        note.save()
    context = {'obj':obj}
    context['agents'] = profileModel.objects.filter(Teacher_or_Parent='Agent')
    objs = notes.objects.filter(relshortlist = obj)
    check = 2
    notelist = {}
    ratings = {}
    for i in obj.relproperties.all():
        ratings[i] = getrating(i,obj)
        for j in objs:
            if j.relproperty == i and j.relshortlist == obj:
                notelist[i] = j.note
                check = 1
                break
            else:
                check = 2
        if check == 2:
            notelist[i] = ''
    context['notes'] = notelist.items()
    context['ratings'] = ratings.items()
    context['lists'] = []
    for i in shortlist.objects.all():
        if i.user == request.user and i != context['obj']:
            context['lists'].append(i)
    if profileModel.objects.get(user=request.user).Teacher_or_Parent == 'Agent':
        context['agentcheck'] = True
    else:
        context['agentcheck'] = False
    return render(request,template,context)

@login_required
def requesttour(request,listid,proid,reqid):
    template = 'page_43_google_slides.html'
    context = {}
    if (int(reqid) != 0):
        reqobj = tourrequests.objects.get(pk=reqid)
    elif (int(listid) == 0):
        obj = properties.objects.get(pk=proid)
        reqobj = tourrequests()
        reqobj.user = request.user
        reqobj.save()
        reqobj.relproperty.add(obj)
        reqobj.save()
    elif (int(proid) == 0):
        obj = shortlist.objects.get(pk=listid)
        reqobj = tourrequests()
        reqobj.user = request.user
        reqobj.save()
        for i in obj.relproperties.all():
            reqobj.relproperty.add(i)
        reqobj.save()
    else:
        pass
    context['reqobj'] = reqobj
    return render(request,template,context)

@login_required
def removefromtour(request,proid,reqid):
    obj = tourrequests.objects.get(pk=reqid)
    obj.relproperty.remove(properties.objects.get(pk=proid))
    return redirect('/request-tour/0/0/'+str(reqid))

@login_required
def submitrequest(request,reqid):
    reqobj = tourrequests.objects.get(pk=reqid)
    a = request.POST
    reqobj.date1 = a['date1']
    reqobj.time1_date1 = a['time1']
    reqobj.time2_date1 = a['time2']
    reqobj.time3_date1 = a['time3']
    reqobj.date2 = a['date2']
    reqobj.time1_date2 = a['time4']
    reqobj.time2_date2 = a['time5']
    reqobj.time3_date2 = a['time6']
    reqobj.date3 = a['date3']
    reqobj.time1_date3 = a['time7']
    reqobj.time2_date3 = a['time8']
    reqobj.time3_date3 = a['time9']
    reqobj.note = a['note']
    reqobj.name = a['tourname']
    reqobj.status = 'Requested'
    reqobj.save()
    return redirect('/show-tour/'+str(reqid))

@login_required
def showtour(request,reqid):
    template = 'page_54_google_slides.html'
    context = {}
    if (profileModel.objects.get(user=request.user).Teacher_or_Parent == 'Agent'):
        context['agentcheck'] = True
    else:
        context['agentcheck'] = False
    reqobj = tourrequests.objects.get(pk=reqid)
    context['reqobj'] = reqobj
    return render(request,template,context)

@login_required
def addnote(request,id):
    template = 'add-note.html'
    context = {'id':id}
    if request.method == 'POST':
        id = request.POST['id']
        note1 = request.POST['note']
        for i in profileModel.objects.filter(Teacher_or_Parent = 'Agent'):
            a = notes()
            a.user = request.user
            a.reciever = i.user
            a.relproperty = properties.objects.get(pk=id)
            a.note = note1
            a.save()
        return redirect('/property-detail/'+str(id))
    return render(request,template,context)

@login_required
def toursrequested(request):
    if request.method == 'POST':
        obj = tourrequests.objects.get(pk=request.POST['id'])
        obj.name = request.POST['listname']
        obj.save()
    template = 'tr.html'
    context = {}
    a = profileModel.objects.get(user=request.user).Teacher_or_Parent
    if a == 'Buyer':
        context['agentcheck'] = False
        context['objs'] = reversed(tourrequests.objects.filter(user=request.user))
    else:
        context['agentcheck'] = True
        context['objs'] = reversed(tourrequests.objects.all())
    return render(request,template,context)

@login_required
def shownotes(request):
    template = 'show-notes.html'
    context = {'sent':notes.objects.filter(user=request.user),'recieved':notes.objects.filter(reciever=request.user)}
    return render(request,template,context)

@login_required
def replytonote(request,id):
    template = 'add-note.html'
    context = {'id':id}
    if request.method == 'POST':
        id = request.POST['id']
        note1 = request.POST['note']
        noteobj = notes.objects.get(pk=id)
        a = notes()
        a.user = noteobj.reciever
        a.reciever = noteobj.user
        a.relproperty = noteobj.relproperty
        a.note = note1
        a.save()
        return redirect('/show-notes')
    return render(request,template,context)

@login_required
def listnotechange(request,id):
    obj = shortlist.objects.get(pk=id)
    obj.note = stripspace(request.POST['listnote'])
    obj.save()
    return redirect('/show-list/'+str(id))

@login_required
def addfromlist(request,listid,proid,currentid):
    obj1 = properties.objects.get(pk=proid)
    obj = shortlist.objects.get(pk=listid)
    obj.relproperties.add(obj1)
    obj.save()
    obj = shortlist.objects.get(pk=currentid)
    obj.relproperties.add(obj1)
    obj.save()
    return redirect('/show-list/'+str(currentid))

@login_required
def listofbuyers(request):
    template = 'page_46_End.html'
    context = {'objs':profileModel.objects.filter(Teacher_or_Parent='Buyer')}    
    if profileModel.objects.get(user=request.user).Teacher_or_Parent != 'Agent':
        return redirect('/')
    else:
        context['agentcheck'] = True
    return render(request,template,context)

@login_required
def addtotour(request,tid,proid):
    obj = tourrequests.objects.get(pk=tid)
    obj.relproperty.add(properties.objects.get(pk=proid))
    return redirect('/property-detail/'+str(proid))

@login_required
def approvetour(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'Scheduled'
    obj.save()
    return redirect('/show-tour/'+str(id))

@login_required
def canceltour(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'Cancelled'
    obj.save()
    return redirect('/show-tour/'+str(id))

@login_required
def offer(request,id):
    obj = offers()
    obj.user = request.user
    obj.relproperty = properties.objects.get(pk=id)
    obj.note = request.POST['offer']
    obj.save()
    return redirect('/property-detail/'+str(id))

@login_required
def agent_offercheck(request):
    context = {}
    if (profileModel.objects.get(user=request.user).Teacher_or_Parent == 'Agent'):
        template = 'page_81_End.html'
        objs = offers.objects.all()
        context['data'] = {}
        for i in objs:
            if i in context['data'].keys():
                context['data'][i.user.username].append(i)
            else:
                context['data'][i.user.username] = []
                context['data'][i.user.username].append(i)
        context['agentcheck'] = True
    else:
        template = 'page_43.html'
        objs = offers.objects.filter(user=request.user)
        context['ic'] = []
        context['req'] = []
        context['sub'] = []
        context['ft'] = []
        context['cl'] = []
        for i in objs:
            if i.status == 'In Contract':
                context['ic'].append(i)
            if i.status == 'Requested':
                context['req'].append(i)
            if i.status == 'Submitted':
                context['sub'].append(i)
            if i.status == 'Fell Through':
                context['ft'].append(i)
            if i.status == 'Closed':
                context['cl'].append(i)
        context['agentcheck'] = False
    context['offers'] = objs
    return render(request,template,context)

@login_required
def tour(request,id):
    obj = tourrequests()
    obj.user = request.user
    obj.name = request.POST['tourname']
    obj.save()
    obj.relproperty.add(properties.objects.get(pk=id))
    obj.save()
    return redirect('/property-detail/'+str(id))

@login_required
def changeofferstatus(request,id,id2):
    obj = offers.objects.get(pk=id2)
    obj.status = id
    obj.save()
    return redirect('/offers')

@login_required
def profilepage(request,usr):
    if request.user.username == usr:
        return redirect('/')
    if request.method == 'POST':
        obj = User.objects.get(username=usr)
        obj.first_name = request.POST['name']
        obj.email = request.POST['email']
        obj.save()
        print('done')
        obj = profileModel.objects.get(user=obj)
        try:
            obj.contactNumber = request.POST['phone']
        except:
            pass
        obj.occupation = request.POST['occu']
        obj.any_other = request.POST['any_other']
        obj.save()
    template = 'page_471.html'
    objs = profileModel.objects.all()
    obj = None
    for i in objs:
        if i.user.username == usr:
            print(i.user.username)
            obj = i
            print(obj.user.first_name)
            break
    context = {}
    context['agentcheck'] = True
    context['obj'] = obj
    return render(request,template,context)

@login_required
def sharelist(request,usr,id):
    obj = shortlist.objects.get(pk=id)
    a = User.objects.get(username=usr)
    obj.shared_with.add(a)
    obj.save()
    email = EmailMessage(
        subject = request.user.username + ' shared an Interest list',
        body = request.get_host()+'/show-list/'+str(id)+' is the link to the list.',
        to = [a.email]
    )
    email.send()
    return

@login_required
def sharelistbuyer(request,usr,id):
    obj = shortlist.objects.get(pk=id)
    a = User.objects.get(username=usr)
    obj.shared_with.add(a)
    obj.save()
    email = EmailMessage(
        subject = request.user.username + ' shared an Interest list',
        body = request.get_host()+'/show-list/'+str(id)+' is the link to the list.',
        to = [a.email]
    )
    email.send()
    return

@login_required
def unlinklist(request,id):
    obj = shortlist.objects.get(pk=id)
    for i in obj.shared_with.all():
        obj.shared_with.remove(i)
    obj.save()
    return

@login_required
def ratepro(request,listid,proid,rating):
    objl = shortlist.objects.get(pk=listid)
    objp = properties.objects.get(pk=proid)
    for i in propertyrating.objects.all():
        if objl == i.linklist and objp == i.relproperty:
            i.rating = rating
            i.save()
            return

#helping functions
def stripspace(a):
    b = ''
    check = 1
    for i in a:
        if check == 1:
            if i == ' ':
                continue
            elif i == '\n':
                continue
            else:
                check = 2
        if check == 2:
            b = b + i
    return b

def getrating(a,b):
    for i in propertyrating.objects.all():
        if i.linklist == b and i.relproperty == a:
            return i.rating