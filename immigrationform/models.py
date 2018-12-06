from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class FreeResponseQuestion(Question):
    pass


class MultiChoiceQuestion(Question):
    pass


class PolarQuestion(Question):
    true_score = models.ManyToManyField('DocumentAttrValue', related_name='true_scores')
    false_score = models.ManyToManyField('DocumentAttrValue', related_name='false_scores')


class Answer(models.Model):
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # answer_scores = models.TextField()  # Actually serializes a dictionary of values
    answer_score = models.ManyToManyField('DocumentAttrValue')


class FreeResponse(Answer):
    answer_val = models.CharField(max_length=120)

    def __str__(self):
        return self.answer_val


class MultiChoiceResponse(Answer):
    answer_val = models.TextField(default='')

    def __str__(self):
        return self.answer_val


class PolarResponse(Answer):
    answer_val = models.BooleanField


class DocumentAttribute(models.Model):
    attribute_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name


class DocumentAttrValue(models.Model):
    attribute_val = models.CharField(max_length=200)
    for_attribute = models.ForeignKey(DocumentAttribute, on_delete=models.CASCADE)

    def __str__(self):
        return self.attribute_val


class CharMultiResponse(models.Model):
    by_character = models.ForeignKey('Character', on_delete=models.CASCADE)
    with_response = models.ForeignKey(Answer, on_delete=models.CASCADE)


class CharPolarResponse(models.Model):
    by_character = models.ForeignKey('Character', on_delete=models.CASCADE)
    for_question = models.ForeignKey(PolarQuestion, on_delete=models.CASCADE, null=True, default=None)
    with_response = models.BooleanField()


class Character(models.Model):
    name = models.CharField(max_length=200)

    def calculate_attributes(self):
        all_attributes = DocumentAttribute.objects.all()
        attr_counts = {}

        for an_attr in all_attributes:
            attr_counts[an_attr] = {}
            for a_val in an_attr.documentattrvalue_set.all():
                attr_counts[an_attr][a_val] = 0

        for a_mc in self.charmultiresponse_set.all():
            for a_val in a_mc.with_response.answer_score.all():
                attr_counts[a_val.for_attribute][a_val] += 1

        for a_plr in self.charpolarresponse_set.all():
            if a_plr.with_response:
                for a_val in a_plr.for_question.true_score.all():
                    attr_counts[a_val.for_attribute][a_val] += 1
            else:
                for a_val in a_plr.for_question.false_score.all():
                    attr_counts[a_val.for_attribute][a_val] += 1

        attr_vals = {}
        for an_attr in all_attributes:
            attr_vals[an_attr] = max(attr_counts[an_attr], key=attr_counts[an_attr].get)

        return attr_vals

    def str_attributes(self):
        str_out =""
        attr_dict = self.calculate_attributes()
        for key, value in attr_dict.items():
            str_out += "{}: {} \n".format(key, value)
        return str_out

