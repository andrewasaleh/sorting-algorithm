import tkinter as tk
import random

# Import library matplotlib (pip install matplotlib)
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# Import sorting algorithms files
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort

# Function generates a random array given the index we had set with the number scale
def generate_array():
    # this gets the value of the scale
    array_size = scale_var.get()  

    # Define a global variable to hold the generated array values
    global random_array   
    # within the index size, this will create random ints, from 0 to 500
    random_array = [random.randint(0, 500) for _ in range(array_size)]  
    
    # outputs the array to the window
    # value_label.config(text="Array to be sorted: {}".format(random_array))  

    # Call the graph embedding function directly with the generated array
    embed_graph(random_array)  

    return random_array # return the array in order to pass to the alogorithms

def get_index_value(): 
     # outputs the selected index to the window
    value_label.config(text="Selected Value: {}".format(scale_var.get()))


def perform_algorithms(): # this function executes the sorting function if they are checked off


    generated_array = generate_array() # creating a variable for the generated array
    
    # Doing individual if statements here, because they're all independent from each other
def sort_with_merge_sort():
    if random_array:  # Check if the array has been generated
        sorted_array = merge_sort(random_array.copy())  # Sort the array using merge sort
        embed_graph(sorted_array)  # Embed the graph with the sorted array

def sort_with_bubble_sort():
    if random_array:  # Check if the array has been generated
        sorted_array = bubble_sort(random_array.copy())  # Sort the array using bubble sort
        embed_graph(sorted_array)  # Embed the graph with the sorted array

def sort_with_quick_sort():
    if random_array:  # Check if the array has been generated
        sorted_array = quick_sort(random_array.copy())  # Sort the array using quick sort
        embed_graph(sorted_array)  # Embed the graph with the sorted array



##################################################################
##### Below is all the GUI code ##########################

# below creates the graph window (dynamic graph based on the generated array)
def embed_graph(values):    
    # Generate labels for the bars in the bar graph
    labels = [f' {i+1}' for i in range(len(values))]
    
    # Create a new Figure object with a specified size and dpi
    fig = Figure(figsize=(5, 4), dpi=100)
    
    # Get the Axes object from the Figure object
    ax = fig.add_subplot(111)
    
    # Clear any previous graph from the Axes object
    ax.clear()
    
    # Plot the bar graph with the given values and labels
    ax.bar(labels, values, color='darkorchid', width=.5)
    
    # Rotate the x-axis labels by % and adjust font size
    ax.tick_params(axis='x', rotation=40, labelsize=8)
    
    # Embed the Figure object in a Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    
    # Draw the Figure object on the FigureCanvasTkAgg object
    canvas.draw()

    # Embed the FigureCanvasTkAgg object in the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# below creates the main window
root = tk.Tk()
root.title("Pixel Pioneers Gui")

# Frame to hold buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Sorting algorithm buttons placed inside the frame
merge_sort_button = tk.Button(button_frame, text="Merge Sort", command=sort_with_merge_sort)
merge_sort_button.pack(side=tk.LEFT, padx=5)

bubble_sort_button = tk.Button(button_frame, text="Bubble Sort", command=sort_with_bubble_sort)
bubble_sort_button.pack(side=tk.LEFT, padx=5)

quick_sort_button = tk.Button(button_frame, text="Quick Sort", command=sort_with_quick_sort)
quick_sort_button.pack(side=tk.LEFT, padx=5)

# Create a scale widget
scale_var = tk.IntVar()  # Fixed to int as we cannot have a double index size
scale = tk.Scale(root, variable=scale_var, from_=1, to=50, orient="horizontal", length=300)
scale.pack(pady=20)

# Create a button to get the selected value
get_index_value_button = tk.Button(root, text="Set Index", command=get_index_value)
get_index_value_button.pack()

# Create a label to display the selected value
value_label = tk.Label(root, text="Index Value: {}".format(scale_var.get()))
value_label.pack()

# Button to generate and display the array
generate_array_button = tk.Button(root, text="Generate Array", command=generate_array)
generate_array_button.pack()

# Running the GUI
root.mainloop()