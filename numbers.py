#pi=3.14159
#print(pi)

first_num=input('Please enter a number')
second_num=input('Please enter a number')
#print(first_num+second_num)--gives 56 (treats numbers as strings)
#print(int(first_num)+int(second_num))---gives 11
#print(float(first_num)+float(second_num))---gives 11.0

days_in_February=28
#print(days_in_February+'total days in February')--unsupported operand type+ )int and string combined
#print(str(days_in_February)+' total days in February')

i=1
while True:
    if i%3==0:
        break
    print(i)
    i +=2

Nums=list({1: 'one' , 2: 'two'})
print(Nums)