import tkinter as tk
from tkinter import messagebox
from calculator import calculate_deposit_income # Импорт логики

def calculate_income():
    """Расчёт дохода по вкладу (обработчик GUI)"""
    try:
        s = float(entry_sum.get())
        p = float(entry_rate.get())
        d = float(entry_days.get())
        
        # Вызов чистой функции из calculator.py
        income = calculate_deposit_income(s, p, d)
        result_var.set(f"{income:.2f}")
    except ValueError as e:
        if "больше нуля" in str(e):
            messagebox.showerror("Ошибка", str(e))
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения!")

def clear_fields():
    entry_sum.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_days.delete(0, tk.END)
    result_var.set("")

def exit_program():
    if messagebox.askyesno("Выход", "Вы действительно хотите выйти?"):
        root.destroy()

# --- Создание главного окна ---
root = tk.Tk()
root.title("Калькулятор дохода по вкладу")
root.geometry("450x350")
root.resizable(False, False)

title_label = tk.Label(root, text="Расчёт дохода по банковскому вкладу", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

label_sum = tk.Label(frame_inputs, text="Сумма вклада (руб.):", width=25, anchor="w")
label_sum.grid(row=0, column=0, padx=5, pady=5)
entry_sum = tk.Entry(frame_inputs, width=20)
entry_sum.grid(row=0, column=1, padx=5, pady=5)

label_rate = tk.Label(frame_inputs, text="Годовая ставка (%):", width=25, anchor="w")
label_rate.grid(row=1, column=0, padx=5, pady=5)
entry_rate = tk.Entry(frame_inputs, width=20)
entry_rate.grid(row=1, column=1, padx=5, pady=5)

label_days = tk.Label(frame_inputs, text="Срок размещения (дней):", width=25, anchor="w")
label_days.grid(row=2, column=0, padx=5, pady=5)
entry_days = tk.Entry(frame_inputs, width=20)
entry_days.grid(row=2, column=1, padx=5, pady=5)

frame_result = tk.Frame(root)
frame_result.pack(pady=15)
label_result = tk.Label(frame_result, text="Доход (руб.):", font=("Arial", 11, "bold"))
label_result.grid(row=0, column=0, padx=5)
result_var = tk.StringVar()
label_result_value = tk.Label(frame_result, textvariable=result_var, font=("Arial", 11, "bold"), fg="blue")
label_result_value.grid(row=0, column=1, padx=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=15)

btn_calculate = tk.Button(frame_buttons, text="Рассчитать", command=calculate_income, width=12, bg="#4CAF50", fg="white")
btn_calculate.grid(row=0, column=0, padx=5)
btn_clear = tk.Button(frame_buttons, text="Очистить", command=clear_fields, width=12, bg="#2196F3", fg="white")
btn_clear.grid(row=0, column=1, padx=5)
btn_exit = tk.Button(frame_buttons, text="Выход", command=exit_program, width=12, bg="#f44336", fg="white")
btn_exit.grid(row=0, column=2, padx=5)

root.mainloop()