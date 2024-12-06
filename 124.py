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
    print(diag_data)
    # Reorient Strings - Reversed. Reverse Order all existing variations created so far \\ No need. Instead just findall "SAMX" too
    #flattened_data = flatten(test, vert_data, diag_data)
    # Count Occurences of "XMAS" in each string in all lists created above
    #matches = re.findall("XMAS", data)
    #print(f"XMAS appears {len(matches)} times in the puzzle")

def vert(li):
    vertical_strings = []
    for j in range(len(li[0])):                     # For each column
        vertical_string = ""                        # Collect letters
        for i in li:                                # For each row
            vertical_string += i[j]                 # Collect that column's letter from the row
        vertical_strings.append(vertical_string)
    return vertical_strings

def diag(li):
    diagonal_strings = [li[0][0] + li[1][1] + li[2][2], li[0][1] + li[1][2] + li[2][3], li[0][2] + li [1][3] + li[2][4]]
    return diagonal_strings





if __name__ == "__main__":
    main()