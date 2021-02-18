"""
Name : homework1.py
Author : Emrullah GUNES
Contact : egunes1911@gmail.com
Time    : 17.02.2021 13:42
Desc:
    Prepared for an assignment given in the Introduction To Python course given by Global AI HUB.
    Homework subject : Generating a 3x3 matrix with 9 random prime numbers. (You have to do it using the for loop.)
"""
import random  # We used the "random" library to generate a random number.

# Global variables
matrixRow = 3  # We defined the row variable of the matrix we will create as three.
matrixColumn = 3  # We defined the column variable of the matrix we will create as three.


def check_prime(random_num):  # A function that checks whether a randomly determined number is prime.
    i = 2
    while i < random_num:   # A loop that takes the mode of the random number
        k = random_num % i  # with numbers from 2 to one less than the random number.
        i += 1
        if k == 0:        # This number is not prime if the remainder is 0 when
            return False  # divided by a number other than itself and 1.
    return True


def print_matrix(row, column, matrix):  # The function I use to print any list in matrix form.
    for i in range(row):
        [print(matrix[i][j], end=" ") for j in range(column)]  # We printed it using the comprehension method.
        print()


""" The for loop is written more clearly
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()
"""


def generating_matrix(row, column):
    count = 0
    prime_list = []
    while count < (row * column):
        random_num = random.randint(2, 1000)  # We have defined a variable for the random number between (2,1000)
        check = check_prime(random_num)  # We call the control function and pass it to a boolean variable.
        if check:
            prime_list.append(random_num)  # If the number is prime add it to the list.
            count += 1  # we increment the counter one by one
    matrix = [[prime_list[(i + j) + (i * 2)] for j in range(column)] for i in range(row)]
    # We rebuild the list in matrix format using two for loops.
    print_matrix(row, column, matrix)  # We print our matrix by calling the print function.


""" The for loop is written more clearly
    for i in range(row):
        iter1 = []
        for j in range(column):
            iter1.append(prime_list[(i + j) + (i * 2)])
        matrix.append(iter1)    
"""


# Main  function
generating_matrix(matrixRow, matrixColumn)  # It will be sufficient to change
                                            # the number of rows and columns of the matrix
                                            # you want to create in the global variables section.
