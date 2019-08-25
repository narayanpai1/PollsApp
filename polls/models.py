from django.db import models
from django.contrib.auth.models import User


# Model to store the quiz which will include many Question
class Quiz(models.Model):
    name = models.CharField(max_length=100)

    # printing any object will show the returned string
    def __str__(self):
        return str(self.name)


# Model to store each question
class Question(models.Model):
    question_text = models.TextField(null=True, blank=True)

    option_1 = models.TextField(null=True, blank=True)
    # Number of people who have chosen option 1
    option_1_chosen = models.IntegerField()

    option_2 = models.TextField(null=True, blank=True)
    option_2_chosen = models.IntegerField()

    option_3 = models.TextField(null=True, blank=True)
    option_3_chosen = models.IntegerField()

    # Each question belongs to a certain quiz
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE,)

    # printing any object will show the returned string
    def __str__(self):
        return self.question_text


# Model to store the information of each input poll answer which will belong to a particular quiz and which is being answered by a particular user
class Question_answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Answer can be 1,2 or 3
    MY_CHOICES = ((1, 'option_1'), (2, 'option_2'), (3, 'option_3'))
    input_answer = models.IntegerField(choices=MY_CHOICES, default=1)

    # printing any object will show the returned string
    def __str__(self):
        return str(self.question.id) + " " + str(self.user)
