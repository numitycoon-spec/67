def calculate_mean_score(quiz_score: float, exam_score: float, bonus: float):
    return ((quiz_score + exam_score) / 2) + bonus


def evaluate_final_score(quiz_score: float, exam_score: float, bonus: float):
    final_score = calculate_mean_score(quiz_score, exam_score, bonus)

    print(f"Final Score: {final_score:.2f}")

   
    if final_score >= 50.0:
        print("Result: Pass")
    else:
        print("Result: Fail")

evaluate_final_score(78.0, 86.0, 4.0)


