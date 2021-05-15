from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, ImageUpload,AddProject
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import  HttpResponse
from django.shortcuts import redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random

def getRandom():
    return random.randint(1000, 9999)

def display_projects(request):
    opt = 0


    projects = Project.objects.all()
    project_list = []
    for project in projects:
        tmp_dict ={}
        tmp_dict['id'] = project.id
        tmp_dict['name'] = project.name
        tmp_dict['tagline'] = project.tag_line
        tmp_dict['photo'] = project.photo
        project_list.append(tmp_dict)

    params = {'projects' : project_list,'opt': opt}
    if request.user.is_authenticated:
        params['my_template'] = 'basic2.html'
        student = Student.objects.get(username=request.user)
        params['profile'] = student.photo
    else:
        params['my_template'] = 'basic.html'
    # for p in params['projects']:
    #     print(p)
    return render(request,"DisplayProjects.html",params)

def homepage(request):
    params = {}
    if request.user.is_authenticated:
        params['my_template'] = 'basic2.html'
        student = Student.objects.get(username = request.user)
        params['profile'] = student.photo
        # print(params)
    else:
        params['my_template'] = 'basic.html'

    return render(request,'Homepage.html',params)


def single_project(request,id,slug):
    print(id)
    project = Project.objects.get(id = id)

    project_info = {}
    project_info['name'] = project.name.capitalize()
    project_info['tag_line'] = project.tag_line
    project_info['photo'] = project.photo
    project_info['year'] = project.year
    project_info['domain'] = project.domain
    project_info['guide'] =project.guide
    project_info['inspiration'] = project.inspiration
    project_info['what_it_does'] = project.what_it_does
    project_info['how_we_build'] = project.how_we_build
    project_info['challenges'] = project.challenges
    project_info['accomplishment'] = project.accomplishment
    project_info['we_learned'] = project.we_learned
    project_info['whats_next'] = project.whats_next
    # print(project_info)
    params = {'project' : project_info}
    if request.user.is_authenticated:
        params['my_template'] = 'basic2.html'
        student = Student.objects.get(username=request.user)
        params['profile'] = student.photo
    else:
        params['my_template'] = 'basic.html'
    return render(request,'Project.html',params)

# def login(request):
#     if request.method == 'POST':
#         return HttpResponse("Post")
#     return HttpResponse("Gandal")

