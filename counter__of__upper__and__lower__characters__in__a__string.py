
def counter_lower_upper_case(string):
    lower_case = 0
    upper_case = 0
    for caracter in string:
        if('A'<=caracter<='Z'):
            upper_case += 1
        elif('a'<=caracter<='z'):
            lower_case += 1
        else:
            continue
    return lower_case,upper_case


string = input("Enter a string: ")
lower_case,upper_case = counter_lower_upper_case(string)
print("The string {0} has {1} upper and lower"
      " {2} characters".format(string,str(upper_case),str(lower_case)))


