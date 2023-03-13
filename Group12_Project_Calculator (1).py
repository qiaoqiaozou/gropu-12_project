#!/usr/bin/env python
# coding: utf-8

# # Group12
# # March 9, 2023
# ## Member:
# ### Natthakorn Rattanakun
# ### Digvijaysinh Hemantsinh Devdhara
# ### Mohammand Shahid Sirajbhai Jamadar
# ### Qiaoqiao Zou
# ### Pongsatorn Krabuansang

# In[2]:


from math import sqrt, pi, e
import tkinter as tk

TEXT_str = ''


def get_value():
    try:
        print('FUNCTION:', TEXT_str)
        value = str(eval(TEXT_str))
        return value
    except BaseException:
        print('wrong！')
        return ''
def main():
    root = tk.Tk()
    root.title("CALCULATOR")
    root.geometry('630x265+250+250')
    root.resizable(False, False)

    text_list = [
        'AC', 'DEL', '( )', '%','^',
        '7', '8', '9', '+', 'sqrt()',
        '4', '5', '6', '-', 'e',
        '1', '2', '3', '*', 'pi',
        '.', '0', '=', '/', 'cancel',
    ]

    Entry_word = tk.Entry(root, width=30, font=('Arial', 15))
    Entry_word.grid(row=0, column=0, columnspan=4)
    
    def CloseCal():
        root.destroy()
        exit()

    def btn_command(idx=None):
        global TEXT_str
        s = text_list[idx]
        print("INPUT：", s)
        if s == '=':
            # Press the equal sign to call the evaluation function
            value_str = get_value()
            TEXT_str = ''  # Expression sought
            Entry_word.delete(0, tk.END)  
            Entry_word.insert(tk.END, value_str)  
        elif s == 'AC':
            TEXT_str = ''  
            Entry_word.delete(0, tk.END)  
        elif s == 'DEL':
            # print(Entry_word.index(tk.INSERT))
            Entry_word.delete(Entry_word.index(tk.INSERT) - 1,
                              Entry_word.index(tk.INSERT))
            TEXT_str = Entry_word.get()
        elif s == '( )':
            Entry_word.insert(tk.INSERT, '()')
            TEXT_str = Entry_word.get()
        elif s == "^":
            Entry_word.insert(tk.INSERT, "pow(,)")
            TEXT_str = Entry_word.get()
        elif s == "%":
            Entry_word.insert(tk.INSERT, "*0.01")
            TEXT_str = Entry_word.get()
        elif s == "cancel":
            CloseCal()
        else:
            Entry_word.insert(tk.INSERT, s)
            TEXT_str = Entry_word.get()

    key = 0
    for i in range(1, 6):
        for j in range(0, 5):
            if text_list[key] == "=":
                btn = tk.Button(
                    root,
                    text=text_list[key],
                    width=10,
                    height=2,
                    relief=tk.GROOVE,
                    command=lambda idx=key: btn_command(idx),
                    bg="orange"
                )
            else:
                btn = tk.Button(
                    root,
                    text=text_list[key],
                    width=10,
                    height=2,
                    relief=tk.GROOVE,
                    command=lambda idx=key: btn_command(idx))
            btn.grid(row=i, column=j)
            key += 1

    root.mainloop()


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




