from .models import Question, Quiz
from django import forms


# form for questions of given quiz used in question_view view
class QuestionForm(forms.Form):

    def __init__(self, quiz_id, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        all_questions = Question.objects.all().filter(quiz=quiz_id)

        # for each question, there is one choicefield in the form which can be 1, 2 or 3
        for question in all_questions:

            # get the option-text to be displayed for each option
            MY_CHOICES = (
                (1, str(question.option_1)), (2, str(question.option_2)), (3, str(question.option_3)))

            self.fields['question' + str(question.id)
                        ] = forms.ChoiceField(choices=MY_CHOICES)
