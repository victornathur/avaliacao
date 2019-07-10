from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {"users":users})


@permission_required("delete_user", login_url="/blog/list/")
@login_required
def delete(request, id):
    user = User.objects.all().get(pk=id).delete()
    messages.success(request, "Sucesso")
    return redirect("/blog/list/")
