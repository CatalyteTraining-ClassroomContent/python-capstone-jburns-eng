quiz_submmission1 = {
    "quiz_name": "Fruit Transition",
    "quiz_module": "Art",
    "quiz_score": 95,
    "student_id": 100,
    "student_name": "Jessica Alba",
    "submission_date": "9-22-2025",
}

quiz_submission2 = {
    "quiz_name": "Calculating Fractions",
    "quiz_module": "Algebra",
    "quiz_score": 77,
    "student_id": 101,
    "student_name": "Mark Walhberg",
    "submission_date": "9-22-2025",
}

quiz_submission3 = {
    "quiz_name": "Supply and Demand",
    "quiz_module": "Economics",
    "quiz_score": 100,
    "student_id": 102,
    "student_name": "Tony Stark",
    "submission_date": "9-23-2025",
}

quiz_submission4 = {
    "quiz_name": "Fruit Transition",
    "quiz_module": "Art",
    "quiz_score": 88,
    "student_id": 101,
    "student_name": "Mark Walhberg",
    "submission_date": "9-22-2025",
}

quiz_submission5 = {
    "quiz_name": "Calculating Fractions",
    "quiz_module": "Algebra",
    "quiz_score": 74,
    "student_id": 100,
    "student_name": "Jessica Alba",
    "submission_date": "9-22-2025",
}

quiz_submission6 = {
    "quiz_name": "Fruit Transition",
    "quiz_module": "Art",
    "quiz_score": 77,
    "student_id": 102,
    "student_name": "Tony Stark",
    "submission_date": "9-22-2025",
}

quiz_submission7 = {
    "quiz_name": "Calculating Fractions",
    "quiz_module": "Algebra",
    "quiz_score": 99,
    "student_id": 102,
    "student_name": "Tony Stark",
    "submission_date": "9-22-2025",
}

quiz_submission8 = {
    "quiz_name": "Supply and Demand",
    "quiz_module": "Economics",
    "quiz_score": 83,
    "student_id": 100,
    "student_name": "Jessica Alba",
    "submission_date": "9-23-2025",
}

quiz_submission9 = {
    "quiz_name": "Supply and Demand",
    "quiz_module": "Economics",
    "quiz_score": 87,
    "student_id": 101,
    "student_name": "Mark Walhberg",
    "submission_date": "9-23-2025",
}


submissions = [
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 74,
        "student_id": 100,
        "student_name": "Jessica Alba",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 77,
        "student_id": 101,
        "student_name": "Mark Walhberg",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": 100,
        "student_id": 102,
        "student_name": "Tony Stark",
        "submission_date": "9-23-2025",
    },
    {
        "quiz_name": "Fruit Transition",
        "quiz_module": "Art",
        "quiz_score": 88,
        "student_id": 101,
        "student_name": "Mark Walhberg",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 74,
        "student_id": 100,
        "student_name": "Jessica Alba",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Fruit Transition",
        "quiz_module": "Art",
        "quiz_score": 77,
        "student_id": 102,
        "student_name": "Tony Stark",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 99,
        "student_id": 102,
        "student_name": "Tony Stark",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": 83,
        "student_id": 100,
        "student_name": "Jessica Alba",
        "submission_date": "9-23-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": 87,
        "student_id": 101,
        "student_name": "Mark Walhberg",
        "submission_date": "9-23-2025",
    },
]


def filter_by_date(date: str, submissions: list) -> list:
    return [
        submissions
        for submission in submissions
        if submission["submission_date"] == date
    ]


def filter_by_student_id(student_id, submissions):
    return [
        submission
        for submission in submissions
        if submission.get("student_id") == student_id
    ]