def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully !!')
            fm.save()
            email = fm.cleaned_data['email']
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password1']
            first_name = fm.cleaned_data['first_name']
            last_name = fm.cleaned_data['last_name']
            # print(email,username,password,first_name,last_name)
            student = Student(username = username,name = first_name+" "+last_name, mail = email, password = password)
            student.save()
    else:
        fm=SignUpForm()

    return render(request,'signup1.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    student = Student.objects.get(username=uname)
                    # print(student.username)
                    # print(student.verified)
                    login(request, user)
                    messages.success(request,'Logged in successfully !!')
                    if(student.verified==False):
                        # updting otp
                        Student.objects.filter(username = uname).update(otp = getRandom())
                        return HttpResponseRedirect('/verification/')
                    else:
                        # return redirect(request.META['HTTP_REFERER'])
                        return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        #fm=AuthenticationForm()
        return render(request,'StuLogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def stu_verification(request):
    if request.user.is_authenticated:

        student = Student.objects.get(username=request.user)

        subject = 'Account Verification'
        message = f'Hi ,Your OTP for verification is {student.otp}'
        email_from = 'medicatorvs@gmail.com'
        recipient_list = [str(request.user.email), ]
        send_mail(subject, message, email_from, recipient_list)
        print(student.otp)
        return render(request,'verification.html',{'name':request.user,'email':request.user.email,'msg':None})
    else:
        return HttpResponseRedirect('/login/')

def verify_otp(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            otp = request.POST.get('otp')
            # print(otp)
            student = Student.objects.get(username = request.user)

            if(str(student.otp) == otp):
                # print("Jamal")
                Student.objects.filter(username = request.user).update(verified = True)
                return HttpResponseRedirect('/profile/')
            else:
                return render(request,'verification.html',{'name':request.user,'email':request.user.email,'msg':"Entered Wrong OTP ,please enter correct OTP"})
    else:
        return HttpResponseRedirect('/login/')

def user_profile(request):
    if request.user.is_authenticated:
         student = Student.objects.get(username=request.user)
         if (student.verified == False):
             Student.objects.filter(username=request.user).update(otp=getRandom())
             return HttpResponseRedirect('/verification/')

         return render(request,'profile.html',{'name':request.user,'profile':student.photo})
    else:
        return HttpResponseRedirect('/login/')



def settings(request):
    params = {}
    if request.method == 'POST':
        image_upload = ImageUpload(request.POST,request.FILES)
        if image_upload.is_valid():
            image_upload.save()
            photo = image_upload.cleaned_data['photo']
            print(photo)
            photo = '/media/tmp/' + str(photo)
            Student.objects.filter(username = request.user).update(photo = photo)
        else:
            image_upload = ImageUpload()

    if request.user.is_authenticated:
        params['my_template'] = 'basic2.html'
        student = Student.objects.get(username = request.user)
        name = student.name
        li = name.split()
        first_name = li[0]
        last_name = li[1]
        params['profile'] = student.photo
        params['first_name'] = first_name
        params['last_name'] = last_name
        params['github'] = student.github
        params['linkedin'] = student.linked_in
        params['form'] = image_upload


        # print(params)
    else:
        return HttpResponseRedirect('/login/')

    return render(request,'Settings.html',params)

def save_changes(request):
    params = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            pic = request.POST.get('profile')
            print('pic: ',pic)
            name = request.POST.get('first_name')
            name += " " + request.POST.get('last_name')
            github = request.POST.get('github')
            linkedin = request.POST.get('linkedin')
            Student.objects.filter(username=request.user).update(name = name, github = github, linked_in = linkedin)
            return HttpResponseRedirect('/settings/')
        # print(params)
    else:
        return HttpResponseRedirect('/login/')

    return render(request, 'Settings.html', params)

def portfolio(request):
    params = {}
    if request.user.is_authenticated:
        params['my_template'] = 'basic2.html'
        student = Student.objects.get(username=request.user)
        projects = Project.objects.filter(project_student__student_id=student)
        # print(projects)
        project_list = []
        for project in projects:
            dict = {}

            # print(p)
            dict['id'] = project.id
            dict['photo'] = project.photo
            dict['name'] = project.name
            dict['tag_line'] = project.tag_line
            project_list.append(dict)

        params['projects'] = project_list
        if student.photo:
            params['profile'] = student.photo
        else:
            params['profile'] = "../media/Profile1.jpg"
        params['name'] = student.name
        params['username'] = student.username
        params['len'] = len(projects)
        # print(params)
    else:
        return HttpResponseRedirect('/login/')



    return render(request, 'Portfolio.html', params)


def add_project(request):
    if request.method=="POST":
        fm=AddProject(request.POST,request.FILES)
        if fm.is_valid():
            messages.success(request,'Successfully Added')
            fm.save()
            student = Student.objects.get(username=request.user)
            # s_id = student.id
            project = Project.objects.filter(name = fm.cleaned_data['name'], tag_line = fm.cleaned_data['tag_line'])[0]
            # p_id = project.id
            pro = Project_Student(project_id=project, student_id=student)
            pro.save()

            return HttpResponseRedirect('/portfolio/')

    else:
        messages.success(request, 'Error !!')
        fm=AddProject()
        # return HttpResponseRedirect('/settings/')

    params = {}
    if request.user.is_authenticated:
        params['my_template'] = 'basic2.html'
        student = Student.objects.get(username=request.user)
        params['profile'] = student.photo
        params['name'] = student.name
        params['username'] = student.username
        params['form'] = fm
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'Addproject.html',params)
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    #
    # fm=AddProject(request.POST)
    #
    # if request.method == "POST":
    #     fm = AddProject(request.POST)
    #     if fm.is_valid():
    #         messages.success(request, 'Account Created Successfully !!')
    #         fm.save()
    #         return HttpResponse("Success")
    #
    # else:
    #     return HttpResponse("Failure")
    #     fm = AddProject()
    # if fm.is_valid():
    #     messages.success(request,'Account Created Successfully !!')
    #     fm.save()
    #     return HttpResponse("Success")
    # else:
    #     return HttpResponse("Failure")


    return render(request,'signup.html',{'form':fm})
    # #pass
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    # fm = AddProject(request.POST)
    # if fm.is_valid():
    #     messages.success(request, 'Added Successfully !!')
    #     fm.save()
    #     return HttpResponseRedirect('/portfolio/')
    # # if request.method=="POST":
    # #
    # #
    # #         # student = Student.objects.get(username = request.user)
    # #         # s_id = student.id
    # #         # project_name = Project.objects.get(name = fm.cleaned_data['name'])
    # #         # p_id = project_name.id
    # #         # pro = Project_Student(project_id = p_id, student_id = s_id)
    # #         #
    # #         # pro.save()
    #
    # else:
    #     print("Gandal")
    #     fm = AddProject()
    #
    # params = {}
    # project = AddProject(request.POST)
    # params['my_template'] = 'basic2.html'
    # student = Student.objects.get(username=request.user)
    # params['profile'] = student.photo
    # params['form'] = project
    #
    # return render(request,'Addproject.html',params)



    # params = {}
    # project = AddProject(request.POST)
    # params['my_template'] = 'basic2.html'
    # student = Student.objects.get(username = request.user)
    # params['profile'] = student.photo
    # params['form'] = project

    # if project.is_valid():
    #     return HttpResponseRedirect('/settings/')
    # if request.method == 'POST':
    #     print("post")
    # return render(request, 'Addproject.html', params)
    # if request.method == 'POST':
    #     project = AddProject(request.POST)
    #     params = {}
    #
    #     params['my_template'] = 'basic2.html'
    #     student = Student.objects.get(username = request.user)
    #     params['profile'] = student.photo
    #     params['form'] = project
    #
    #
    #     if project.is_valid():
    #         print('project',project)
    #         project.save()
    #         student = Student.objects.get(username = request.user)
    #         s_id = student.id
    #         project_name = Project.objects.get(name = project.cleaned_data['name'])
    #         p_id = project_name.id
    #         pro = Project_Student(project_id = p_id, student_id = s_id)
    #
    #         pro.save()
    #         return HttpResponseRedirect('/portfolio/')
    #     else:
    #         print('not valid')
    #
    #
    #
    #     # print(params)
    # else:
    #     return HttpResponseRedirect('/login/')
    #
    # return render(request,'Addproject.html',params)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


