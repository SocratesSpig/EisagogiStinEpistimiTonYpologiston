length = int(input("Enter the length of the list :"))
list = []
newValue = True
difference = True
sumInterval = 0

while length % 2 != 0:

    length = int(input("You have to enter an prime integer :"))

for i in range(0, length):

    number = float(input("Enter the numbers in the list : "))

    list.append(number)


x=0

while x < length:

    if list[x] > list[x+1]:

        list[x], list[x+1] = list[x+1], list[x]

    x += 2

print(list)

i=0
j=0

while i < length:

    if i < 2:

        sumInterval += list[i+1] - list[i]

    while j < length:

        if list[i] > list[j+1] or list[i+1] < list[j]:

            if newValue == True:

                sumInterval += + list[j+1] - list[j]
                newValue = False

        elif list[i+1] >= list[j] and list[i+1] <= list[j+1] and difference == True:

            if j >= 2:

                sumInterval = sum + list[j+1] - list[i+1]
                difference = False
        j+=2

    i+=2


print(sumInterval)