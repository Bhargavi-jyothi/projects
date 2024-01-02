import re
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import UserRegistrationModel
import pandas as pd
import csv
from .utility import preprocess



# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, 'Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

def UserHome(request):
    return render(request,'users/UserHome.html', {})

def Userdata(request):
    import os
    from django.conf import settings
    path = os.path.join(settings.MEDIA_ROOT, "dataset.csv")
    df = pd.read_csv(path)
    df = df.to_html(index=False)
    return render(request,'users/userviewdata.html',{"data":df})


def user_machine_learning(request):
    rf,rf_acc = preprocess.process_RandomForest()
    mlp, mlp_acc = preprocess.MLP()
    c45, c45_acc = preprocess.C45()

    return render(request ,"users/machinlearning.html",{"rf":rf,"rf_acc": rf_acc,"mlp": mlp,"mlp_acc": mlp_acc, "c45": c45,"c45_acc": c45_acc})

def rbf_kernel(request):
    rbf, rbf_acc = preprocess.process_rbf_kernel()
    return render(request, 'users/rbf.html', {"rbf": rbf,"rbf_acc":rbf_acc})

def hybrid(request):
    rbf, rbf_acc = preprocess.process_rbf_kernel()
    mlp, mlp_acc = preprocess.MLP()
    c45, c45_acc = preprocess.C45()
    rf,rf_acc = preprocess.process_RandomForest()
    print(rbf_acc, mlp_acc, c45_acc, rf_acc)
    hyb1 = (rbf_acc+mlp_acc)/2
    hyb2 = (c45_acc+rf_acc)/2
    return render(request, 'users/hybrid.html', {"hyb1": hyb1,"hyb2":hyb2})





    

def get_grade_id(GradeID):
    if GradeID=="GradeID_G-02":
        grade_id = [1,0,0,0,0,0,0,0,0,0]
    elif GradeID == "GradeID_G-04":
        grade_id = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif GradeID == "GradeID_G-05":
        grade_id = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif GradeID == "GradeID_G-06":
        grade_id = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif GradeID == "GradeID_G-07":
        grade_id = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif GradeID == "GradeID_G-08":
        grade_id = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif GradeID == "GradeID_G-09":
        grade_id = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif GradeID == "GradeID_G-10":
        grade_id = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif GradeID == "GradeID_G-11":
        grade_id = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    else:
        grade_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    return  grade_id

def prediction_form(request):
    if request.method == 'POST':
        gender = int(request.POST.get('Gender'))
        raisehands = int(request.POST.get('raisehands'))
        VisITedResources = int(request.POST.get('VisITedResources'))
        AnnouncementsView = int(request.POST.get('AnnouncementsView'))
        Discussion = int(request.POST.get('Discussion'))

        StageID = request.POST.get('StageID')
        GradeID = request.POST.get('GradeID')
        ParentAnswering = request.POST.get('ParentAnswering')
        ParentschoolSatisfaction = request.POST.get("ParentschoolSatisfaction")
        StudentAbsenceDays = request.POST.get("StudentAbsenceDays")

        if StageID=='StageID_HighSchool':
            stage_id = [1,0,0]
        elif StageID=="StageID_MiddleSchool":
            stage_id = [0,1,0]
        else:
            stage_id = [0,0,1]

        grade_id = get_grade_id(GradeID)

        if ParentAnswering=="ParentAnsweringSurvey_No":
            parent_ans = [1,0]
        else:
            parent_ans = [0,1]
        if ParentschoolSatisfaction =="ParentschoolSatisfaction_Bad":
            parent_satis = [0,1]
        else:
            parent_satis = [1,0]
        if StudentAbsenceDays=="StudentAbsenceDays_Above-7":
            std_abs = [1,0]
        else:
            std_abs = [0,1]

        test_set = [gender,raisehands,VisITedResources,AnnouncementsView,Discussion]
        test_set.extend(stage_id)
        test_set.extend(grade_id)
        test_set.extend(parent_ans)
        test_set.extend(parent_satis)
        test_set.extend(std_abs)
        result = preprocess.process_browserInput(test_set)
        print("Result is:",result)
        if result[0][0]==1:
            msg = "High"
        elif result[0][1]==1:
            msg = "Low"
        else:
            msg = "Medium"
        return render(request, "users/adddata.html", {"msg": msg})
    else:
        return render(request, "users/adddata.html", {})
