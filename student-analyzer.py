import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data.csv"

class StudentAnalyzer:

    def __init__(self,file_path):
        self.df = pd.read_csv(file_path)

        self.df["Average"] = (
            self.df[["Math","Science","English"]]
            .mean(axis=1)
            .round(2)
        )

    def statistics(self):
        return self.df.describe().round(2)
    
    def top_student(self):
        return self.df.sort_values(
            by="Average",
            ascending=False
        ).head(3)
    
    def best_student(self):
        best_student = self.df.loc[self.df["Average"].idxmax()]
        return {
            "Name": best_student["Name"],
            "Average": best_student["Average"]
        }
    
    def lowest_student(self):
        lowest_student = self.df.loc[self.df["Average"].idxmin()]
        return {
            "Name": lowest_student["Name"],
            "Average": lowest_student["Average"]
        }
    
    def student_report(self, name):
        result = self.df[self.df["Name"].str.lower() == name.lower()]
        if result.empty:
            return f"{name} not found."

        return result.to_string(index=False)
    
    def showBarPlot(self):
        sns.barplot(data=self.df,x="Name",y="Average")
        plt.show()

    def showStudentPlot(self, name):

        student = self.df[
            self.df["Name"].str.lower() == name.lower()
        ]

        if student.empty:
            print(f"{name} not found.")
            return

        student = student.iloc[0]

        subjects = ["Math", "Science", "English"]

        marks = [
            student["Math"],
            student["Science"],
            student["English"]
        ]

        sns.barplot(
            x=subjects,
            y=marks
        )

        plt.title(f"{name}'s Marks")

        plt.xlabel("Subjects")
        plt.ylabel("Marks")

        plt.show()
    
def main():

    analyzer = StudentAnalyzer(file_path)

    while True:
        print("\n===== STUDENT ANALYZER SYSTEM =====")
        print("1. Student Report")
        print("2. Top Students")
        print("3. Best Student")
        print("4. Lowest Student")
        print("5. Statistic")
        print("6. Avg BarPlot")
        print("7. Student BarPlot")
        print("8. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            name = input("Enter name:").strip()
            print(analyzer.student_report(name))
        elif choice == "2":
            print(analyzer.top_student())
        elif choice == "3":
            print(analyzer.best_student())
        elif choice == "4":
            print(analyzer.lowest_student())
        elif choice == "5":
            print(analyzer.statistics())
        elif choice == "6":
            analyzer.showBarPlot()
        elif choice == "7":
            name = input("Enter name:").strip()
            analyzer.showStudentPlot(name)
        elif choice == "8":
            print("Thank you for using Student Analyzer.")
            break
        else:
            print("Invalid Choice! Please enter 1-8.")

if __name__ == "__main__":
    main()