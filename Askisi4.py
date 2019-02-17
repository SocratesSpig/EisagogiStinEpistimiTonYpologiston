firstnumber=input('you have to put the firt number')
chooseoperation=input('you have to choose the operation')
secondnumber=input('you have to put the second number')




if firstnumber == 'zero':
    firstnumber = 0
if secondnumber == 'zero' :
    secondnumber = 0
if firstnumber == 'one':
    firstnumber = 1
if secondnumber == 'one' :
    secondnumber = 1
if firstnumber == 'two':
 firstnumber = 2
if secondnumber == 'two':
    secondnumber = 2
if firstnumber == 'three':
    firstnumber = 3
if secondnumber == 'three' :
    secondnumber = 3
if firstnumber == 'four':
    firstnumber = 4
if secondnumber == 'four' :
    secondnumber = 2
if firstnumber == 'five':
 firstnumber = 5
if secondnumber == 'five':
    secondnumber = 5
if firstnumber == 'six':
    firstnumber = 6
if secondnumber == 'six' :
    secondnumber = 6
if firstnumber == 'seven':
    firstnumber = 7
if secondnumber == 'seven' :
    secondnumber = 7
if firstnumber == 'eight':
 firstnumber = 8
if secondnumber == 'eight':
    secondnumber = 8
if firstnumber == 'nine':
    firstnumber = 9
if secondnumber == 'nine' :
    secondnumber = 9



if firstnumber == '' and chooseoperation == '' and secondnumber =='':
    print("put number")
else:
    if chooseoperation == "plus":

        sum= int(firstnumber) + int(secondnumber)
        print (firstnumber,"(",chooseoperation,"(",secondnumber,"))","output",sum)
    elif chooseoperation == "time":
       Multiplying = firstnumber * secondnumber
       print(firstnumber,"(",chooseoperation,"(",secondnumber,"))","output",Multiplying)
    elif chooseoperation == "minus":
        plin = firstnumber - secondnumber
        print(firstnumber, "(", chooseoperation, "(", secondnumber, "))", "output",plin)