submissions = [
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 74,
        "student_id": 100,
        "student_name": "Jessica Alba",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 77,
        "student_id": 101,
        "student_name": "Mark Walhberg",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": 100,
        "student_id": 102,
        "student_name": "Tony Stark",
        "submission_date": "9-23-2025",
    },
    {
        "quiz_name": "Fruit Transition",
        "quiz_module": "Art",
        "quiz_score": 88,
        "student_id": 101,
        "student_name": "Mark Walhberg",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 74,
        "student_id": 100,
        "student_name": "Jessica Alba",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Fruit Transition",
        "quiz_module": "Art",
        "quiz_score": 77,
        "student_id": 102,
        "student_name": "Tony Stark",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Calculating Fractions",
        "quiz_module": "Algebra",
        "quiz_score": 99,
        "student_id": 102,
        "student_name": "Tony Stark",
        "submission_date": "9-22-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": 83,
        "student_id": 100,
        "student_name": "Jessica Alba",
        "submission_date": "9-23-2025",
    },
    {
        "quiz_name": "Supply and Demand",
        "quiz_module": "Economics",
        "quiz_score": 87,
        "student_id": 101,
        "student_name": "Mark Walhberg",
        "submission_date": "9-23-2025",
    },
]
all_quizzes = ["Fruit Transition", "Calculating Fractions", "Supply and Demand"]


def find_unsubmitted(date, student_names, submissions):

    submitted_students_on_date = {
        submission["student_name"]
        for submission in submissions
        if submission["submission_date"] == date
    }
    unsubmitted = [
        name for name in student_names if name not in submitted_students_on_date
    ]

    return unsubmitted


def get_average_score(submissions):
    if not submissions:
        return 0.0
    scores = [submission["quiz_score"] for submission in submissions]
    average = sum(scores) / len(scores)
    return round(average, 1)


def get_average_score_by_module(submissions: list) -> dict:

    module_scores = {}

    for submission in submissions:
        module = submission.get("quiz_module")
        score = submission.get("quiz_score")

        if module is not None and score is not None:
            if module not in module_scores:
                module_scores[module] = []
            module_scores[module].append(score)

    average_scores = {}
    for module, scores in module_scores.items():
        if scores:
            average = sum(scores) / len(scores)
            average_scores[module] = round(average, 1)

    return average_scores


print("All submissions for student 100:")
jessicas_submissions = filter_by_student_id(100, submissions)
print(jessicas_submissions)

print("All submissions for student 101:")
mark_submissions = filter_by_student_id(101, submissions)
print(mark_submissions)

print("All submissions for student 102:")
tony_submissions = filter_by_student_id(102, submissions)
print(tony_submissions)

print("All submissions for student 103:")
james_soul_right_now_submissions = filter_by_student_id(104, submissions)
print(james_soul_right_now_submissions)


filtered_day_one = filter_by_date("9-22-2025", submissions)
print(f"Submissions for 9-22-2025: {len(filtered_day_one)} results")

filtered_day_two = filter_by_date("9-23-2025", submissions)
print(f"Submissions for 9-23-2025: {len(filtered_day_two)} results")

filtered_empty = filter_by_date("9-24-2025", submissions)
print(f"Submissions for 9-24-2025: {len(filtered_empty)} results")

filtered_empty_list = filter_by_date("9-22-2025", [])
print(
    f"Submissions for 9-22-2025 from an empty list: {len(filtered_empty_list)} results"
)


date1 = "9-22-2025"
student_names1 = ["Jessica Alba", "Mark Walhberg", "Tony Stark"]
print(f"Students with unsubmitted quizzes on {date1}:")
print(find_unsubmitted(date1, student_names1, submissions))


date2 = "9-23-2025"
student_names2 = ["Jessica Alba", "Mark Walhberg", "Tony Stark"]
print(f"Students with unsubmitted quizzes on {date2}:")
print(find_unsubmitted(date2, student_names2, submissions))

date3 = "9-24-2025"
student_names3 = ["Jessica Alba", "Mark Walhberg", "Tony Stark"]
print(f"Students with unsubmitted quizzes on {date3}:")
print(find_unsubmitted(date3, student_names3, submissions))


average_score = get_average_score(submissions)
print(f"The average quiz score of all quizzes is: {average_score}")


average_scores_by_module = get_average_score_by_module(submissions)
print(average_scores_by_module)
