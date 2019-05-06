from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Courses
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request,'home.html'
    )
@login_required(login_url='signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description']:

            try:
                topic = Courses.objects.get(topicTitle=request.POST['title'])
                topicsByUser = Courses.objects.filter(userId=request.user)
                return render(request,'create.html',{'error1':'The topic title has already been taken, Please Try different Title','topics':topicsByUser})
            except Courses.DoesNotExist:
                topic = Courses()
                topic.topicTitle = request.POST['title']
                topic.description = request.POST['description']
                topic.userId = request.user
                topic.save()
                topicsByUser = Courses.objects.filter(userId=request.user)
                return render(request,'create.html', {'error':'Topic Has been created successfully','topics':topicsByUser})

            # if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            #     prod.url = request.POST['url']
            # else:
            #     prod.url = 'http://' + request.POST['url']

            # prod.icon = request.FILES['icon']
            # prod.image = request.FILES['image']
            # prod.pub_date = timezone.datetime.now()
            # prod.votes_total = 1

    else:
        # user = User.objects.get(username = request.POST['username'])
        try:
            topic = Courses.objects.filter(userId=request.user)

            print("does exit")
            print(topic)
            return render(request,'create.html',{'topics':topic})
        except Courses.DoesNotExist:
            print("does not exit")
            return render(request,'create.html')

@login_required(login_url='signup')
def edit(request,topic_id):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description']:
            if request.POST['title'] !='' and request.POST['description'] !='':
                topics = get_object_or_404(Courses, pk=topic_id )
                topics.topicTitle = request.POST['title']
                topics.description = request.POST['description']
                topics.save()
                topicsByUser = Courses.objects.filter(userId=request.user)
                return render(request,'create.html',{'error':'The topic has been edited successfully','topics':topicsByUser})
            else:
                 topics = get_object_or_404(Courses, pk=topic_id )
                 topicsByUser = Courses.objects.filter(userId=request.user)
                 return render(request,'create.html',{'topics':topicsByUser,'topicEdit':topics})



                    # topicsByUser = Courses.objects.filter(userId=request.user)
                #TODO: next line has to be fixed
        else:
             print('not post requset')
             topics = get_object_or_404(Courses, pk=topic_id )
             topicsByUser = Courses.objects.filter(userId=request.user)
             return render(request,'create.html',{'topics':topicsByUser,'topicEdit':topics})
    else:
        print('not post requset2')
        topics = get_object_or_404(Courses, pk=topic_id )
        #print(topics.topicTitle)
        topicsByUser = Courses.objects.filter(userId=request.user)
        return render(request,'create.html',{'topics':topicsByUser,'topicEdit':topics})










# def detail(request, product_id):
#     product_de = get_object_or_404(product, pk=product_id)
#     return render(request,'detail.html',{'product':product_de})
#
# @login_required(login_url='signup')
# def upvote(request,product_id):
#     if request.method == 'POST':
#         product_de = get_object_or_404(product, pk=product_id)
#         product_de.votes_total += 1
#         product_de.save()
#         return redirect('/product/' + str(product_de.id))
