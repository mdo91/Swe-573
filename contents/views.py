from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from courses.models import Courses
from lessons.models import Lessons
from .models import Lessons
from contents.models import Contents
from .models import Contents
from django.utils import timezone
from django.db.models.query import QuerySet

@login_required(login_url='signup')
def create_content(request):
    print("=================== create_content=============================")


    if request.method == 'POST':
        if request.POST['lesson_id'] and request.POST['content'] and request.POST['material_title']:
            print("--------------------data------------------")
            print(request.POST['lesson_id'])
            print(request.POST['content'])
            print(request.POST['material_title'])


            if request.POST['lesson_id']!='' and request.POST['content']!='' and request.POST['material_title']!='':



                # ls = Lessons.objects

                lessons = Lessons.objects.filter(id=request.POST['lesson_id'])
                print("----------------------------------------------------")
                print(lessons)
                contents = Contents.objects.create(content=request.POST['content'],lessonId_id=request.POST['lesson_id'],material_title=request.POST['material_title'])
                # for lesson in lessons:
                #     content = Contents()
                #     content.material_title = request.POST['material_title']
                #     content.content = request.POST['content']
                #     content.lessonId_id = lesson.id
                #     content.save()





                print("=======================")
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
                contentsByLesson = []

                contents = Contents.objects
                for contentbylesson in lessonsByUser:
                    print("//////////////////////////////////////////////////////==contentbylesson avalaible11")
                    for content in contents.all():
                        print("//////////////////////////////////////////////////////==content avalaible22")
                        if content.lessonId_id == contentbylesson.id:


                            contentsByLesson.append(content)
                            # lastlesson.append(contentbylesson)
                            print("//////////////////////////////////////////////////////==contentsbyLesson avalaible33")

                # wiki_topic_id = topic.id
                # lesson = Lessons.objects
                print(contentsByLesson)
                lastlesson = lessonsByUser[-1]
                # lastlesson
                print("last lesson=====================")
                print(lastlesson)

                return render(request,'contents_create.html',{'lessons':lessonsByTopic,'ls':lessonsByUser,'contentsbylesson':contentsByLesson,'lastlesson':lastlesson})

            else:
                print("not all Available else statement3")
                topic = Courses.objects.filter(userId=request.user)
                materialsbylesson = Lessons.objects


                wikidata = Wikidata.objects
                return render(request,'contents_create.html', {'error':'Lesson Has been created successfully','topics':topic,'lessons':materialsbylesson})
        else:

            print("not all Available else statement2")
            print(request.POST['content'])
            topic = Courses.objects.filter(userId=request.user)
            materialsbylesson = Lessons.objects


            wikidata = Wikidata.objects
            return render(request,'contents_create.html', {'error1':'some inserted data is missing','topics':topic,'lessons':materialsbylesson})


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
            contentsByLesson = []

            contents = Contents.objects
            for contentbylesson in lessonsByUser:
                print("//////////////////////////////////////////////////////==contentbylesson avalaible11")
                for content in contents.all():
                    print("//////////////////////////////////////////////////////==content avalaible22")
                    if content.lessonId_id == contentbylesson.id:


                        contentsByLesson.append(content)
                        # lastlesson.append(contentbylesson)
                        print("//////////////////////////////////////////////////////==contentsbyLesson avalaible33")

            # wiki_topic_id = topic.id
            # lesson = Lessons.objects
            print(contentsByLesson)
            lastlesson = lessonsByUser[-1]
            # lastlesson
            print("last lesson=====================")
            print(lastlesson)

            return render(request,'contents_create.html',{'lessons':lessonsByTopic,'ls':lessonsByUser,'contentsbylesson':contentsByLesson,'lastlesson':lastlesson})
        except Courses.DoesNotExist:
            print("except post request")
            print("does not exit")
            return render(request,'contents_create.html')




@login_required(login_url='signup')
def edit(request, lesson_id):
    return render(request,'create_content.html')
# Create your views here.
