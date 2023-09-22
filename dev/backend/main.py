# This is a sample Python script.
import tkinter

import customtkinter as customtkinter
import firebase_admin
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkLabel, CTkFrame

from firebase_admin import credentials
from firebase_admin import firestore
import json
import pickle
import os
import time
import pandas as pd
import re
from tqdm import tqdm
from IPython.display import Javascript

from tkinter import *
from tkinter.ttk import *
import requests
from copy import deepcopy


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def load_dummy_data(db, upload=True):
    # coll: data > doc: slide > SINGLE FIELD {'slides':{"events":{}, "gadgets":{},...}
    # Use a breakpoint in the code line below to debug your script.
    final_data={"slides":{}}

    dummy_files=[x for x in os.listdir("./data")]

    for filename in dummy_files:
        with open("./data/"+filename, "r") as file:
            k=filename.replace(".json","") #k for final_data
            dict_=json.load(file)
            final_data['slides'].update(dict_)
    if upload==True:
        db.collection("data").document("data").set(final_data)


def first_type_changed(event):
    first_type_target = first_type.get()
    second_type_target = second_type_opts[first_type_opts.index(first_type_target)]
    second_type.config(value= second_type_target) #change values
    try:
        second_type.set(second_type_target[0])#select first
    except:
        second_type.set('')  #

def file_selection_changed(event):
    mode,target_2= modes_.get(), second_type.get()
    print("CHANGED", mode , target_2, event)

def show_error(message):
    # Show some error message
    CTkMessagebox(title="Error", message=message, icon="cancel")
def delete_data(target_idxs):
    # list of dicts
    #del target_idx
    global firebase_data
    print("TARGETS: ",target_idxs)
    changed_data= [x for i,x in enumerate(firebase_data[first_type.get()][second_type.get()]) if str(i) not in target_idxs]
    print(len(changed_data))
    new_firebase_data= deepcopy(firebase_data)
    del new_firebase_data[first_type.get()][second_type.get()]


    new_firebase_data[first_type.get()][second_type.get()]=changed_data
    firebase_data=new_firebase_data
    print("Deleted!", len(firebase_data[first_type.get()][second_type.get()]), len(old_firebase_data[first_type.get()][second_type.get()]))
    #delete previous rows
    for child in display_frame.winfo_children():
        child.grid_forget()
        child.destroy()
    #re insert rows
    for i,each in enumerate(firebase_data[first_type.get()][second_type.get()]):
        #row
        row_txt_val=f"{i} ==> {each['idx']} "
        row_txt= CTkLabel(display_frame,text=row_txt_val, width=300)
        row_txt.grid(column=0, row=i)

    data_changed(firebase_data, old_firebase_data)
    for child in bottom_frame.winfo_children():
        child.grid_forget()
        child.destroy()
    idx_inp.delete(0, END)
    action_feed.configure(text="Dati cancellati con successo.",fg_color="green")
    action_feed.after(action_update_interval, lambda: action_feed.configure(text='', fg_color= root.cget("fg_color")) )




def idx_inp_changed(idx_inp,mode):
    print("works",idx_inp.get())
    all_entries= [int(x) for x in re.split("\D", idx_inp.get()) if x!=""]
    print(all_entries)

    if mode=="Aggiungi":
        pass
    elif mode=="Modifica":
        if len(all_entries)>1:
            show_error(f"La modalità modifica accetta 1 elemento ma hai inserito\n{len(all_entries)} elementi: {all_entries}.\n\nInseriscine solo uno!")
            return
        if all_entries==[]:
            show_error(f"Occorre almeno un elemento!")
            return
    elif mode=="Cancella":
        if all_entries == []:
            show_error(f"Occorre almeno un elemento!")
            return
    #handle result
    handle_bottom_frame()

def clear(el): #root, frame
    list = el.grid_slaves()
    for l in list:
        l.destroy()

