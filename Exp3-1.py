import matplotlib.pyplot as plt

# Data to plot
# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice
n = int(input("Enter No. of elements: "))
labels = list(map(str, input("Enter list of labels: ").split()))
sizes = list(map(int, input("Enter list of sizes: ").split()))
colors = list(map(str, input("Enter list of colors: ").split()))
explode = [0]*n

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()