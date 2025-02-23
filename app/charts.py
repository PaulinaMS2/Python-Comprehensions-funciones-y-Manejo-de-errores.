import matplotlib.pyplot as plt

def generate_bar_char(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, textprops={'fontsize': 10})
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [11, 22, 33]
    # generate_bar_char(labels, values)
    generate_pie_chart(labels, values)