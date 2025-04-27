#import os
import file_converter as fc
import tkinter as tk
from tkinter import filedialog


def process_file(file_path):
    marks_dict = fc.generate_marks(fc.csv_to_dict("./5.1_temat.csv"), 0, 10)
    print(f"Processing file {file_path}")


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        process_file(file_path)


def create_window():
    root = tk.Tk()
    root.title("Mark generator")
    root.mainloop()

def main():

    print(fc.generate_marks(fc.csv_to_dict("./5.1_temat.csv"), 0, 10))
    create_window()


if __name__ == '__main__':
    main()