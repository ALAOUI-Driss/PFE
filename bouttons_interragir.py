import fenetre
import bouttons_fonctions
import bouttons_nav
import sql

num_origin=0

def do_cancel():
      bouttons_fonctions.is_ajouter=0
      bouttons_fonctions.is_modifier=0
      bouttons_fonctions.do_deleting()
      bouttons_fonctions.do_inserting(sql.action_retour(num_origin))
      bouttons_fonctions.do_getting()
      bouttons_fonctions.entries_switch_DISABLED()
      bouttons_fonctions.buttons_switch_NORMAL()


def action_ajouter():
  global num_origin
  bouttons_fonctions.is_ajouter=1
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.buttons_switch_DISABLED()
  num_origin=bouttons_fonctions.fenetre.e_Numero.get()
  bouttons_fonctions.do_deleting()
def action_modifier():
  global num_origin
  bouttons_fonctions.is_modifier=1
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.buttons_switch_DISABLED()
  num_origin=bouttons_fonctions.fenetre.e_Numero.get()

def action_supprimer():
  if(bouttons_fonctions.fenetre.tkinter.messagebox.askyesno("Confirmation","Voulez-vous vraiment supprimer l'element courant ?")):
    if(sql.action_supprimer_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0])==0) :
      bouttons_fonctions.fenetre.tkinter.messagebox.showinfo("Confirmation","Element supprime")
      bouttons_nav.action_deb()
    else : fenetre.tkinter.messagebox.showwarning("Erreur","La table doit contenir au moins un element")

def action_rechercher():
  bouttons_fonctions.is_rechercher=1
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.buttons_switch_DISABLED()



def action_annuler():
  if(bouttons_fonctions.is_rechercher==0):
    bouttons_fonctions.do_deleting()
    bouttons_fonctions.do_inserting(bouttons_fonctions.current_info)
    bouttons_fonctions.entries_switch_DISABLED()
    bouttons_fonctions.buttons_switch_NORMAL()
  else:
    bouttons_fonctions.is_rechercher=0
    bouttons_fonctions.entries_switch_DISABLED()
    bouttons_fonctions.buttons_switch_NORMAL()
    bouttons_fonctions.current_table='etudiant'
    bouttons_nav.action_deb()


fenetre.boutton_modifier.config(command=action_modifier)
fenetre.boutton_annuler.config(command=action_annuler)
fenetre.boutton_ajouter.config(command=action_ajouter)
fenetre.boutton_supprimer.config(command=action_supprimer)
fenetre.boutton_rechercher.config(command=action_rechercher)