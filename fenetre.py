import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("Notre projet")
window.geometry("720x480")
window.config(background='#FA8072')


frame_nav=tkinter.Frame(window, bg='#FA8072')
boutton_deb=tkinter.Button(frame_nav,text="<<", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_deb.grid(row=0,column=0, padx=5, pady=5)
boutton_prec=tkinter.Button(frame_nav,text="<", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_prec.grid(row=0,column=1, padx=5, pady=5)
boutton_suiv=tkinter.Button(frame_nav,text=">", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_suiv.grid(row=0,column=3, padx=5, pady=5)
boutton_fin=tkinter.Button(frame_nav,text=">>", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_fin.grid(row=0,column=4, padx=5, pady=5)
boutton_count=tkinter.Button(frame_nav,text="count", font=("Courrier",15), bg='#41B77F',fg='white', state='disabled')
boutton_count.grid(row=0,column=2, padx=5, pady=5)

frame_options=tkinter.Frame(window, bg='#FA8072')
boutton_ajouter=tkinter.Button(frame_options,text="Ajouter", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_ajouter.grid(row=0,column=0, padx=5, pady=5)
boutton_annuler=tkinter.Button(frame_options,text="Annuler", font=("Courrier",15), bg='#41B77F',fg='white', state=tkinter.DISABLED)
boutton_annuler.grid(row=0,column=1, padx=5, pady=5)
boutton_valider=tkinter.Button(frame_options,text="Valider", font=("Courrier",15), bg='#41B77F',fg='white', state=tkinter.DISABLED)
boutton_valider.grid(row=0,column=2, padx=5, pady=5)
boutton_supprimer=tkinter.Button(frame_options,text="Supprimer", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_supprimer.grid(row=1,column=0, padx=5, pady=5)
boutton_modifier=tkinter.Button(frame_options,text="Modifier", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_modifier.grid(row=2,column=0, padx=5, pady=5)
boutton_rechercher=tkinter.Button(frame_options,text="Rechercher", font=("Courrier",15), bg='#41B77F',fg='white')
boutton_rechercher.grid(row=3,column=0, padx=5, pady=5)


frame_main=tkinter.Frame(window,bg='#FA8072')

l_Numero=tkinter.Label(frame_main, text="Numero", font=("Courrier",15), bg='#FA8072',fg='blue')
l_Numero.grid(row=0, column=0)
l_Nom=tkinter.Label(frame_main, text="Nom", font=("Courrier",15), bg='#FA8072',fg='blue')
l_Nom.grid(row=1, column=0)
l_Adresse=tkinter.Label(frame_main, text="Adresse", font=("Courrier",15), bg='#FA8072',fg='blue')
l_Adresse.grid(row=2, column=0)
l_Mail=tkinter.Label(frame_main, text="Mail", font=("Courrier",15), bg='#FA8072',fg='blue')
l_Mail.grid(row=3, column=0)
l_Classe=tkinter.Label(frame_main, text="Classe", font=("Courrier",15), bg='#FA8072',fg='blue')
l_Classe.grid(row=4, column=0)


e_Numero=tkinter.Entry(frame_main, font=("Courrier",15), bg='white',fg='black')
e_Numero.grid(row=0, column=1)
e_Nom=tkinter.Entry(frame_main, font=("Courrier",15), bg='white',fg='black')
e_Nom.grid(row=1, column=1)
e_Adresse=tkinter.Entry(frame_main, font=("Courrier",15), bg='white',fg='black')
e_Adresse.grid(row=2, column=1)
e_Mail=tkinter.Entry(frame_main, font=("Courrier",15), bg='white',fg='black')
e_Mail.grid(row=3, column=1)
e_Classe=tkinter.Entry(frame_main, font=("Courrier",15), bg='white',fg='black')
e_Classe.grid(row=4, column=1)


frame_main.pack()
frame_options.pack(side=tkinter.BOTTOM)
frame_nav.pack(side=tkinter.BOTTOM)