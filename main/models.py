from django.db import models


class Symptom(models.Model):
    symptom_name = models.CharField(max_length=200)

    def __str__(self):
        return self.symptom_name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    symptoms = models.ManyToMany(Symptom, related_name="symptoms")

    def __str__(self):
        return self.question_text
