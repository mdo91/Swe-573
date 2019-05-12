from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Courses
from wikidata.models import Wikidata
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
                if request.POST.get('checkbox0'):
                    print("checkBOX 1 is true/////////////////////////////////////")
                if request.POST['textvalue0']:
                    print("textvalue0  is true/////////////////////////////////////")


                # MARK: GET wiki data
                print("checking/////////////////////////////////////")
                if request.POST.get('checkbox0') and request.POST['urlValue0'] and request.POST['textvalue0']:
                     print("first value is checked/////////////////////////////////////")
                     # //check if checkbox is checked or if value is true/flase or if 0/1
                     wikidata = Wikidata.objects.create(wikiTitle=request.POST['textvalue0'],wikiLink=request.POST['urlValue0'],topic_id=topic)
                     wikidata.save()
                     # topic_id = Courses.objects.latest('id')

                if request.POST.get('checkbox1') and request.POST['urlValue1'] and request.POST.get('textvalue1',False):
                     wikidata = Wikidata.objects.create(wikiTitle=request.POST['textvalue1'],wikiLink=request.POST['urlValue1'],topic_id=topic)
                     wikidata.save()
                if request.POST.get('checkbox2') and request.POST['urlValue2'] and request.POST.get('textvalue2',False):
                      wikidata = Wikidata.objects.create(wikiTitle=request.POST['textvalue2'],wikiLink=request.POST['urlValue2'],topic_id=topic)
                      wikidata.save()
                if request.POST.get('checkbox3') and request.POST['urlValue3'] and request.POST['textvalue3']:
                     wikidata = Wikidata.objects.create(wikiTitle=request.POST['textvalue3'],wikiLink=request.POST['urlValue3'],topic_id=topic)
                     wikidata.save()
                if request.POST.get('checkbox4') and request.POST['urlValue4'] and request.POST['textvalue4']:
                      wikidata = Wikidata.objects.create(wikiTitle=request.POST['textvalue4'],wikiLink=request.POST['urlValue4'],topic_id=topic)
                      wikidata.save()

                topicsByUser = Courses.objects.filter(userId=request.user)
                wikidata = Wikidata.objects.filter(topic_id=topic.id)
                return render(request,'create.html', {'error':'Topic Has been created successfully','topics':topicsByUser,'wikidata':wikidata})

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
            print("//////////////////////////////////////////////////////==")
            print(topic)
            print("//////////////////////////////////////////////////////==")
            # wiki_topic_id = topic.id
            wikidata = Wikidata.objects

            print("does exit")
            print(topic)
            return render(request,'create.html',{'topics':topic,'wikidata':wikidata})
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
