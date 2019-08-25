from django.shortcuts import render
from .models import *
from django.contrib import messages
from .forms import QuestionForm
from django.shortcuts import redirect


# view for polls/quiz<int:quiz_id>/ which displays all the questions of a particular quiz
def question_view(request, quiz_id):

    # if a user is not authenticated, go to a page which tells the user to log-in
    if (not request.user) or (not request.user.is_authenticated):
        return render(request, "polls/no_user.html")

    # get all the questions of a given quiz
    question = Question.objects.all().filter(quiz=quiz_id)

    # if a user has attempted the first question of the quiz, he must(is enforced) have answered all the questions of the quiz, so send him to the page having aggregate results of the quiz till the current time
    if Question_answer.objects.all().filter(question=question[0].id).filter(user=request.user):
        return redirect("results/")

    # if the user submits the form
    if request.method == "POST":
        # flag is used to check if the user has answered all the questions or not
        flag = 0

        # get the filled form
        form = QuestionForm(quiz_id, request.POST)

        if form.is_valid():
            for q in question:
                q_ans = form.cleaned_data["question"+str(q.id)]

                # if any one of the question is not answered, flag=1
                if not q_ans:
                    # message to be shown to the user
                    messages.success(request, f'Answer all')
                    flag = 1

            # if the user has answered all the questions
            if flag == 0:
                for q in question:
                    # get the answer which can be 1, 2 or 3
                    q_ans = form.cleaned_data["question"+str(q.id)]

                    # save it in Question_answer table
                    q_a = Question_answer.objects.create(
                        question=q, user=request.user, input_answer=q_ans)

                    # to update the number of users who have answered a given option
                    if int(q_ans) == 1:
                        q.option_1_chosen = q.option_1_chosen+1
                    elif int(q_ans) == 2:
                        q.option_2_chosen = q.option_2_chosen+1
                    else:
                        q.option_3_chosen = q.option_3_chosen+1
                    q.save()

                # redirect the user to results page to show the aggregate results till the current time
                return redirect("results/")

    else:
        # create a new form by passing the quiz_id which will return the form having fields of all the questions of the quiz
        # go to polls/forms.py for more details
        form = QuestionForm(quiz_id)

    # list of names of all the form fields to be used when rendering the form
    form_fields = []
    for q in question:
        form_fields.append("question" + str(q.id))
    
    context = {'question': question, 'form': form, 'form_fields': form_fields,
               'title': "Quiz"}
    return render(request, 'polls/quiz.html', context)


# view for polls/quiz<int:quiz_id>/results which shows the aggregate results till the current time
def result_view(request, quiz_id):

    # if a user is not authenticated, go to a page which tells the user to log-in
    if (not request.user) or (not request.user.is_authenticated):
        return render(request, "polls/no_user.html")

    # get all the questions under a given quiz
    question = Question.objects.all().filter(quiz=quiz_id)

    # q_a is a list of dictionary having all the information of the questions of the quiz 
    q_a = []
    for q in question:
        curr = {}
        curr['question'] = q
        curr['answer'] = Question_answer.objects.all().filter(
            question=q).get(user=request.user)
        curr['total'] = len(Question_answer.objects.all().filter(question=q))
        q_a.append(curr)
        
    context = {'q_a': q_a, 'title': "Quiz results"}
    return render(request, "polls/results.html", context)


def quiz_home(request):

    # if a user is not authenticated, go to a page which tells the user to log-in
    if (not request.user) or (not request.user.is_authenticated):
        return render(request, "polls/no_user.html")

    # get all the quiz objects
    quiz = Quiz.objects.all()

    context = {'quiz': quiz, 'title': "Quiz home"}
    return render(request, 'polls/index.html', context)
