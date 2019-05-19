from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from courses.models import Courses
from lessons.models import Lessons
from .models import Lessons
from .models import Materials
from materials.models import Materials
from wikidata.models import Wikidata
from django.utils import timezone
from django.db.models.query import QuerySet

@login_required(login_url='signup')
def create_content(request):
    print("=================== create_content=============================")


    if request.method == 'POST':
        if request.POST['lesson_id'] and request.POST['content'] and request.POST['material_title']:
            print("===========================================all Available")
            if request.POST['lesson_id']!='' and request.POST['content']!='' and request.POST['material_title']!='':

                print("============================== all Available and not empty")
                print(request.POST['lesson_id'])
                print(request.POST['content'])
                print(request.POST['material_title'])
                ls = Lessons.objects
                print("+++++++++++++++++++++")
                print(ls.count)
                print("+++++++++++++++++++++ count")
                lessons = Lessons.objects.filter(id=request.POST['lesson_id'])
                # material = Materials()
                # material.content = "test"
                # material.lesson_id_id = lessons
            #    material.material_title = "test"

                material = Materials.objects.create(content=request.POST['content'],lesson_id_id=lessons,material_title=request.POST['material_title'])
                # wikidata.save()
                material.save()
                print("=======================")


                topic = Courses.objects.filter(userId=request.user)
                materialsbylesson = Lessons.objects



                return render(request,'create_content.html', {'error':'Lesson Has been created successfully','topics':topic,'lessons':materialsbylesson})

            else:
                print("not all Available else statement3")
                topic = Courses.objects.filter(userId=request.user)
                materialsbylesson = Lessons.objects


                wikidata = Wikidata.objects
                return render(request,'create_content.html', {'error':'Lesson Has been created successfully','topics':topic,'lessons':materialsbylesson})
        else:

            print("not all Available else statement2")
            print(request.POST['content'])
            topic = Courses.objects.filter(userId=request.user)
            materialsbylesson = Lessons.objects


            wikidata = Wikidata.objects
            return render(request,'create_content.html', {'error1':'some inserted data is missing','topics':topic,'lessons':materialsbylesson})


    else:
        # user = User.objects.get(username = request.POST['username'])
        try:
            # MARK get topics by user
            # MARK get lessons by topic
            print("==================================not post request")

            topic = Courses.objects.filter(userId=request.user)
            lessonsByTopic = Lessons.objects
            lessonsByUser = []
            for topicls in topic:
                lessons_hierarchy = Lessons.objects
                level_lesson = 1
                for lesson_hierarchy in lessons_hierarchy.all():
                    if lesson_hierarchy.topic_id_id == topicls.id:
                        lessonsByUser.append(lesson_hierarchy)

            print("//////////////////////////////////////////////////////==")
            print(topic)
            print(lessonsByUser)
            # print(lessonsByTopic)
            print("//////////////////////////////////////////////////////==")
            # wiki_topic_id = topic.id
            # lesson = Lessons.objects
            # get contents
            contentsByLesson = []
            contents = Contents.objects
            for contentbylesson in lessonsByUser:
                for content in contents:
                    if content.lessonId_id == contentbylesson.id:
                        contentsbyLesson = content




            return render(request,'create_content.html',{'topics':topic,'lessons':lessonsByTopic,'ls':lessonsByUser,'contentsbylesson':contentsbyLesson})
        except Courses.DoesNotExist:
            print("except post request")
            print("does not exit")
            return render(request,'create_content.html')




@login_required(login_url='signup')
def edit(request, lesson_id):
    return render(request,'create_content.html')
# Create your views here.
