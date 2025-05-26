#import os
import file_converter as fc
import tkinter as tk
from tkinter import filedialog, ttk

class MarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mark Generator")
        self.root.geometry("1200x400")

        self.tree = None
        self.create_components()

    def create_components(self):
        load_button = tk.Button(self.root, text="Load file", command=self.load_file)
        load_button.pack(anchor="nw", padx=5, pady=5)

        #table
        columns = ("Student", "Mark")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

    @staticmethod
    def process_file(file_path):
        marks_dict = fc.generate_marks(fc.csv_to_dict(file_path), 0, 10)
        print(f"Processing file {file_path}")
        return marks_dict


    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            data = self.process_file(file_path)
            self.update_table(data)


    def update_table(self, data):
        self.tree.delete(*self.tree.get_children())
        max_marks = max(len(marks) for marks in data.values())
        columns = ["Student"] + [i + 1 for i in range(max_marks)]
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        for student, marks in data.items():
            row = [student] + list(marks) + [""] * (max_marks - len(marks))
            self.tree.insert("", "end", values=row)

def main():

    #print(fc.generate_marks(fc.csv_to_dict("./5.1_temat.csv"), 0, 10))
    root = tk.Tk()
    app = MarkApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()