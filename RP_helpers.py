import matplotlib.pyplot as plt
import numpy as np

def plot_multi_bar_graph(dictionaries: list[dict], legend:list[str]):
    # Set the width of the bars
    bar_width = 1.0 / (len(dictionaries) + 1)
    labels = dictionaries[0].keys()
        
    # Set the positions of the bars on the x-axis
    r_values = [np.arange(len(labels))]
    for i in range(len(dictionaries) - 1):
        r_values.append([x + bar_width for x in r_values[i]])
    
    # Plot the bar graph
    for i, dictionary in enumerate(dictionaries):
        values = list(dictionary.values())
        r = r_values[i]
        plt.bar(r, values, color=np.random.rand(3,), width=bar_width, edgecolor='white', label=list(dictionary.keys())[0])
    
    # Add labels and title
    plt.xlabel('Models')
    plt.xticks([r + (bar_width * (len(dictionaries) - 1) / 2) for r in r_values[0]], labels)
    plt.ylabel('Accuracy')
    plt.title("Model Accuracies")
    
    # Add legend
    plt.legend(legend, loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=len(dictionaries))
    
    # Show the plot
    plt.tight_layout()
    plt.show()