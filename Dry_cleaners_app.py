from tkinter import *
import sqlite3
from datetime import date
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *

treeview_counter=0
search_records=[]
clothes=[]
prices=[]
clothe_ID=[]
database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
database_cursor=database_connect.cursor()
database_cursor.execute("SELECT ID,clothe_name,clothe_price from CLOTHES")
clothes_all=database_cursor.fetchall()
for i in range(len(clothes_all)) :
    clothe_ID.append(clothes_all[i][0])
    clothes.append(clothes_all[i][1])
    prices.append(clothes_all[i][2])
main_window=Tk()
#Frame of the buttons 
Buttons_frame=Frame(main_window,bg='grey',width=400,height=190)
Buttons_frame.place(x=430,y=500)
#window things
main_window.title("Pressing El fessi")
main_window.attributes('-fullscreen', True)  
main_window.bind("<F11>",lambda event: main_window.attributes("-fullscreen",not main_window.attributes("-fullscreen")))
main_window.bind("<Escape>",lambda event: main_window.attributes("-fullscreen",False))
widthx=main_window.winfo_screenwidth()
heighty=main_window.winfo_screenheight()
main_window.geometry(str(widthx)+"x"+str(heighty))
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
   background="silver",
   foreground="black",
   rowheight=25,
   fieldbackground="silver"
   )
style.map('Treeview',
    background=[('selected','green')])
#____________________________________________________
#client Name,Prename,Phone number Entries in the main_window
Name_client_Label=Label(width=16,text="Nom de client :",font=('arial',18))
Name_client_Label.place(x=0,y=10)
Name_client_Entry=Entry(width=16,font=('arial',18))
Name_client_Entry.place(x=220,y=10)
Prename_client_Label=Label(width=15,text="Prénom client:",font=('arial',18))
Prename_client_Label.place(x=0,y=60)
Prename_client_Entry=Entry(width=16,font=('arial',18))
Prename_client_Entry.place(x=220,y=60)
Numero_tlf_client=Label(width=15,text="Numero Client :",font=('arial',18))
Numero_tlf_client.place(x=5,y=105)
Numero_tlf_Entry=Entry(width=16,font=('arial',18))
Numero_tlf_Entry.place(x=220,y=105)
#______________________________________________________
#clothes and it quantity choices 
clothes_name=StringVar()
clothes_name.set("Choisir")
clothes_choice_label=Label(width=12,text="Vêtements :",font=('arail',18))
clothes_choice_label.place(x=6,y=170)
clothes_choice=OptionMenu(main_window,clothes_name,*clothes)
clothes_choice.place(x=220,y=165)
clothes_choice.config(font='arial')
quantity=[1,2,3,4,5,6,7,8,9,10]
clothes_choice_quantity=Label(width=12,text="Quantité  :",font=("araial",18))
clothes_choice_quantity.place(x=1,y=220)
quantity_value=StringVar()
quantity_value.set(1)
clothes_choice_quantity_drop=OptionMenu(main_window,quantity_value,*quantity)
clothes_choice_quantity_drop.place(x=220,y=220)
clothes_choice_quantity_drop.config(font='arial')
#_______________________________________________________
#price of the commands it changes everytime a new command is added
Prix_total_label=Label(width=11,text="Prix total :",font=('arial',18))
Prix_total_label.place(x=0,y=370)
Prix_total_label_value=Label(width=11,text=" 0 ",font=("arial",18))
Prix_total_label_value.place(x=120,y=370)
#________________________________________________________
to_add_inside_sql=[]
price_total=0
def ajouter_commande() :
    global to_add_inside_sql
    global treeview_counter
    global price_total
    to_add_inside_sql.append((Name_client_Entry.get(),Prename_client_Entry.get(),Numero_tlf_Entry.get(),clothe_ID[clothes.index(clothes_name.get())],clothes_name.get(),quantity_value.get(),int(prices[clothes.index(clothes_name.get())]*int(quantity_value.get()))))
    commands_treeview.insert('','end',iid=treeview_counter,values=(Name_client_Entry.get(),Prename_client_Entry.get(),Numero_tlf_Entry.get(),clothes_name.get(),quantity_value.get(),int(prices[clothes.index(clothes_name.get())]*int(quantity_value.get()))))
    treeview_counter+=1
    price_total+=(int(prices[clothes.index(clothes_name.get())]*int(quantity_value.get())))
    Prix_total_label_value.config(text=price_total)
    quantity_value.set(1)
    clothes_name.set("Choisir")
