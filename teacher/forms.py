from django import forms

<<<<<<< HEAD
from .models import Course, MultipleChoiceQuestion
=======
from .models import Course
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("course_title", "course_description", "cover_image", "course_video", "course_assessment")
<<<<<<< HEAD
        
        
class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'correct_answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3}),
        }
        
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['course', 'text']

# class ChoiceForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = ['question', 'text', 'is_correct']

# class QuizForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         questions = kwargs.pop('questions')
#         super(QuizForm, self).__init__(*args, **kwargs)
#         for question in questions:
#             choices = [(choice.id, choice.text) for choice in question.choices.all()]
#             self.fields[f'question_{question.id}'] = forms.ChoiceField(
#                 choices=choices, widget=forms.RadioSelect, label=question.text)
=======
        
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
