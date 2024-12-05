import re

def main():
    # Import txt - split on /n
    test =[
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # Reorient Strings - Vertical. Loop through test and build a new list of [all test[0], all test[1], etc.]
    vert_data = vert(test)
    print(vert_data)
    # Reorient Strings - Diagonal. Loop through test and build a new list of valid [test1[0], test2[1], test3[2], etc.]
    diag_data = diag(test)
    # Reorient Strings - Reversed. Reverse Order all existing variations created so far
    flattened_data = flatten(test, vert_data, diag_data)
    reversed_data = reverse(flattened_data)
    data = flattened_data.append(reversed_data)
    # Count Occurences of "XMAS" in each string in all lists created above
    matches = re.findall("XMAS", data)
    print(f"XMAS appears {len(matches)} times in the puzzle")

def vert(li):
    vertical_strings = []
    for j in range(len(li[0])):
        vertical_string = ""
        for i in li:
            vertical_string += i[j]
        vertical_strings.append(vertical_string)
    return vertical_strings


if __name__ == "__main__":
    main()