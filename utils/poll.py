def build_response_dictionary(response):
    """
    Builds a dictionary with the following format,
    {'question_id':'answer'}
    """
    question_ids = response.poll_response_questions.split(",")
    question_answers = response.poll_response_answers.split(",")
    response = {}
    for i in range(0, len(question_ids)):
       response[question_ids[i]] = question_answers[i]
    return response

def build_questionid_list(questions):
    ids = []
    for question in questions:
        ids.append(question.question_id)
    return ids

def get_question_type(questions, question_id):
    """ extract a questions type from a list of questions (used to prevent tons of database calls)"""
    for question in questions:
        if question.question_id == question_id:
            return question.question_type

def get_question_from_list(questions, q_id):
    for question in questions:
        if question.question_id == q_id:
            return question
