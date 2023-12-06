import tkinter
import random

root = tkinter.Tk()

root.configure(bg="skyblue")

root.title("My To Do List")

root.geometry("325x275")

tasks = []

tasks = ["Education","Study well"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task."
    txt_input.delete(0,"end")    

def del_task():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()    


lbl_title = tkinter.Label(root,text="To-do-list",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root,width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add task",fg="green",bg="white",command=add_task)
btn_add_task.grid(row=2,column=0)

btn_del_task = tkinter.Button(root, text="del task",fg="green",bg="white",command=del_task)
btn_del_task.grid(row=3,column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)


root.mainloop()
