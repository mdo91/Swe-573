from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Courses
from lessons.models import Lessons
from .models import Lessons
from wikidata.models import Wikidata
from django.utils import timezone
from django.db.models.query import QuerySet

@login_required(login_url='signup')
def create_lesson(request):
    cs = Courses.objects
    lss = Lessons.objects
    wiki = Wikidata.objects
    print("????????????????????????count")
    print(cs.count)
    print("???????????Lesson?????????????count")
    print(lss.count)
    print(wiki.count)

    if request.method == 'POST':
        if request.POST['lesson_title'] and request.POST['topic_id']:
            if request.POST['lesson_title']!='' and request.POST['topic_id']!='':

                # try:
                #     print(request.POST['lesson_title'])
                #     print("//////////////////////////mdo")
                #     print(request.POST['topic_id'])
                #     # MARK: get lessons by topic
                #     # topic = Courses.objects.filter(id=request.POST['topic_id'])
                #     lessonsByTopic = Lessons.objects.get(lesson_title=request.POST['lesson_title'],topic_id=request.POST['topic_id'])
                #     print(lessonsByTopic)
                #     return render(request,'create_lesson.html',{'error1':'The lesson title has already been taken, Please Try different Title','topics':lessonsByTopic})
                # except Lessons.DoesNotExist:
                    # get lessons Hierarchy
                    ls = Lessons.objects
                    print("+++++++++++++++++++++")
                    print(ls.count)
                    print("+++++++++++++++++++++ count")
                    topics = Courses.objects.filter(id=request.POST['topic_id'])
                    for topic in topics:
                        lessons_hierarchy = Lessons.objects
                        level_lesson = 1
                        for lesson_hierarchy in lessons_hierarchy.all():
                            if lesson_hierarchy.topic_id_id == topic.id:
                                if level_lesson <= lesson_hierarchy.lesson_hierarchy:
                                    level_lesson = lesson_hierarchy.lesson_hierarchy + 1
                                else:
                                    # do something
                                    print("level is larger")







                    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                    # print(lessons_hierarchy)
                    # level = 1
                    # # check if its the first lesson or not
                    # if  lessons_hierarchy.all().first:
                    #     for lesson_hierarchy in lessons_hierarchy:
                    #         # check if the pointer is less than all lesson_hierarchies
                    #         if level <= lesson_hierarchy.lesson_hierarchy:
                    #             level = lesson_hierarchy.lesson_hierarchy + 1
                    #         else:
                    #             # do something
                    #             print("level is larger")
                    lesson = Lessons()
                    lesson.lesson_title = request.POST['lesson_title']
                    lesson.lesson_hierarchy = level_lesson
                    lesson.topic_id = topic
                    lesson.save()

                    topic = Courses.objects.filter(userId=request.user)
                    lessonsByTopic = Lessons.objects


                    wikidata = Wikidata.objects
                    return render(request,'create_lesson.html', {'error':'Lesson Has been created successfully','topics':topic,'lessons':lessonsByTopic})

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
            # MARK get topics by user
            # MARK get lessons by topic

            topic = Courses.objects.filter(userId=request.user)
            lessonsByTopic = Lessons.objects

            print("//////////////////////////////////////////////////////==")
            print(topic)
            # print(lessonsByTopic)
            print("//////////////////////////////////////////////////////==")
            # wiki_topic_id = topic.id
            # lesson = Lessons.objects

            return render(request,'create_lesson.html',{'topics':topic,'lessons':lessonsByTopic})
        except Courses.DoesNotExist:
            print("does not exit")
            return render(request,'create_lesson.html')


@login_required(login_url='signup')
def edit(request, lesson_id):
    print("lesson to be edited")
# Create your views here.
@login_required(login_url='signup')
def home(request):
    print("home")