#commande -> add to the treeview in the main page 


Add_commande_main_window=CTkButton(command = ajouter_commande,corner_radius=15,fg_color="grey",width=50,height=50,text="Ajouter la commande",text_color="black",text_font=('arial',15)
,hover=True,hover_color='green')
Add_commande_main_window.place(x=30,y=280)
#_________________________________________________
#paid or no buttons and label
paid_state=""
def YES_paid() :
   global paid_state
   paid_state="OUI"
   paid_label_answer.config(text="Payé ou pas: OUI",fg='green')
def NO_paid() :
    global paid_state
    paid_state="NON"
    paid_label_answer.config(text="Payé ou pas: NON",fg='red')
paid_label=Label(width=13,text="Payé ou pas",font=('arial',18))
paid_label.place(x=0,y=450)
paid_YES=Button(text="OUI",font=("arial",18),width=5,bg='green',command=YES_paid)
paid_YES.place(x=255,y=450)
paid_No=Button(text="NON",command=NO_paid,bg='red',font=('arial',18),width=5)
paid_No.place(x=170,y=450)
paid_label_answer=Label(width=15,text="Payé ou pas:",font=('arial',18))
paid_label_answer.place(x=0,y=520)
#_____________________________________________
#last button which add the commands to the data base 
def save_commande() :
      global paid_state
      global to_add_inside_sql
      global price_total
      global treeview_counter
      database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
      database_cursor=database_connect.cursor()
      for i in range(len(to_add_inside_sql)) :
        today=date.today()
        hour =datetime.now()
        minute=datetime.now()
        seconds=datetime.now()
        database_cursor.execute("INSERT INTO COMMANDE(name_client,prename_client,phone_client,date_commande,hour_commande,clothe_ID,clothe_name,clothe_quantity,Paid_y_n,clothe_total_price) VALUES (?,?,?,?,?,?,?,?,?,?)",
      (to_add_inside_sql[i][0],to_add_inside_sql[i][1],to_add_inside_sql[i][2],str(today),str(hour.hour)+':'+str(minute.minute)+':'+str(int(seconds.second)+i),to_add_inside_sql[i][3],to_add_inside_sql[i][4],to_add_inside_sql[i][5],paid_state,to_add_inside_sql[i][6]))
        database_connect.commit()
        Name_client_Entry.delete(0,END)
        Prename_client_Entry.delete(0,END)
        Numero_tlf_Entry.delete(0,END)
        paid_label_answer.config(text="Payé ou pas:",fg='black')
        clothes_name.set("Choisir")
        quantity_value.set(1)
        price_total=0
        Prix_total_label_value.config(text=price_total)
        for records in commands_treeview.get_children() :
            commands_treeview.delete(records)
      treeview_counter=0
      to_add_inside_sql=[]
      messagebox.showinfo("Terminer!","la commande est faite !")
End_commande_button=CTkButton(command=save_commande,corner_radius=15,fg_color="green",width=70,height=70,text="Terminer la commande",text_color="black",text_font=('arial',15)
,hover=True,hover_color='light green')
End_commande_button.place(x=20,y=600)
#_____________________________________________
#frame and treeview commands
commands_frame=Frame(main_window)
commands_frame.place(x=500,y=100)
commands_treeview=ttk.Treeview(columns=(1,2,3,4,5,6),show='headings',height=9)
commands_treeview.place(x=600,y=50)
commands_treeview.heading(1,text='Nom_client')
commands_treeview.column("#1",anchor=CENTER, stretch=NO, width=120)
commands_treeview.heading(2,text='Prénom_client')
commands_treeview.column("#2",anchor=CENTER, stretch=NO, width=120)
commands_treeview.heading(3,text='Numero_client')
commands_treeview.column("#3",anchor=CENTER, stretch=NO, width=150)
commands_treeview.heading(4,text='vêtements')
commands_treeview.column("#4",anchor=CENTER, stretch=NO, width=160)
commands_treeview.heading(5,text='Quantité')
commands_treeview.column("#5",anchor=CENTER, stretch=NO, width=60)
commands_treeview.heading(6,text='Prix')
commands_treeview.column("#6",anchor=CENTER, stretch=NO, width=90)
#____________________________________________________________________
#delete a commande from the treeview 
def delete_selected() :
    global treeview_counter
    global to_add_inside_sql 
    global price_total
    x=commands_treeview.focus()
    price_total-=int(to_add_inside_sql[int(x)][6])  
    to_add_inside_sql.pop(int(x))
    treeview_counter-=1
    for i in commands_treeview.get_children() :
        commands_treeview.delete(i)
    for i in range(len(to_add_inside_sql)) :
        commands_treeview.insert('','end',iid=i,values=(to_add_inside_sql[i][0],to_add_inside_sql[i][1],to_add_inside_sql[i][2],to_add_inside_sql[i][4],to_add_inside_sql[i][5],to_add_inside_sql[i][6]))
    Prix_total_label_value.config(text=price_total)
    commands_frame.update() 
    commands_treeview.update()