def update_rows_txt(frame):
    # delete previous rows
    for child in frame.winfo_children():
        child.grid_forget()
        child.destroy()
    # re insert rows
    for i, each in enumerate(firebase_data[first_type.get()][second_type.get()]):
        # row
        row_txt_val = f"{i} ==> {each['idx']} "
        row_txt = CTkLabel(frame, text=row_txt_val, width=300)
        row_txt.grid(column=0, row=i)
    #change bind fucntion according to mode
def handle_middle_frame():
    global firebase_data

    data_changed(firebase_data, old_firebase_data)
    state_label.configure(text= f"{first_type.get()} -> {second_type.get()} -> {modes_.get()}")


    target_1= first_type.get()
    target_2= second_type.get()
    mode= modes_.get()


    for child in  display_frame.winfo_children():
        child.configure(state='normal', fg_color=root.cget("fg_color"))
    idx_search_btn.configure(state='normal', fg_color=filter_btn.cget("fg_color"))
    idx_inp.configure(state='normal', fg_color=root.cget("fg_color"))

    for child in bottom_frame.winfo_children():
        child.grid_forget()
        child.destroy()

    for child in root.winfo_children():
        try:
             if child.cget('text')=='Aggiungi' or child.cget('text')=='Applica modifiche':
                 child.grid_forget()
                 child.destroy()
        except:
            pass

    idx_inp.delete(0,END)

    print(target_1, target_2, mode)
    target_data=firebase_data[target_1][target_2]
    display_data=[x["idx"] for x in target_data]

    # delete previous rows
    for child in display_frame.winfo_children():
        child.grid_forget()
        child.destroy()
    # re insert rows
    for i, each in enumerate(firebase_data[first_type.get()][second_type.get()]):
        # row
        row_txt_val = f"{i} ==> {each['idx']} "
        row_txt = CTkLabel(display_frame, text=row_txt_val, width=300)
        row_txt.grid(column=0, row=i)
    #change bind fucntion according to mode
    #change bind fucntion according to mode

    if mode=="Cancella":
        #select one or many
        for child in bottom_frame.winfo_children():
            child.grid_forget()
            child.destroy()

        pass
    elif mode=="Modifica":
        #select only one!
        pass

    #display_frame



    if mode=="Aggiungi":
        for child in display_frame.winfo_children():
            child.configure(state='disabled', fg_color="red")
        idx_search_btn.configure(state='disabled',fg_color="red")
        idx_inp.configure(state='disabled',fg_color="red")
        handle_bottom_frame()




def handle_bottom_frame():
    all_entries= [int(x) for x in re.split("\D", idx_inp.get()) if x!=""]
    if all_entries==[] and modes_.get()!="Aggiungi":
        return
    #remove old els
    for child in bottom_frame.winfo_children():
        child.grid_forget()
        child.destroy()
    mode= modes_.get()
    target_data=firebase_data[first_type.get()][second_type.get()]
    print("mode", mode)

    if mode=="Aggiungi":
        for i, k in enumerate([*target_data[0].keys()]):
            print("K", k)
            add_btn= customtkinter.CTkButton(root, text="Aggiungi", command=add_data)

            bottom_frame_row = CTkFrame(bottom_frame)
            row_label = CTkLabel(bottom_frame_row, text=k, width=150)
            row_input = customtkinter.CTkEntry(bottom_frame_row, placeholder_text="",
                                               width=150)

            row_label.grid(column=0, row=i)
            row_input.grid(column=1, row=i)

            bottom_frame_row.grid(column=0, row=i)
            add_btn.grid(row=5, column=0, pady=5)

            # a frame per row : Frame -> [key Label - value Entry]
            # per row:
            pass
    elif mode=="Modifica":
        for i,k in enumerate([*target_data[0].keys()]): # or target_data[all_entries[n]] in case of multi (not implemented, implemented only as single modify)
            print("K", k)
            bottom_frame_row = CTkFrame(bottom_frame)
            row_label = CTkLabel(bottom_frame_row, text=k, width=150)
            row_input = customtkinter.CTkEntry(bottom_frame_row, placeholder_text=target_data[all_entries[0]][k],width=150)

            row_label.grid(column=0, row=i)
            row_input.grid(column=1, row=i)

            bottom_frame_row.grid(column=0, row=i)

            #
            target_els = [x for x in firebase_data[first_type.get()][second_type.get()]]
            target_idxs = sorted([str(x) for x in all_entries if int(x) <= len(target_els) and int(x) >= 0])
            modify_btn= customtkinter.CTkButton(root,text="Applica modifiche", command=lambda:modify_data(target_idxs[0])) #only one idx
            modify_btn.grid(row=5, column=0, pady=5)

            pass
    elif mode=="Cancella":
        target_els=[x for x in firebase_data[first_type.get()][second_type.get()]]
        target_idxs=[* pd.Series(sorted([str(x) for x in all_entries if int(x)<=len(target_els) and int(x)>=0])).unique()] #idx starts from 0
        delete_els= customtkinter.CTkLabel(bottom_frame, text=f"Verranno cancellati: "+ ", ".join(target_idxs))
        delete_btn = customtkinter.CTkButton(bottom_frame, text="Elimina", command=lambda:delete_data(target_idxs), width=300)
        delete_els.grid(column=0,row=0)
        delete_btn.grid(column=0, row=1)

