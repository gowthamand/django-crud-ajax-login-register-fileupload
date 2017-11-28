from django.shortcuts import render, redirect
from .models import Member, Document, Ajax
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from crud.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string



@login_required
def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

@login_required
def create(request):
    member = Member(
    firstname=request.POST['firstname'],
    lastname=request.POST['lastname'],
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),)
    member.save()
    messages.success(request, 'Member was created successfully!')
    return redirect('/')

@login_required    
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

@login_required
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    messages.warning(request, 'Member was updated successfully!')
    return redirect('/')

@login_required
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.info(request, 'Member was deleted successfully!')
    return redirect('/')

@login_required
def fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        document = Document(
        description=request.POST['description'],
        document=(myfile.name, myfile),
        uploaded_at=datetime.datetime.now(),)
        document.save()
        messages.success(request, 'Member was created successfully!')
        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('fileupload')

    return render(request, 'crud/fileupload.html')

@login_required
def signup(request):
    
    return render(request, 'crud/signup.html')

@login_required
def ajax(request):
    if request.method == 'POST':
        if request.is_ajax():
            print "**ajax post**"
            print (request.POST['telephone'])
            data = Ajax(
            text=request.POST['text'],
            search=request.POST['search'],
            email=request.POST['email'],
            url=request.POST['url'],
            telephone=request.POST['telephone'],
            password=request.POST['password'],
            number=request.POST['number'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), 
            )
            data.save()
            print(data)
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return JsonResponse({'data': astr})
    return JsonResponse({'data':'bar'})


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
    return render(request, 'crud/register.html', {'form': form})
 
def register_success(request):
    return render_to_response(
    'crud/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )