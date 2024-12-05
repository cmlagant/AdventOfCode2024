import re

def main():
    test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    data = open('03.txt').read().split("do()")
    data = remove_dont(data)
    matches = clean(data)
    flat = flatten(matches)
    print(product(flat))

    # Part 2 - split data at do() and don't. Keep the splits from do(), remove the splits starting with don't(). first split as normal.

def flatten(li):
    flat_matches = []
    for sublist in li:
        for item in sublist:
            flat_matches.append(item)
    return flat_matches

def remove_dont(li):
    filtered_list = []
    for i in li:
        if "don't()" in i:
            filtered_list.append(i.split("don't()")[0])
        else:
            filtered_list.append(i)
    return filtered_list


def clean(li):
    clean_data = []
    for i in li:
        # Regex - Find all strings that match the following format "mul([0-9][0-9],[0-9][0-9])" - Assumes 2 digit numbers. Saves to list of strings "mul(x,y)"
        matches = re.findall(r"mul\((\d+),(\d+)\)", i)
        clean_data.append(matches)
    return clean_data
        

def product(li):
    products = []
    for x, y in li:
        products.append(int(x) * int(y))
    return sum(products)
            

if __name__ == "__main__":
    main()

    