Delete_from_treeviex=CTkButton(text="Effacer la Commande",hover=True,hover_color='green',
width=200,height=50,text_font=('arial',15),corner_radius=15,text_color='black',fg_color='red',command=delete_selected)
Delete_from_treeviex.place(x=600,y=310)
#____________________________________________________________________
#all records
def show_all_records() :
    database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
    database_cursor=database_connect.cursor()
    database_cursor.execute("SELECT name_client,prename_client,phone_client,date_commande,hour_commande,sum(clothe_total_price),Paid_y_n from COMMANDE where Paid_y_n='OUI' GROUP BY phone_client,name_client,prename_client order by phone_client ASC,date_commande ASC,hour_commande ASC")
    all_record=database_cursor.fetchall()
    records_of_clients=Toplevel()
    records_of_clients.title("Records de clients")
    records_of_clients.geometry(str(widthx)+"x"+str(heighty))
    all_records_frame=Frame(records_of_clients)
    all_records_frame.place(x=0,y=0)
    all_records_treeview=ttk.Treeview(records_of_clients,columns=(1,2,3,4,5,6,7),show='headings',height=25)
    all_records_treeview.place(x=0,y=0)
    all_records_treeview.heading(1,text='Nom_client')
    all_records_treeview.column("#1",anchor=CENTER, stretch=NO, width=120)
    all_records_treeview.heading(2,text='Prénom_client')
    all_records_treeview.column("#2",anchor=CENTER, stretch=NO, width=120)
    all_records_treeview.heading(3,text='Numero')
    all_records_treeview.heading(4,text='date_commande')
    all_records_treeview.heading(5,text='heur_commande')
    all_records_treeview.heading(6,text='prix_total')
    all_records_treeview.heading(7,text='Payé')
    sum_of_prices_amount=0
    amount_of_clients=len(all_record)
    for i in range(len(all_record)) :
        all_records_treeview.insert('',"end",iid=i,values=(all_record[i][0],all_record[i][1],all_record[i][2],all_record[i][3],all_record[i][4],all_record[i][5],all_record[i][6]))
        sum_of_prices_amount+=int(all_record[i][5])
    database_connect.commit()
    label_all_clients=Label(records_of_clients,fg='red',text="cette option vous montre\n tous les clients et leurs commandes totales qui ont été payées",font='arial')
    label_all_clients.place(x=400,y=heighty-200)
    sum_of_prices=Label(records_of_clients,fg='green',bg='black',text='bénéfices totales= '+"{:,.2f}".format(sum_of_prices_amount)+' dt',font=('arial',18))
    sum_of_prices.place(x=widthx-500,y=heighty-200)
    amount_of_clients_label=Label(records_of_clients,fg='white',bg='black',text='Nombre de clients :'+str(amount_of_clients),font=('arial',18))
    amount_of_clients_label.place(x=widthx-500,y=heighty-150)

