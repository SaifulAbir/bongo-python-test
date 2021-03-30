class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def print_depth(data, depth=0):
    if type(data) is Person:
        print_family_info(data.__dict__, depth)
    elif isinstance(data, dict):
        for key, value in data.items():
            print(key, depth + 1)
            if type(value) is dict:
                print_depth(value, depth + 1)
            elif isinstance(value, Person):
                print_family_info(value.__dict__, depth + 1)


def print_family_info(data, depth):
    for key, value in data.items():
        print(key, depth+1)
        if isinstance(value, Person):
            print_family_info(value.__dict__, depth+1)


if __name__ == '__main__':
    person_a = Person("Barbara", "Fain", None)
    person_b = Person("Saiful", "Islam", person_a)

    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
            }
        },
    }
    print_depth(a)