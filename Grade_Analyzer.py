def calculate_vit_grade():
    print("=== VIT Bhopal Grade & Pass Predictor ===")
    
    # 1. Identify Course Type
    print("Course Types: 1. LT | 2. LP | 3. LTP")
    choice = input("Select Course Type (1-3): ")
    
    # 2. Input Internal Components (Marks out of 50 total)
    # Based on Assessment Table [cite: 7]
    midterm = float(input("Mid-term Score (out of 50, weighted to 30): "))
    midterm_weighted = (midterm / 50) * 30
    
    attendance_pct = float(input("Your Attendance Percentage: "))
    # Attendance Marks Logic 
    if attendance_pct >= 96: att_marks = 5
    elif attendance_pct >= 91: att_marks = 4
    elif attendance_pct >= 86: att_marks = 3
    elif attendance_pct >= 81: att_marks = 2
    elif attendance_pct >= 75: att_marks = 1
    else: att_marks = 0
    
    # Simple input for remaining internals (Assignments/Lab/Class Assessment)
    # LTP total internals = 30 (Midterm) + 5 (Att) + 10 (Class) + 25 (Lab) = 70 (scaled later)
    # For simplicity, we ask for the remaining 'Internal' bucket marks [cite: 7]
    other_internals = float(input("Other Internal marks (Assignments/Lab/Quiz total): "))
    
    total_internal_score = midterm_weighted + att_marks + other_internals
    print(f"\nTotal Internal Score: {total_internal_score:.2f} / 70")

    # 3. Predict TEE Needs based on Pass Criteria 
    # Rule 1: TEE >= 40/100
    # Rule 2: (Midterm (50) + TEE (100)) >= 60/150
    
    min_tee_rule1 = 40
    min_tee_rule2 = 60 - midterm 
    
    required_for_pass = max(min_tee_rule1, min_tee_rule2)

    print("-" * 40)
    print(f"PASS REQUIREMENT FOR {choice}:")
    print(f"- You MUST score at least {required_for_pass}/100 in TEE to pass.")
    
    # 4. Absolute Grading Prediction 
    target_grade = input("\nEnter Target Grade (S, A, B, C, D, E): ").upper()
    grade_thresholds = {"S": 90, "A": 80, "B": 70, "C": 60, "D": 50, "E": 40}
    
    if target_grade in grade_thresholds:
        # Total = Internals (70) + TEE_Weighted (30)
        target_score = grade_thresholds[target_grade]
        needed_tee_weighted = target_score - total_internal_score
        needed_tee_raw = (needed_tee_weighted / 30) * 100
        
        if needed_tee_raw > 100:
            print(f"To get an {target_grade}, you'd need {needed_tee_raw:.1f}/100. (Impossible!)")
        else:
            print(f"To get an {target_grade}, you need {max(needed_tee_raw, required_for_pass):.1f}/100 in TEE.")
    print("-" * 40)

if __name__ == "__main__":
    calculate_vit_grade()