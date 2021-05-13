# estas variables se definen dentro del ambiente __main__
name = 'Alan Turing'
age = 41
birthplace = 'Maida Vale, London, England'
gender = "male"
def say_hi():
# Estas variables están siendo defindas en un ambiente nuevo: el de any_function
# Las variables name y age son "variables nuevas",
# que no tienen relación con las variables globales definidas previamente.
    name = 'Ian MacKaye'
    age = 56
    occupation = 'Musician'
    print("{} is a {} and is {} years old. He is {}.".format(name,
    occupation, age, gender))
# name y age tomarán los valores de su scope local
say_hi()
# name y age toman los valores del scope main

print("{} was born in {} and died when he was {} years old. He was {}.".format(name, birthplace, age, gender))
