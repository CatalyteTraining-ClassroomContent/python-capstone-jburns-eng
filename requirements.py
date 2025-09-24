quiz_submmission1 = {
    "quiz_name": "Fruit Transition",
    "quiz_module": "Art",
    "quiz_score": "95",
    "student_id": "100",
    "student_name": "Jessica Alba",
    "submission_date": "9-22-2025",
}

quiz_submission2 = {
    "quiz_name": "Calculating Fractions",
    "quiz_module": "Algebra",
    "quiz_score": "77",
    "student_id": "101",
    "student_name": "Mark Walhberg",
    "submission_date": "9-22-2025",
}

quiz_submission3 = {
    "quiz_name": "Supply and Demand",
    "quiz_module": "Economics",
    "quiz_score": "100",
    "student_id": "102",
    "student_name": "Tony Stark",
    "submission_date": "9-23-2025",
}

quiz_submission4 = {
    "quiz_name": "Fruit Transition",
    "quiz_module": "Art",
    "quiz_score": "88",
    "student_id": "101",
    "student_name": "Mark Walhberg",
    "submission_date": "9-22-2025",
}

quiz_submission5 = {
    "quiz_name": "Calculating Fractions",
    "quiz_module": "Algebra",
    "quiz_score": "74",
    "student_id": "100",
    "student_name": "Jessica Alba",
    "submission_date": "9-22-2025",
}

quiz_submission6 = {
    "quiz_name": "Fruit Transition",
    "quiz_module": "Art",
    "quiz_score": "77",
    "student_id": "102",
    "student_name": "Tony Stark",
    "submission_date": "9-22-2025",
}

quiz_submission7 = {
    "quiz_name": "Calculating Fractions",
    "quiz_module": "Algebra",
    "quiz_score": "99",
    "student_id": "102",
    "student_name": "Tony Stark",
    "submission_date": "9-22-2025",
}

quiz_submission8 = {
    "quiz_name": "Supply and Demand",
    "quiz_module": "Economics",
    "quiz_score": "83",
    "studend_id": "100",
    "student_name": "Jessica Alba",
    "submission_date": "9-23-2025",
}

quiz_submission9 = {
    "quiz_name": "Supply and Demand",
    "quiz_module": "Economics",
    "quiz_score": "87",
    "student_id": "101",
    "student_name": "Mark Walhberg",
    "submission_date": "9-23-2025",
}


submissions = [
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": "74",
        "student_id": "100",
        "student_name": "Jessica Alba",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": "77",
        "student_id": "101",
        "student_name": "Mark Walhberg",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": "100",
        "student_id": "102",
        "student_name": "Tony Stark",
        "submission_date": "9-23-2025",
    },
    {
        "quiz_name": "Fruit Transition",
        "quiz_module": "Art",
        "quiz_score": "88",
        "student_id": "101",
        "student_name": "Mark Walhberg",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": "74",
        "student_id": "100",
        "student_name": "Jessica Alba",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Fruit Transition",
        "quiz_module": "Art",
        "quiz_score": "77",
        "student_id": "102",
        "student_name": "Tony Stark",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": "99",
        "student_id": "102",
        "student_name": "Tony Stark",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": "83",
        "studend_id": "100",
        "student_name": "Jessica Alba",
        "submission_date": "9-23-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": "87",
        "student_id": "101",
        "student_name": "Mark Walhberg",
        "submission_date": "9-23-2025",
    },
]


def filter_by_date(submissions, date):
    filtered_submissions = []
    for submission in submissions:
        if submission["submission_date"] == date:
            filtered_submissions.append(submission)
    return filtered_submissions


def filter_by_student_id(submissions, student_id):
    return [
        submissions
        for submissions in submissions
        if submissions.get("studentId") == student_id
    ]


def find_unsubmitted_quizzes(submissions, student_id):
    unsubmitted_quizzes = []
    for submission in submissions:
        if submission["student_id"] == student_id:
            unsubmitted_quizzes.append(submission["quiz_name"])
    return unsubmitted_quizzes


def get_average_score(submissions):
    total = sum(submission["quiz_score"] for submission in submissions)
    return total / len(submissions)


def get_average_score_by_module(submissions, module):
    filtered_submissions = sum(submissions, module)
    total = sum(submission["quiz_score"] for submission in filtered_submissions)
    return total / len(filtered_submissions)


print(submissions)
date_filtered = filter_by_date(submissions, "9-22-2025")
date_filtered = filter_by_date(submissions, "9-23-2025")
print(date_filtered, "9-22-2025")
print(date_filtered, "9-23-2025")
id_filtered = filter_by_student_id(submissions, "100")
print(id_filtered, "Jessica Alba")
unsubmitted_quiz = find_unsubmitted_quizzes(submissions)
print(unsubmitted_quiz)
print(find_unsubmitted_quizzes)
print(get_average_score)
print(get_average_score_by_module)
