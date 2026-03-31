#  VIT Bhopal Grade & Pass Predictor

# Project Overview
The VIT Bhopal Grade & Pass Predictor is a Python-based application that helps students estimate their academic performance based on internal marks and exam criteria.

It allows users to:
- Predict pass/fail status
- Calculate minimum TEE marks required
- Estimate marks needed for target grades

---

# Features
- Supports course types: LT, LP, LTP
- Calculates internal marks (out of 70)
- Applies attendance-based scoring system
- Predicts minimum TEE marks required to pass
- Calculates TEE marks needed for target grades
- Simple command-line interface

---

#  Working Logic

# Internal Marks (Out of 70)
- Midterm (scaled to 30)
- Attendance (out of 5)
- Other internals

# Attendance Criteria
- ≥ 96% → 5
- 91–95% → 4
- 86–90% → 3
- 81–85% → 2
- 75–80% → 1
- < 75% → 0

---

# Pass Criteria
1. TEE ≥ 40/100
2. Midterm + TEE ≥ 60/150

---

# Grade Thresholds
S → 90  
A → 80  
B → 70  
C → 60  
D → 50  
E → 40  

---

# How to Run

1. Install Python 3
2. Save file as: vit_grade_predictor.py
3. Run:
python vit_grade_predictor.py

---

# Functionalities
- Input marks
- Calculate internals
- Predict pass requirement
- Estimate grade targets

---

#  Author
Tushar Tyagi  
Reg No: 25BCE11251
