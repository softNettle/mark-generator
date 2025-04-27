import csv
from random import randint
from decimal import Decimal, ROUND_HALF_UP

def custom_round(number):
    return int(Decimal(number).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def csv_to_dict(filename):
    result = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            if row:
                key = row[0].lstrip("\ufeff")
                values = tuple(row[1:])
                result[key] = values
    return result

def generate_marks(mark_dict, column, amount):
    def fill_tuple(min, max):
        marks = []
        for i in range(amount):
            marks.append(randint(min, max))
        return tuple(marks)
    new_dict = {}
    for student in mark_dict:
        them_mark = int(mark_dict[student][column])
        result = 0
        new_marks=()
        while result != them_mark:
            if them_mark == 12:
                new_marks = fill_tuple(11,12)
            elif them_mark == 11:
                new_marks = fill_tuple(9,12)
            elif them_mark == 9 or them_mark == 10:
                new_marks = fill_tuple(7, 11)
            else:
                new_marks = fill_tuple(1, 10)
            average = sum(new_marks) / len(new_marks)
            result = custom_round(average)
        if result:
            new_dict[student] = new_marks
    return new_dict



