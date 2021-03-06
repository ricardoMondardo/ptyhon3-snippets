# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

arrFibonacci = []
sumLast = 0
evenNumber = 2

for n in range(1,10):

    if (n <= 2):
        arrFibonacci.append(n)
    else:        
        LastTwo = arrFibonacci[len(arrFibonacci)-2:]
        sumLast = LastTwo[0] + LastTwo[1]
        arrFibonacci.append(sumLast)         

    if sumLast % 2 == 0 and sumLast >= 2:
        evenNumber += sumLast

print('evenNumber sum:', evenNumber ,', arrFibonacci:' , arrFibonacci)

