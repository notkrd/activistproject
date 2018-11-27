from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.TextField()


class FreeResponseQuestion(Question):
    current_answer = models.ForeignKey('FreeResponse', null=True, on_delete=models.SET_NULL)


class MultiChoiceQuestion(Question):
    current_answer = models.ForeignKey('MultiChoiceResponse', null=True, on_delete=models.SET_NULL)


class PolarQuestion(Question):
    current_answer = models.BooleanField()
    true_score = models.ManyToManyField('DocumentAttrValue', related_name='true_scores')
    false_score = models.ManyToManyField('DocumentAttrValue', related_name='false_scores')


class Answer(models.Model):
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # answer_scores = models.TextField()  # Actually serializes a dictionary of values
    answer_score = models.ManyToManyField('DocumentAttrValue')


class FreeResponse(Answer):
    answer_val = models.CharField(max_length=120)


class MultiChoiceResponse(Answer):
    choice_code = models.CharField(max_length=12)
    choice_val = models.TextField()


class DocumentAttribute(models.Model):
    attribute_name = models.CharField(max_length=100)


class DocumentAttrValue(models.Model):
    attribute_val = models.CharField(max_length=200)
    for_attribute = models.ForeignKey(DocumentAttribute, on_delete=models.CASCADE)
