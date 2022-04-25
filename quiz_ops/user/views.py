from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserQuizSummary, UserQuizDetail
from quiz.models import Question, Options
from django.http import JsonResponse 

# Create your views here.

class QuizResultView(APIView):
    def post(self,request,format=None):
        # Getting Data ready
        quiz_data = request.data[0]
        quiz_summary = quiz_data.get('summary')
        quiz_detail = quiz_data.get('detail')
        # Calculating number of correct and wrong attempts 
        no_correct_attempt = 0
        no_wrong_attempt = 0
        score_percentage = 0
        # Iterate through each question in the request
        for quiz_question in quiz_detail:
            question = Question.objects.get(id=quiz_question.get('question_id'))
            # Get the list of options through question_id
            option_list = Options.objects.filter(question=question)
            # If the chosen option in the option list is correct then
            if option_list[quiz_question.get('user_answer_id')-1].option_flag:
                no_correct_attempt += 1
                # Add the weight of the question to score_percentage
                score_percentage += question.weight
            else :
                no_wrong_attempt += 1
        # Saving UserQuizSummary
        user_quiz_summary = UserQuizSummary(user=quiz_summary.get('user'),
                                            quiz_name=quiz_summary.get('quiz_name'),
                                            quiz_date=quiz_summary.get('quiz_date'),
                                            no_correct_attempt=no_correct_attempt,
                                            no_wrong_attempt=no_wrong_attempt)
        user_quiz_summary.save()
        # Iterate through each qustion in the detail
        for quiz_question in quiz_detail:
            question = Question.objects.get(id=quiz_question.get('question_id'))
            user_quiz_detail = UserQuizDetail(quiz_id=user_quiz_summary,
                                              question_id=question,
                                              user_answer=quiz_question.get('user_answer_id'))
            user_quiz_detail.save()
        return JsonResponse({'score_percentage':score_percentage})
            
        