def modify_data(target_idx):
    global firebase_data
    print("MOD", target_idx)
    new_firebase_data = deepcopy(firebase_data)
    changed_data = {}
    #retrieve all keys and values
    for child in bottom_frame.winfo_children():
        row=child.winfo_children()
        print(row[0].cget('text'), row[1].get()=="", row[1].cget("placeholder_text"))
        key_=row[0].cget('text')
        if row[1].get()=="": #if not modified
            val_=row[1].cget("placeholder_text")
        else:
            val_= row[1].get()
        #check date format
        if key_=="date":
            if val_ !="":
                if len(re.split("\D", val_)[0]) != 4 or len(re.split("\D", val_)) != 3 \
                        or len(re.split("\D", val_)[1]) > 2 or len(re.split("\D", val_)[2]) > 2:
                    show_error("Il campo 'date'\ndeve rispettare il formato\n ANNO-MESE-GIORNO: 2023-08-30")
                    return
                #check len of month and date

                if len(re.split("\D", val_)[1])==1: #month
                    val_= re.split("\D", val_)[0] + "-0"+re.split("\D", val_)[1]+"-"+re.split("\D", val_)[2]
                if len(re.split("\D", val_)[2])==1: #day
                    val_= re.split("\D", val_)[0] + "-"+re.split("\D", val_)[1]+"-0"+re.split("\D", val_)[2]

                val_= "-".join(re.split("\D", val_))



        changed_data[key_]=val_
    print("CHANGED DATA",changed_data)
    new_firebase_data[first_type.get()][second_type.get()][int(target_idx)]=changed_data
    firebase_data= new_firebase_data
    data_changed(firebase_data, old_firebase_data)
    print("COMP", old_firebase_data==new_firebase_data)
    action_feed.configure(text="Dati modificati con successo.", fg_color="green")
    action_feed.after(action_update_interval, lambda: action_feed.configure(text='', fg_color= root.cget("fg_color")) )


def reset_data():
    global firebase_data
    global old_firebase_data
    firebase_data=old_firebase_data
    root.bind("<<FirstClick>>", handle_middle_frame()) #simulate first click
    action_feed.configure(text="Dati resettati con sucesso.", fg_color="green")
    action_feed.after(action_update_interval, lambda: action_feed.configure(text='', fg_color= root.cget("fg_color")) )


