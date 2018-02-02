from django.shortcuts import render, redirect
from .models import Member, Document , Ajax
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def list(request):
    members_list = Member.objects.all()
    paginator = Paginator(members_list, 5)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'members': members})

@login_required
def create(request):
    if request.method == 'POST':
        member = Member(
        firstname=request.POST['firstname'],
        lastname=request.POST['lastname'],
        mobile_number=request.POST['mobile_number'],
        description=request.POST['description'],
        date=request.POST['date'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/list')
    else:
        return render(request, 'add.html')

@login_required    
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)

@login_required
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    mobile_number=request.POST['mobile_number'],
    description=request.POST['description'],
    date=request.POST['date'],
    member.save()
    messages.success(request, 'Member was updated successfully!')
    return redirect('/list')

@login_required
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.error(request, 'Member was deleted successfully!')
    return redirect('/list')

@login_required
def fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        document = Document(
        description=request.POST['description'],
        document=myfile.name, 
        uploaded_at=datetime.datetime.now(),)
        document.save()
        messages.success(request, 'Member was created successfully!')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('fileupload')
    else:
        documents = Document.objects.order_by('-uploaded_at')[:3]
        context = {'documents': documents}
    return render(request, 'fileupload.html', context)

@login_required
def ajax(request):
    if request.method == 'POST':
        if request.is_ajax():
            data = Ajax(
            text=request.POST['text'],
            search=request.POST['search'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), 
            )
            data.save()
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return JsonResponse({'data': 'success'})
    else:
        ajax_list = Ajax.objects.order_by('-created_at')
        context = {'ajax_list': ajax_list}
    return render(request, 'ajax.html',  {'ajax_list': ajax_list})

@csrf_protect
def getajax(request):
    if request.method == 'GET':
        if request.is_ajax():
            data = Ajax.objects.order_by('-created_at').first()
            created = data.created_at.strftime('%m-%d-%Y %H:%M:%S')
            datas = {"id": data.id, "text": data.text, "search": data.search, "email": data.email, "telephone": data.telephone, "created_at": created}
            return JsonResponse(datas)
    else:
        return JsonResponse({'data': 'failure'})
  
@csrf_protect
def ajax_delete(request):
    if request.method == 'GET':
        if request.is_ajax():
            id=request.GET['id']
            ajax = Ajax.objects.get(id=id)
            ajax.delete()
            return JsonResponse({'data': 'success'})
    else:
        return JsonResponse({'data': 'failure'})
  

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
 
def register_success(request):
    return render_to_response(
    'success.html',
    )
 