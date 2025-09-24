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
    "student_id": "100",
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
        "student_id": "100",
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
    return [
        submissions
        for submissions in submissions
        if submissions["submission_date"] == date
    ]


def filter_by_student_id(submissions, student_id):
    return [
        submissions
        for submissions in submissions
        if submissions.get("student_id") == student_id
    ]


all_quizzes = ["Fruit Transition", "Calculating Fractions", "Supply and Demand"]


def find_unsubmitted_quizzes(submissions, student_id):

    submitted = [
        submissions["quiz_name"]
        for submissions in submissions
        if submissions.get("student_id") == student_id
    ]

    unsubmitted = [quiz for quiz in all_quizzes if quiz not in submitted]
    return unsubmitted


def get_average_score(submissions):
    scores = [
        int(submissions["quiz_score"])
        for submissions in submissions
        if "quiz_score" in submissions
    ]
    return sum(scores) / len(scores) if scores else 0


def get_average_score_by_module(submissions, module):
    scores = [
        int(submissions["quiz_score"])
        for submissions in submissions
        if submissions["quiz_module"] == module
    ]
    return sum(scores) / len(scores) if scores else 0


print(submissions)

print(filter_by_date(submissions, "9-22-2025"))
print(filter_by_date(submissions, "9-23-2025"))
print(filter_by_student_id(submissions, "100"))
print(filter_by_student_id(submissions, "101"))
print(filter_by_student_id(submissions, "102"))
print(find_unsubmitted_quizzes(submissions, "100"))
print(find_unsubmitted_quizzes(submissions, "101"))
print(find_unsubmitted_quizzes(submissions, "102"))
print("The average score of all quizzes are", get_average_score(submissions))
print(
    "The average score of Algebra scores are",
    get_average_score_by_module(submissions, "Algebra"),
)
print(
    "The average score of Art scores are",
    get_average_score_by_module(submissions, "Art"),
)
print(
    "The average score of Economics scores are",
    get_average_score_by_module(submissions, "Economics"),
)
