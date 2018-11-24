from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()
    active_answer = models.ForeignKey('Answer', null=True)

class Answer(models.Model):
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_scores = models.TextField()  # Actually serializes a dictionary of values

class FreeResponse(Answer):
    answer_val = models.CharField(max_length=120)

class MultiChoiceResponse(Answer):
    choice_code = models.CharField(max_length=12)
    choice_val = models.TextField()
