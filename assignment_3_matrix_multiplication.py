def reading_matrix_from_csv(filepath):
    with open(filepath, 'r') as f:
        matrix = []
        for line in f:
            row = line.strip().split(',')
            row = [int(value) for value in row]
            matrix.append(row)
    return matrix

def multiplying_matrix(mat1, mat2):
    rows = len(mat1)
    cols = len(mat2[0])
    cols2 = len(mat1[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform matrix multiplication
    for r in range(rows):
        for c in range(cols):
            for c1 in range(cols2):
                result[r][c] += mat1[r][c1] * mat2[c1][c]
    return result

def storing_in_csv(outputfile, output):
    with open(outputfile, 'w') as file:
        for row in output:
            row_string = ','.join(map(str, row))
            file.write(row_string + '\n')
    print(f"\nOutput stored in {outputfile}\n")

def main():
    # Specify file paths
    filemat1 = "mat1.csv"
    filemat2 = "mat2.csv"
    outputfile = "output.csv"

    # Read matrices from CSV
    mat1 = reading_matrix_from_csv(filemat1)
    print("\nMatrix 1\n")
    for row in mat1:
        print(row)

    mat2 = reading_matrix_from_csv(filemat2)
    print("\nMatrix 2\n")
    for row in mat2:
        print(row)

    # Multiply matrices
    print("\nMultiplying Matrix 1 and Matrix 2")
    output = multiplying_matrix(mat1, mat2)

    # Print result matrix
    print("\nThis is the output:\n")
    for row in output:
        print(row)

    # Store result in output CSV
    storing_in_csv(outputfile, output)

# Execute the program
main()
