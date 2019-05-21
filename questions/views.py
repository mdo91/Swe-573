from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from courses.models import Courses
from lessons.models import Lessons
from questions.models import Questions
from options.models import Options
# from .models import Lessons
from contents.models import Contents
from .models import Contents
from django.utils import timezone
from django.db.models.query import QuerySet

@login_required(login_url='signup')
def create_question(request):
    print("=================== create_content=============================")


    if request.method == 'POST':
        if request.POST['material_id'] and request.POST['question']:
            print("--------------------data------------------")
            print(request.POST['material_id'])
            print(request.POST['question'])




            if request.POST['material_id']!='' and request.POST['question']!='':
                question = Questions()
                question.question_text = request.POST['question']
                question.materialId_id = request.POST['material_id']
                question.save()
                print("///////////////////////////////////@@@@@")
                print(question.id)
                # question = Question.objects.create(question_text=request.POST['question'],materialId_id=request.POST['material_id'])
                if request.POST['option1']!='' and request.POST['answer1']!='':
                     print("=======================STORING1")
                     option = Options.objects.create(optionText=request.POST['option1'],answer=request.POST['answer1'],questionId_id=question.id)

                if request.POST['option2']!='' and request.POST['answer2']!='':
                     option = Options.objects.create(optionText=request.POST['option2'],answer=request.POST['answer2'],questionId_id=question.id)
                     print("=======================STORING2")
                if request.POST['option3']!='' and request.POST['answer3']!='':
                    print("=======================STORING3")
                    option = Options.objects.create(optionText=request.POST['option3'],answer=request.POST['answer3'],questionId_id=question.id)
                if request.POST['option4']!='' and request.POST['answer4']!='':
                    option = Options.objects.create(optionText=request.POST['option4'],answer=request.POST['answer4'],questionId_id=question.id)
                    print("=======================STORING4")





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
                if contentsByLesson:
                    lastcontent = contentsByLesson[-1]
                else:
                    lastcontent = contentsByLesson


                # lastlesson
                print("last lesson=====================")
                # print(lastlesson)

                return render(request,'create_question.html',{'lessons':lessonsByTopic,'ls':lessonsByUser,'contentsbylesson':contentsByLesson,'lastcontent':lastcontent})

            else:
                print("not all Available else statement3")
                topic = Courses.objects.filter(userId=request.user)
                materialsbylesson = Lessons.objects


                # wikidata = Wikidata.objects
                return render(request,'create_question.html', {'error':'Lesson Has been created successfully','topics':topic,'lessons':materialsbylesson})
        else:

            print("not all Available else statement2")

            topic = Courses.objects.filter(userId=request.user)
            materialsbylesson = Lessons.objects



            return render(request,'create_question.html', {'error1':'some inserted data is missing','topics':topic,'lessons':materialsbylesson})


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
            questionsbycontent = []
            optionsbyquestion = []

            contents = Contents.objects
            questions = Questions.objects
            options = Options.objects
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
            if contentsByLesson:
                lastcontent = contentsByLesson[-1]
            else:
                lastcontent = contentsByLesson
            # lastlesson
            print("last lesson=====================")
            for question in questions.all():
                for material in contentsByLesson:
                    if material.id == question.materialId_id:
                        questionsbycontent.append(question)
                        print("# QUESTION: appending=====================")


            # print(lastlesson)
            print("# QUESTION:=====================")
            print(questionsbycontent)
            for option in options.all():
                for q in questionsbycontent:
                    if option.questionId_id == q.id:
                        optionsbyquestion.append(option)


            return render(request,'create_question.html',{'lessons':lessonsByTopic,'ls':lessonsByUser,'contentsbylesson':contentsByLesson,'lastcontent':lastcontent,'questions':questionsbycontent,'options':optionsbyquestion})
        except Courses.DoesNotExist:
            print("except post request")
            print("does not exit")
            return render(request,'create_question.html')




@login_required(login_url='signup')
def edit(request, lesson_id):
    return render(request,'create_content.html')
# Create your views here.
