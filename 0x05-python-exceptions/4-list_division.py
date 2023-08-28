#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists"""
    div_result = []
    for i in range(list_length):
        divide = 0
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            div_result.append(divide)
    return div_result
