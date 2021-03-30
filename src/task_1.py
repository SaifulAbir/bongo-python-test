# This function will print all keys of a nested dictionary with their depth.
def print_depth(data, depth=0):
    for key, value in data.items():
        print(key, depth+1)
        if type(value) is dict:
            print_depth(value, depth+1)


if __name__ == '__main__':
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    print_depth(a)
