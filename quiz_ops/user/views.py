from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserQuizSummary, UserQuizDetail
from quiz.models import Question, Options
from django.http import JsonResponse 

# Create your views here.

class QuizResultView(APIView):
    def post(self,request,format=None):
        # Getting Data ready
        data = request.data[0]
        summary = data.get('summary')
        detail = data.get('detail')
        # Calculating number of correct and wrong attempts 
        no_correct_attempt = 0
        no_wrong_attempt = 0
        score_percentage = 0
        for q in detail:
            question = Question.objects.get(id=q.get('question_id'))
            options = Options.objects.filter(question=question)
            if options[q.get('user_answer_id')].option_flag:
                no_correct_attempt += 1
                score_percentage += question.weight
            else :
                no_wrong_attempt += 1
        # Saving UserQuizSummary
        user_quiz_summary = UserQuizSummary(user=summary.get('user'),
                                            quiz_name=summary.get('quiz_name'),
                                            quiz_date=summary.get('quiz_date'),
                                            no_correct_attempt=no_correct_attempt,
                                            no_wrong_attempt=no_wrong_attempt)
        user_quiz_summary.save()
        # Saving UserQuizDetail
        for q in detail:
            question = Question.objects.get(id=q.get('question_id'))
            user_quiz_detail = UserQuizDetail(quiz_id=user_quiz_summary,
                                              question_id=question,
                                              user_answer=q.get('user_answer_id'))
            user_quiz_detail.save()
        return JsonResponse({'score_percentage':score_percentage})
            
        