all_records=CTkButton(command=show_all_records,corner_radius=15,fg_color="black",width=150,height=70,text="Tous les clients",text_color="white",text_font=('arial',15),bg_color='grey',
hover=True,hover_color='black')
all_records.place(x=640,y=heighty-350)
#_________________________________________________________________
#search about a commande 
treeview_search_counter=0
def search_about_commande () :
    search_window=Toplevel()
    search_window.geometry(str(widthx-100)+"x700")
    search_window.title("rechercher un client")
    Numero_tlf_client_search_label=Label(search_window,text="Numero de client :",font=('arial',12))
    Numero_tlf_client_search_label.place(x=0,y=10)
    Numero_tlf_client_search_entry=Entry(search_window,width=20,font='arial')
    Numero_tlf_client_search_entry.place(x=190,y=10)
    def search_about_client() :
       global treeview_search_counter
       global search_records
       database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
       database_cursor=database_connect.cursor()
       database_cursor.execute("SELECT name_client,prename_client,phone_client,date_commande,hour_commande,sum(clothe_total_price) as Total_commade,Paid_y_n from COMMANDE where phone_client=('%s') and Paid_y_n='NON' group by date_commande,name_client "%str(Numero_tlf_client_search_entry.get()))
       search_records=database_cursor.fetchall()
       for i in range(len(search_records)) :
            commands_treeview_search.insert('','end',iid=treeview_search_counter,values=(search_records[i][0],search_records[i][1],search_records[i][2],search_records[i][3],search_records[i][4],search_records[i][5],search_records[i][6]))
            treeview_search_counter+=1
       treeview_search_counter=0
       database_connect.commit()
    search_button=Button(search_window,width=10,text="chercher ",height=2,command=search_about_client)
    search_button.place(x=420,y=0)
    search_window.bind('<Return>',search_about_client)
    commands_frame_search=Frame(search_window)
    commands_frame_search.place(x=0,y=100)
    commands_treeview_search=ttk.Treeview(search_window,columns=(1,2,3,4,5,6,7),show='headings',height=9)
    commands_treeview_search.place(x=20,y=70)
    commands_treeview_search.heading(1,text='Nom_client')
    commands_treeview_search.column("#1",anchor=CENTER, stretch=NO, width=120)
    commands_treeview_search.heading(2,text='Prénom_client')
    commands_treeview_search.heading(3,text='Numero_client')
    commands_treeview_search.heading(4,text='date_commande')
    commands_treeview_search.heading(5,text='heur_commande')
    commands_treeview_search.heading(6,text='prix_total')
    commands_treeview_search.heading(7,text='Payé')
    def paid_done() :
       global search_records
       x=commands_treeview_search.focus()
       database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
       database_cursor=database_connect.cursor()
       phone_get=search_records[int(x)][2]
       name_get=search_records[int(x)][0]
       database_cursor.execute("UPDATE COMMANDE set Paid_y_n='OUI' where Paid_y_n='NON' and phone_client=('%s') and name_client=('%s')"%(phone_get,name_get))
       database_connect.commit()
       messagebox.showinfo("Terminer !","la commande est faite ! :) ")
       search_window.destroy()
       
    client_paid_done=Button(search_window,width=15,text="PAYE",height=2,font="arial",bg="green",command=paid_done)
    client_paid_done.place(x=50,y=400)
command_search=CTkButton(command=search_about_commande,corner_radius=15,bg_color='grey',fg_color="dark orange",width=70,height=70,text="Chercher un commande",text_color="black",text_font=('arial',10)
,hover=True,hover_color='Orange')
command_search.place(x=450,y=heighty-350)
#_______________________________________________________________________
#change the price of a commande
def changing_clothes_infos() :
    changing_window=Toplevel()
    changing_window.title("Changer le prix")
    changing_window.geometry("500x"+str(heighty-100))
    commands_frame_search=Frame()
    commands_frame_search.place(x=0,y=10)
    commands_frame_search_treeview=ttk.Treeview(changing_window,columns=(1,2),show='headings',height=19)
    commands_frame_search_treeview.place(x=0,y=10)
    commands_frame_search_treeview.heading(1,text='Nom des vêtements')
    commands_frame_search_treeview.column('#1',anchor=CENTER,width=250)
    commands_frame_search_treeview.heading(2,text='Prix des vêtements')
    commands_frame_search_treeview.column('#2',anchor=CENTER,width=250)
    for i in range(len(clothes)) :
        commands_frame_search_treeview.insert('','end',iid=i,values=(clothes[i],prices[i]))
    def change_price_fun() :
       database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
       database_cursor=database_connect.cursor()
       x=commands_frame_search_treeview.focus()
       database_cursor.execute("UPDATE CLOTHES set clothe_price =(?) where clothe_name=(?)",(float(change_entry.get()),clothes[int(x)]))
       prices[int(x)]=change_entry.get()
       database_connect.commit()
       change_entry.delete(0,END)
       messagebox.showinfo("Terminer!","le changement est fait :) !")
    change_price=Button(changing_window,width=10,height=1,text="changer",font='arial',command=change_price_fun)
    change_price.place(x=200,y=519)
    change_entry=Entry(changing_window,width=15,font='arial')
    change_entry.place(x=0,y=519)

