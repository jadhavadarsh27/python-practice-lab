import matplotlib.pyplot as plt

students = [20, 30, 40]
subjects = ["Aws", "GCP", "Azure"]

plt.pie(
    students,
    labels =  subjects,
    autopct = "%1.1f%%")

plt.title("Student Information")

plt.show()
