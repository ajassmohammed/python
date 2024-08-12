def arithmatic_operation(a,b,operation):
    if operation =='add':
        return a+b
    elif operation =='sub':
        return a-b
    elif operation =='multi':
        return a*b
    elif operation =='div':
        x=4
        y=2
        if y!=0:
            return x/y
        else:
            return"error:division by zero is not possible"
    else:
            return"invalid error"


a = float(input("enter the number 1: "))
b = float(input("enter the number 2: "))
print(arithmatic_operation(a, b, 'add'))
print(arithmatic_operation(a, b, 'sub'))
print(arithmatic_operation(a, b, 'multi'))
print(arithmatic_operation(a, b, 'div'))

