#21st june 2026
print("basic calculator");
import pandas as pd;
s=['+','*','/','%','-'];
while True:
    operation=input("enter operation");
    if operation=="+":
        while True:
             x=int(input("enter value="));
             y=int(input("enter value="));
#addition
             sum=x+y;
             print("sum =",sum);
             break
    elif operation=="*":
         while True:
            x=int(input("enter value="));
            y=int(input("enter value="));
#multiplication
            mul=x*y;
            print("product=",mul);
            break
    elif operation=="/":
         while True:
            x=int(input("enter value="));
            y=int(input("enter value="));
#division
            div=x/y;
            print("quotient=",div);
            break
    elif operation=="-":
        while True:
             x=int(input("enter value="));
             y=int(input("enter value="));
#subtraction
             sub=x-y;
             print("value=",sub);
             break
    elif operation=="%":
        while True:
              x=int(input("enter value="));
              y=int(input("enter value="));
#mod (division remainder )
              remainder=x%y;
              print("remainder=",remainder);
              break
    elif operation=="exit":
         print("calculator off");
         break
          