change_price_commande=CTkButton(main_window,command=changing_clothes_infos,corner_radius=15,fg_color="pink",width=70,height=70,text="Changer le prix",text_color="black",text_font=('arial',15),bg_color="grey",hover=True,hover_color='light pink')
change_price_commande.place(x=640,y=heighty-270)
#_____________________________________________________
#change the theme of the screen 
theme_counter=0
def change_theme() :
    global theme_counter 
    theme_counter+=1
    if theme_counter%2!=0 :
        #black theme 
        Theme_Button.config(bg='white',fg='black')
        main_window.config(bg='black')
        Name_client_Label.config(bg='black',fg="white")
        Prename_client_Label.config(bg='black',fg="white")
        Numero_tlf_client.config(bg='black',fg="white")
        clothes_choice_label.config(bg='black',fg="white")
        paid_label.config(bg='black',fg="white")
        clothes_choice_quantity.config(bg='black',fg="white")
        paid_label_answer.config(bg='black',fg="white")
        Prix_total_label.config(bg='black',fg="white")
        Prix_total_label_value.config(bg='black',fg="white")
        delete_client_Label.config(bg='black',fg='red')
    else :
        Theme_Button.config(bg='black',fg='white')
        main_window.config(bg='SystemButtonFace')
        Name_client_Label.config(bg='SystemButtonFace',fg='black')
        Prename_client_Label.config(bg='SystemButtonFace',fg="black")
        Numero_tlf_client.config(bg='SystemButtonFace',fg="black")
        clothes_choice_label.config(bg='SystemButtonFace',fg="black")
        paid_label.config(bg='SystemButtonFace',fg="black")
        clothes_choice_quantity.config(bg='SystemButtonFace',fg="black")
        paid_label_answer.config(bg='SystemButtonFace',fg="black")
        Prix_total_label.config(bg='SystemButtonFace',fg="black")
        Prix_total_label_value.config(bg='SystemButtonFace',fg="black")
        delete_client_Label.config(bg='SystemButtonFace',fg='red')
Theme_Button=Button(width=15,height=2,text='Changer le theme',bg='black',command=change_theme,fg='white')
Theme_Button.place(x=widthx-400,y=10)
#not paid_clients button -> shows all the records about the clients who doesn't pay yet
def show_all_unpaid() :
    database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
    database_cursor=database_connect.cursor()
    database_cursor.execute("SELECT name_client,prename_client,phone_client,date_commande,hour_commande,sum(clothe_total_price),Paid_y_n from COMMANDE where Paid_y_n='NON' GROUP BY phone_client,name_client,prename_client order by phone_client ASC,date_commande ASC,hour_commande ASC")
    all_record_unpaid=database_cursor.fetchall()
    records_of_clients_unpaid=Toplevel()
    records_of_clients_unpaid.title("Records de clients non payés")
    records_of_clients_unpaid.geometry(str(widthx)+"x"+str(heighty))
    all_records_frame_unpaid=Frame()
    all_records_frame_unpaid.place(x=0,y=0)
    all_records_treeview_unpaid=ttk.Treeview(records_of_clients_unpaid,columns=(1,2,3,4,5,6,7),show='headings',height=19)
    all_records_treeview_unpaid.place(x=0,y=0)
    all_records_treeview_unpaid.heading(1,text='Nom_client')
    all_records_treeview_unpaid.column("#1",anchor=CENTER, stretch=NO, width=120)
    all_records_treeview_unpaid.heading(2,text='Prénom_client')
    all_records_treeview_unpaid.column("#2",anchor=CENTER, stretch=NO, width=120)
    all_records_treeview_unpaid.heading(3,text='Numero')
    all_records_treeview_unpaid.heading(4,text='date_commande')
    all_records_treeview_unpaid.heading(5,text='heur_commande')
    all_records_treeview_unpaid.heading(6,text='prix_total')
    all_records_treeview_unpaid.heading(7,text='Payé')
    for i in range(len(all_record_unpaid)) : 
        all_records_treeview_unpaid.insert('',"end",values=(all_record_unpaid[i][0],all_record_unpaid[i][1],all_record_unpaid[i][2],all_record_unpaid[i][3],all_record_unpaid[i][4],all_record_unpaid[i][5],all_record_unpaid[i][6]))
    database_connect.commit() 

