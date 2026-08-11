import matplotlib.pyplot as plt

subjects = ["Python", "Cloud", "AWS", "Terraform"]
students = [40, 20, 25, 26]

plt.pie(
    students,
    labels = subjects,
    autopct="%1.1f%%")

plt.title("Student data")

plt.show()