def add_data():
    global firebase_data
    global old_firebase_data
    print("ADD")
    new_firebase_data = deepcopy(firebase_data)
    changed_data = {}
    #retrieve all keys and values
    for child in bottom_frame.winfo_children():
        row=child.winfo_children()
        print(row[0].cget('text'), row[1].get()=="", row[1].cget("placeholder_text"))
        key_=row[0].cget('text')
        if row[1].get()=="": #if not modified
            val_=row[1].cget("placeholder_text")
        else:
            val_= row[1].get()
        changed_data[key_]=val_
    #no need to handle type key: if type=="" then no color in frontend

    if changed_data["idx"]=="":
        show_error("Il campo 'idx' è vuoto.\n Inserisci un valore prima di continuare!")
        return
    elif changed_data["idx"] in [x["idx"] for x in firebase_data[first_type.get()][second_type.get()]]:
        show_error("Valore per il campo 'idx' già esistente.\n Scegli un altro valore!")
        return

    print("CHANGED DATA", changed_data)
    new_firebase_data[first_type.get()][second_type.get()].append(changed_data)
    firebase_data = new_firebase_data
    data_changed(firebase_data, old_firebase_data)
    print("COMP", old_firebase_data == new_firebase_data)
    #add data to display_frame
    row_txt_val = f"{len(firebase_data[first_type.get()][second_type.get()])-1} ==> {changed_data['idx']}"
    row_txt = CTkLabel(display_frame, text=row_txt_val, width=300)
    row_txt.configure(state='disabled', fg_color="red")
    row_txt.grid(column=0, row=len(display_frame.winfo_children())-1)
    data_changed(firebase_data, old_firebase_data)
    action_feed.configure(text="Dati aggiunti con successo.",fg_color="green")
    action_feed.after(action_update_interval, lambda: action_feed.configure(text='', fg_color= root.cget("fg_color")) )





def data_changed(firebase_data, old_firebase_data):
    print("COMPARE", len(firebase_data[first_type.get()][second_type.get()]),  len(old_firebase_data[first_type.get()][second_type.get()]))
    if firebase_data==old_firebase_data:
        save_btn.configure(state="disabled")
        reset_btn.configure(state="disabled")
        return False
    elif firebase_data!=old_firebase_data:
        save_btn.configure(state="normal")
        reset_btn.configure(state="normal")
        return True




def ask_question(message):
    # get yes/no answers
    msg = CTkMessagebox(title="Attenzione!", message=message,
                        icon="question", option_1="Sì", option_2="No")
    response = msg.get()

    if response == "Sì":
        pass
    else:
       return

def on_closing():
    if save_btn.cget("state")=="normal":
        ask_question("Modifiche non salvate.\nSe esci senza salvare\n perderai tutte le modifiche.\nVuoi uscire senza salvare?")
    else:
        root.destroy()

