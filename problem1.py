'''
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
'''


def problem1():
    value = 0
    for i in range(0,1000):
        a = i%3
        b = i%5
        if(a==0 or b==0):
            value = value+i
    print 'sum of all the multiples of 3 or 5 below 1000 :',value
if __name__ == '__main__':
    problem1()