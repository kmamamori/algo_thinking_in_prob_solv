from p1_majority_element import majority_element
from p2_single_one import single_number
from p3_climb_stairs import climb_stairs
from p4_house_robber import house_robber
from p5_best_time_to_buy_sell import best_time


points_per_problem = 20


def grade_p1():
    grade = 0

    test1 = majority_element([3, 2, 3])
    test2 = majority_element([2, 2, 1, 1, 1, 2, 2])
    test3 = majority_element([2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    if test1 == 3 and test2 == 2 and test3 == 1:
        grade += points_per_problem

    return grade


def grade_p2():
    grade = 0

    test1 = single_number([2,2,1])
    test2 = single_number([4, 1, 2, 1, 2])
    test3 = single_number([8, 9, 9, 8, 1, 0, 1, 3, 2, 3, 2])

    if test1 == 1 and test2 == 4 and test3 == 0:
        grade += points_per_problem

    return grade


def grade_p3():
    grade = 0

    test1 = climb_stairs(2)
    test2 = climb_stairs(3)
    test3 = climb_stairs(13)

    if test1 == 2 and test2 == 3 and test3 == 377:
        grade += points_per_problem
    return grade


def grade_p4():
    grade = 0

    test1 = house_robber([1,2,3,1])
    test2 = house_robber([2, 7, 9, 3, 1])
    test3 = house_robber([1, 200, 3, 3, 400, 1])

    if test1 == 4 and test2 == 12 and test3 == 600:
        grade += points_per_problem

    return grade


def grade_p5():
    grade = 0

    test1 = best_time([7,1,5,3,6,4])
    test2 = best_time([7, 6, 4, 3, 1])
    test3 = best_time([7, 1, 5, 3, 6, 4, 3, 10, 10, 8])

    if test1 == 5 and test2 == 0 and test3 == 9:
        grade += points_per_problem

    return grade


def compute_grade():

    grade = 0

    grade += grade_p1()
    grade += grade_p2()
    grade += grade_p3()
    grade += grade_p4()
    grade += grade_p5()

    return grade


grade = compute_grade()

print("Your grade is: ", grade)



