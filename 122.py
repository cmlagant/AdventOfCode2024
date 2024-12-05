import pandas as pd

def main():
    # Import Input as Array
    #df = pd.read_csv("122data.csv", header = None)
    #data = df.values.tolist()
    data = [[int(y) for y in x.split(' ')] for x in open('02.txt').read().split('\n')]
    print(f"There are {len(data)} reports")
    #print(data)

    # Create Test Array
    test_data = [
      [7,6,4,2,1],
      [1,2,7,8,9],
      [9,7,6,2,1],
      [1,3,2,4,5],
      [8,6,4,4,1],
      [1,3,6,7,9]  
    ]
    # Create safety_check function - Returns count of safe rows
    print(f"There are {safety_check(data)} safe reports")
    print(f"There are {dampener(data)} safe reports with the dampener")

def safety_check(array):
    # Filter for rows that are increasing or decreasing
    filtered_array = [row for row in array if increasing_or_decreasing(row)]
    print(f"There are {len(filtered_array)} increasing or decreasing reports")

    results = 0
    # If first check passes - determine abs between steps. 1 <= Distance <=3
    for report in filtered_array:
        if safe_distance(report):
            # If both checks pass - update result and move to next row
            results += 1
    return results

def safe_distance(li):
    for i in range(len(li) - 1):
        distance = abs(li[i + 1] - li[i])
        if not (1 <= distance <= 3):
            return False
    return True

def increasing_or_decreasing(li):
    # Remove reports with duplicate levels and Match report against a sort OR reverse sort
    if len(li) != len(set(li)):
        return False
    return li == sorted(li) or li == sorted(li, reverse=True)

def dampener(li):
    results = 0
    for i in li:
        if i:  # Ensure the sublist is not empty
            for j in range(len(i)):  # Generate variations excluding one element
                variation = i[:j] + i[j+1:]
                # If any variation is safe, count it and break
                if safety_check([variation]):  # Wrap variation in a list
                    results += 1
                    break  # Stop checking other variations for this sublist
    return results

    
if __name__ == "__main__":
    main()