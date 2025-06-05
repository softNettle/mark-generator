#import os
import file_converter as fc
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class MarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mark Generator")
        self.root.geometry("1200x400")

        self.tree = None
        self.file_path = None
        self.amount_entry = None
        self.original_data = None  # Сохраняем оригинальные данные

        self.create_components()

    def create_components(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(anchor="nw", padx=5, pady=5, fill="x")

        load_button = tk.Button(top_frame, text="Load file", command=self.load_file)
        load_button.pack(side="left", padx=(0, 10))

        tk.Label(top_frame, text="Number of Marks:").pack(side="left")
        vcmd = (self.root.register(self.validate_number), '%P')
        self.amount_entry = tk.Entry(top_frame, width=5, validate='key', validatecommand=vcmd)
        self.amount_entry.insert(0, "10")
        self.amount_entry.pack(side="left", padx=(0, 10))

        generate_button = tk.Button(top_frame, text="Generate Marks", command=self.generate_marks)
        generate_button.pack(side="left")

        # Таблица
        self.tree = ttk.Treeview(self.root, show="headings")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        # Настройка цветового стиля через теги
        self.tree.tag_configure("original", foreground="blue", font=("Arial", 10, "bold"))

    def validate_number(self, value):
        return value.isdigit() or value == ""

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            try:
                self.original_data = fc.csv_to_dict(self.file_path)
                #messagebox.showinfo("File Loaded", "File successfully loaded. Click 'Generate Marks' to process.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")
                self.original_data = None

    def generate_marks(self):
        if not self.file_path or not self.original_data:
            messagebox.showwarning("No File", "Please load a CSV file first.")
            return

        amount_text = self.amount_entry.get()
        if not amount_text.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number of marks.")
            return

        amount = int(amount_text)
        try:
            generated_data = fc.generate_marks(self.original_data, 0, amount)
            self.update_table(self.original_data, generated_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_table(self, original_data, generated_data):
        self.tree.delete(*self.tree.get_children())

        max_generated = max(len(marks) for marks in generated_data.values())
        columns = ["Student", "Original"] + [f"M{i + 1}" for i in range(max_generated)]
        self.tree["columns"] = columns

        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Student":
                self.tree.column(col, width=240, stretch=False)
            elif col == "Original":
                self.tree.column(col, width=100, stretch=False)
            else:
                self.tree.column(col, width=40, stretch=False, anchor="center")

        for student in original_data:
            orig_marks = original_data[student]
            gen_marks = generated_data.get(student, [])
            row = [student, ", ".join(map(str, orig_marks))] + list(gen_marks) + [""] * (max_generated - len(gen_marks))
            self.tree.insert("", "end", values=row, tags=("original",))

def main():
    root = tk.Tk()
    app = MarkApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
