class pragati:
    director = "shambu"
    age = 45


class cse(pragati):
    HOD = "rajesh"
    age = 40


class data_science(cse):
    CR = "roshan"
    age = 20


class machine_learning(pragati):
    CR = "dadala"
    age = 15
    obj = cse()
    print(obj.age)
    print(obj.director)
    print(obj.HOD)