not_paid_clients=CTkButton(command=show_all_unpaid,corner_radius=15,bg_color='grey',fg_color="purple",width=70,height=70,text="Clients non payé",text_color="white",text_font=('arial',15)
,hover=True,hover_color='purple')
not_paid_clients.place(x=450,y=heighty-270)
#deleting button -> only accessible by the owner with a code that he can only set

def delete_client() :
    def done_password(event) :
        if Enter_password.get()=='1234' :#the owner can set this password 
         delete_window_client=Toplevel()
         delete_window_client.geometry(str(widthx)+"x"+str(heighty))
         delete_window_client.title("Supprimer un client")
         database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
         database_cursor=database_connect.cursor()
         database_cursor.execute("SELECT name_client,prename_client,phone_client,date_commande,hour_commande,sum(clothe_total_price),Paid_y_n from COMMANDE GROUP BY phone_client,name_client,prename_client order by phone_client ASC,date_commande ASC,hour_commande ASC")
         all_record=database_cursor.fetchall()
         all_records_frame=Frame(delete_window_client)
         all_records_frame.place(x=0,y=0)
         all_records_treeview=ttk.Treeview(delete_window_client,columns=(1,2,3,4,5,6,7),show='headings',height=20)
         all_records_treeview.place(x=0,y=0)
         all_records_treeview.heading(1,text='Nom_client')
         all_records_treeview.column("#1",anchor=CENTER, stretch=NO, width=120)
         all_records_treeview.heading(2,text='Prénom_client')
         all_records_treeview.column("#2",anchor=CENTER, stretch=NO, width=120)
         all_records_treeview.heading(3,text='Numero')
         all_records_treeview.heading(4,text='date_commande')
         all_records_treeview.heading(5,text='heur_commande')
         all_records_treeview.heading(6,text='prix_total')
         all_records_treeview.heading(7,text='Payé')
         def Supprimer() :
          database_connect=sqlite3.connect('Dry_cleaners_app_data.db')
          database_cursor=database_connect.cursor()
          x=all_records_treeview.focus()
          to_be_deleted=all_record[int(x)][2]
          all_record.pop(int(x))
          database_cursor.execute("DELETE FROM COMMANDE WHERE phone_client=('%s')"%to_be_deleted)
          database_connect.commit()
          for i in all_records_treeview.get_children() :
            all_records_treeview.delete(i)
          for i in range(len(all_record)) :
            all_records_treeview.insert('','end',iid=i,values=(all_record[i][0],all_record[i][1],all_record[i][2],all_record[i][3],all_record[i][4],all_record[i][5],all_record[i][6])) 
         delete_client_button_toplevel=Button(delete_window_client,text="Supprimer",bg='red',width=15,height=3,font=('arial',15),command=Supprimer)
         delete_client_button_toplevel.place(x=(widthx-200)/2,y=heighty-300)
         for i in range(len(all_record)) :
          all_records_treeview.insert('',"end",iid=i,values=(all_record[i][0],all_record[i][1],all_record[i][2],all_record[i][3],all_record[i][4],all_record[i][5],all_record[i][6]))
         database_connect.commit()
         delete_window.destroy()
        else :
            messagebox.showerror("Error","le mot de passe est faux! ")
            delete_window.destroy()
    delete_window=Toplevel()
    delete_window.geometry("400x200")
    Enter_password=Entry(delete_window,width=15,font=('arial',15),show='*')
    Enter_password.pack()
    Password_label=Label(delete_window,width=20,text="Entrer le mot de passe\ncliquez sur entrer",fg="red",font=('arial',15))
    Password_label.pack()
    delete_window.bind('<Return>',done_password)    
delete_client_button=CTkButton(main_window,command=delete_client,corner_radius=15,fg_color="red",width=70,height=70,text="Supprimer un client",text_color="black",text_font=('arial',15),hover=True)
delete_client_button.place(x=850,y=500)
delete_client_Label=Label(width=30,text="Ce bouton n'est accessible \n qu'au propriétaire principal",fg='red',font=('arial',15))
delete_client_Label.place(x=830,y=600)

main_window.mainloop()