def save_data_to_firebase():
    ask_question("Sei sicuro di voler salvare le modifiche?\n Non potrai tornare indietro.")
    global old_firebase_data
    global firebase_data
    db.collection("data").document("data").set(firebase_data)
    #override old_firebase_data
    old_firebase_data= firebase_data
    data_changed(firebase_data, old_firebase_data)
    action_feed.configure(text="Dati salvati con successo.", fg_color="green")
    action_feed.after(action_update_interval, lambda: action_feed.configure(text='', fg_color= root.cget("fg_color")) )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    action_update_interval=5000
    #auth to firebase
    cred = credentials.Certificate("./hulahoop-58ede-firebase-adminsdk-zezhj-65d9a46336.json")
    #firebase_admin.initialize_app(cred)
    firebase = firebase_admin.initialize_app(cred)
    db = firestore.client()
    #load_dummy_data(db)
    global firebase_data
    firebase_data=db.collection("data").document("data").get().to_dict()
    old_firebase_data= deepcopy(firebase_data) #use it to understand if changes occured

    #tkinter
    root= customtkinter.CTk()
    #root.geometry('800x800')
    w = 800  # width for the Tk root
    h = 650  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 1.3)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.minsize(300, 800)


    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=0)
    root.rowconfigure(2, weight=0)
    root.rowconfigure(3, weight=0)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=0)
    root.columnconfigure(2, weight=0)



    customtkinter.set_default_color_theme("blue")
    login_frame= customtkinter.CTkFrame(root)
    root.title("HulaHoop backend")


    #Insert password.txt before proceeding


    #Choose the type (e.g., "slides")

    #Choose the target (e.g., "events")

    # Choose the mode (modify, add, remove)

    #MODIFY MODE
    #show all the fields for the given results as a pair of label-input (key-value)
    #only allow for changing input fields

    #ADD MODE
    #show all the fields for the given results as a pair of label-input (key-value)
    #only allow for changing input fields

    #REMOVE MODE
    #show all saved entries and allow only for deleting entries
    #possibly allow for selecting entries to be removed

    filter_frame= CTkFrame(root)

    first_type_label= CTkLabel(filter_frame,text="Tipo esterno")
    second_type_label= CTkLabel(filter_frame,text="Tipo interno")
    modes_label= CTkLabel(filter_frame,text="Modalità")



    first_type_opts=[*firebase_data.keys()]
    second_type_opts=[[*firebase_data[x].keys()] for x in first_type_opts] #get dynamically
    first_type= Combobox(filter_frame,state="readonly", values=first_type_opts) #data > slides {"slides": "fourth_type":{...}}
    first_type.set(first_type_opts[0])
    second_type= Combobox(filter_frame,state="readonly", values=second_type_opts[0])
    try:
        second_type.set(second_type_opts[0][0])
    except:
        print("Empty dict")
    modes_= Combobox(filter_frame,state="readonly", values=["Aggiungi","Cancella", "Modifica"])
    modes_.set("Aggiungi")
    first_type.bind("<<ComboboxSelected>>", first_type_changed) #fill second_type value on first_Type  change

    filter_btn=customtkinter.CTkButton(filter_frame, text="Procedi", command=handle_middle_frame)

    middle_frame= CTkFrame(root, width=300)
    display_frame = CTkFrame(middle_frame, width=300)

    idx_inp = customtkinter.CTkEntry(middle_frame, placeholder_text="ID(s)", width=150)
    idx_search_btn = customtkinter.CTkButton(middle_frame, text="Cerca", command=lambda: idx_inp_changed(idx_inp, modes_.get()), width=150)

    footer_frame= customtkinter.CTkFrame(root)
    save_btn= customtkinter.CTkButton(footer_frame, text="Salva", command=lambda:save_data_to_firebase(), width=150)
    reset_btn= customtkinter.CTkButton(footer_frame, text="Resetta", command=lambda:reset_data(), width=150)

    #current state label
    state_label=customtkinter.CTkLabel(root,text=f"{first_type.get()} -> {second_type.get()} -> {modes_.get()}")

    action_frame=customtkinter.CTkFrame(root)
    #action_feed
    action_feed=customtkinter.CTkLabel(action_frame,text="", width=300, fg_color=root.cget("fg_color"))

    bottom_frame = CTkFrame(root,width=300)



    #middle_frame
    display_frame.grid(row=0,column=0)

    #display
    idx_inp.grid(column=0, row=1)
    idx_search_btn.grid(column=0, row=2)


    #filter_frame
    first_type_label.grid(row=0, column=0)
    second_type_label.grid(row=0, column=1)
    modes_label.grid(row=0,column=2)
    first_type.grid(row=1, column=0)
    second_type.grid(row=1, column=1)
    modes_.grid(row=1,column=2)
    filter_btn.grid(row=2, column=1)

    #footer_frame
    save_btn.grid(row=0,column=0)
    reset_btn.grid(row=0,column=1)

    #action_frame
    action_feed.grid(row=1, column=0)

    #root
    filter_frame.grid(row=0,column=0, columnspan=3,pady=15)
    state_label.grid(row=2, column=0)
    middle_frame.grid(row=3, column=0, columnspan=3)
    bottom_frame.grid(row=4, column=0, pady=15)
    footer_frame.grid(row=6, column=0, pady=10)
    action_frame.grid(row=7, column=0)




    root.bind("<<FirstClick>>", handle_middle_frame()) #simulate first click
    root.bind("<<SecondClick>>", handle_bottom_frame()) #simulate first click


    #simulate first click
    root.event_generate("<<FirstClick>>", when='tail')
    root.event_generate("<<SecondClick>>", when='tail')

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
