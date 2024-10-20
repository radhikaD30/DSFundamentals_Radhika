import matplotlib.pyplot as plt
import pandas as pd

# CSV file name
csv_file = "marks.csv"  # Ensure this file is in the same directory as your script

# Function to read the CSV file
def read_file(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

# Function to count the gender distribution
def count_gender(df):
    if 'Gender' not in df.columns:
        print("Gender column is missing")
        return None
    else:
        gender_counts = df['Gender'].value_counts()
        male = gender_counts.get('Male', 0)
        female = gender_counts.get('Female', 0)
        return [male, female]

# Function to count subject results (Passed/Failed)
def count_subject_result(df, subject):
    if subject not in df.columns:
        print(f'{subject} column is missing')
        return None
    else:
        passed = df[df[subject] >= 40].shape[0]
        failed = df[df[subject] < 40].shape[0]
        return [passed, failed]

# Function to plot the pie charts
def plot_all_piecharts(gen, mathmk, engmk):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Gender Pie Chart
    axs[0].pie(gen, labels=["Male", "Female"], autopct='%1.1f%%', colors=['lightblue', 'pink'])
    axs[0].set_title("Gender Distribution")

    # Math Result Pie Chart
    axs[1].pie(mathmk, labels=["Passed", "Failed"], autopct='%1.1f%%', colors=['green', 'red'])
    axs[1].set_title("Math Pass/Fail Distribution")

    # English Result Pie Chart
    axs[2].pie(engmk, labels=["Passed", "Failed"], autopct='%1.1f%%', colors=['green', 'red'])
    axs[2].set_title("English Pass/Fail Distribution")

    plt.show()

# Main function to read the file and plot the pie charts
def main():
    df = read_file(csv_file)
    if df is None:
        return

    gen = count_gender(df)
    math = count_subject_result(df, 'MathMarks')
    eng = count_subject_result(df, 'EnglishMarks')

    if gen is not None and math is not None and eng is not None:
        plot_all_piecharts(gen, math, eng)

# Run the main function
main()
