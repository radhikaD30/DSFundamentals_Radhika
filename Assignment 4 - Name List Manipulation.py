def readName(lines):
    # Open the CSV file and read the names
    with open("names.csv", 'r') as f:
        lines.extend(f.readlines())

def loadIntoMatrix(lines, mat):
    # Load names into a matrix (row by row)
    for line in lines:
        names = line.strip().split(',')
        mat.append(names)

def convertToColumnMajor(mat):
    transpose = []
    n = max(len(row) for row in mat)  # Find the max row length

    # Convert to column major format
    for i in range(n):
        temp = ''
        for j in range(len(mat)):
            try:
                temp += mat[j][i]
            except IndexError:
                temp += ' '  # Handle shorter rows by adding spaces
        transpose.append(temp.rstrip())

    # Clear the original matrix and update with the transpose
    mat.clear()
    mat.extend(transpose)

def calculateCharacterLength(mat):
    # Calculate total length of all characters in the matrix
    total_length = sum(len(row) for row in mat)
    print("Total character length:", total_length)
    return total_length

def storeListAsString(mat):
    # Store the column-major matrix as a string in a text file
    with open("output.txt", "w") as file:
        for i in mat:
            file.write(i + '\n')
    print("\nMatrix stored in output.txt")

def main():
    lines = []
    mat = []

    # Reading names from CSV
    readName(lines)
    loadIntoMatrix(lines, mat)
    print("Loaded matrix:", mat)

    # Convert to column-major
    convertToColumnMajor(mat)
    print("Column-major matrix:", mat)

    # Calculate total character length
    calculateCharacterLength(mat)

    # Store the column-major matrix in output.txt
    storeListAsString(mat)

# Run the main function
main()
