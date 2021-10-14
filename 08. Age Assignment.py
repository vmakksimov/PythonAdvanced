def age_assignment(*args, **kwargs):
    new = {}
    for el in args:
        if el[0] in kwargs.keys():
            key = el
            value = kwargs[el[0]]
            new[key] = value

    return new



print(age_assignment("Peter", "George", G=26, P=19))