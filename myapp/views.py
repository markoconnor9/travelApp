from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.core.validators import validate_email

from .forms import *
# Used to create login page and to recive/validate login credentials 
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
           # print("passed")
            login(request, user)
            print("passed")
          #  print(temp.auto_increment_id)

        else:
             print("failed")
             messages.success(request, ("error"))
    return render(request, 'loginTemplates/login.html', {})

# Used to create new users
def create_account(request):

    if request.method == "POST":
        valid_email = False
        valid_password = False

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["email"]
        password = request.POST["password"]
        try:
            validate_email(username)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            print("good email")
            valid_email = True
        
        if password != "":
            valid_password = True    
    
        if valid_email and valid_password:
            user = User.objects.create_user(username=username, 
                                    password=password, 
                                    is_staff=False,
                                    first_name = first_name,
                                    last_name = last_name)
            user.save()
    form = createUserForm()
    return render(request, 'loginTemplates/createAccount.html', {'form':form})