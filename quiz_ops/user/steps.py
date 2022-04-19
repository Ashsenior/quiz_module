'''
API request and response format:
The API should have the following request data for the quiz performed by user “quizadmin”.

Request:
[{
  "summary": {
      "quiz_name": "Geography",
      "quiz_date": "2022-01-19",
      "user": "quizadmin"
      },
  "detail": [{
          "question_id": 1,
          "user_answer_id": 1
          },
      {
          "question_id": 2,
          "user_answer_id": 2
      },
      {
          "question_id": 3,
          "user_answer_id": 3
      },
      {
          "question_id": 4,
          "user_answer_id": 4
      },
      {
          "question_id": 5,
          "user_answer_id": 1
      },
      {
          "question_id": 6,
          "user_answer_id": 2
      },
      {
          "question_id": 7,
          "user_answer_id": 3
      },
      {
          "question_id": 8,
          "user_answer_id": 4
      },
      {
          "question_id": 9,
          "user_answer_id": 1
      },
      {
          "question_id": 10,
          "user_answer_id": 2
      }
  ]
}]

You should save this response in UserQuizSummary and UserQuizDetail models.
On the basis of user answer id you have to check whether the response of the user is correct or not (correct answer for the given question id is already available in the options model).
Also you have to calculate total no of correct attempts and no of wrong attempts and save it into the UserQuizSummary model.
Also as per weight of the question which is already available in the Question model you have to calculate the total sum of weight of all correct questions and return it as a json response as follows:

Response:

{
   "score_percentage": 98
}


'''
