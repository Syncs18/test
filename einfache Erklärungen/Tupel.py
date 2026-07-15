
list1 = [1,3,4,8]
print(list1)

list1[1] = 10
print(list1)

tupel1 = (1,3,4,8)
print(tupel1)

person1 = ("Max", "Mustermann", 28)

first_name, last_name, age = person1
print(first_name)
print(last_name)
print(age)

def gen_p(name, age):
    # durch name und alter mehrere passwörter

    return ("passwort","passwort2", "passwort3")

password1, password2, passwort3=gen_p("Max", 20)
print(password2)

