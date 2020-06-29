from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def hello(request):
    return HttpResponse('打开浏览器')



def index(request):
    # 本质上返回的也是HttpResopnse
    return render(request,"index.html")

def get_students(request):
    students = Student.objects.all()
    student_dict = {
        "hobby":"coding",
        "time":"one year",

    }
    code = '''
    <h2>睡着了</2>
    <script type="text/javascript">
        alter('你的网站被攻陷了!');
    </script>
    '''
    data = {
        'students':students,
        "student_dict":student_dict,
        "count": 10,
        "code":code,
    }
    return render (request,"students.html",context= data)


def temp(request):

    return render(request,'home.html',context={"title":"home"})


def home(request):
    return render(request, 'home_mine.html')