'''
This program was created by Kaleb in an attempt to make his life easier
'''
def F(x):
    y = x**2 + 1
    return y

def Left_Sum(i,n):
    a = i[0]
    b = i[1]
    dif = b - a
    
    Sum = 0
    for i in range(1,n+1):
        ToSubs = (a + (dif/n)*(i-1))
        ToAdd = F(ToSubs)
        Sum += ToAdd
    ToPrint = Sum * (dif/n)
    return round(ToPrint,4)

def Right_Sum(i,n):
    a = i[0]
    b = i[1]
    dif = b - a
    
    Sum = 0
    for i in range(1,n+1):
        ToSubs = (a + (dif/n)*i)
        ToAdd = F(ToSubs)
        Sum += ToAdd
    ToPrint = Sum * (dif/n)
    return round(ToPrint,4)
    
def Middle_Sum(i,n):
    a = i[0]
    b = i[1]
    dif = b - a
    
    Sum = 0
    for i in range(1,n+1):
        ToSubs = (a + (dif/n)*((2*i-1)/2))
        ToAdd = F(ToSubs)
        Sum += ToAdd
    ToPrint = Sum * (dif/n)
    return round(ToPrint,4)


WhichSum = input('Indicate which method you wish to use, (Right, Left, or Middle): ')
Interval = input('Indicate which interval you wish to use (seperate by space): ')
Interval = Interval.split()
for i in range(len(Interval)):
    Interval[i] = float(Interval[i])
HowMany  = int(input('Indicate how many rectangles you wish to use in the summation: '))
print()

if WhichSum.upper() == 'RIGHT':
    print('Your answer is:',Right_Sum(Interval,HowMany))
elif WhichSum.upper() == 'LEFT':
    print('Your answer is:',Left_Sum(Interval,HowMany))
elif WhichSum.upper() == 'MIDDLE':
    print('Your answer is:',Middle_Sum(Interval,HowMany))
