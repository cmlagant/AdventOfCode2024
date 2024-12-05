def main():
    # Import txt - split on /n
    test =[
        ["MMMSXXMASM"],
        ["MSAMXMSMSA"],
        ["AMXSXMAAMM"],
        ["MSAMASMSMX"],
        ["XMASAMXAMM"],
        ["XXAMMXXAMA"],
        ["SMSMSASXSS"],
        ["SAXAMASAAA"],
        ["MAMMMXMMMM"],
        ["MXMXAXMASX"]
    ]
    # Reorient Strings - Vertical. Loop through test and build a new list of [all test[0], all test[1], etc.]

    # Reorient Strings - Diagonal. Loop through test and build a new list of valid [test1[0], test2[1], test3[2], etc.]

    # Reorient Strings - Reversed. Reverse Order all existing variations created so far

    # Count Occurences of "XMAS" in each string in all lists created above

if __name__ == "__main__":
    main()