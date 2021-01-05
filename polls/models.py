import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return f'{self.question_text} DateTime: {self.pub_date}'
    
    
    def was_published_recently(self):
        return self.pub_date >= (timezone.localtime() - datetime.timedelta(days=1))
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Choice_text: {self.choice_text} \n Votes: {self.votes} \n Question_ID: {self.question.pk}'
    
