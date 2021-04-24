import fenetre
import sql

current_table='etudiant'
current_info=['numero','nom','adresse','mail','classe']
is_rechercher=0
is_ajouter=0
is_modifier=0


def do_deleting():
  fenetre.e_Numero.delete(0,fenetre.tkinter.END)
  fenetre.e_Nom.delete(0,fenetre.tkinter.END)
  fenetre.e_Adresse.delete(0,fenetre.tkinter.END)
  fenetre.e_Mail.delete(0,fenetre.tkinter.END)
  fenetre.e_Classe.delete(0,fenetre.tkinter.END)
def do_inserting(info):
  fenetre.e_Numero.insert(0,info[0])
  fenetre.e_Nom.insert(0,info[1])
  fenetre.e_Adresse.insert(0,info[2])
  fenetre.e_Mail.insert(0,info[3])
  fenetre.e_Classe.insert(0,info[4])
def do_getting():
  global current_info
  current_info[0]=fenetre.e_Numero.get()
  current_info[1]=fenetre.e_Nom.get()
  current_info[2]=fenetre.e_Adresse.get()
  current_info[3]=fenetre.e_Mail.get()
  current_info[4]=fenetre.e_Classe.get()


# def widget_switch_states(widget):
#   if (widget['state'] == NORMAL) : widget['state'] = DISABLED
#   else : widget['state'] = NORMAL


def entries_switch_NORMAL():
  fenetre.e_Numero['state']= fenetre.tkinter.NORMAL
  fenetre.e_Nom['state']= fenetre.tkinter.NORMAL
  fenetre.e_Adresse['state']= fenetre.tkinter.NORMAL
  fenetre.e_Mail['state']= fenetre.tkinter.NORMAL
  fenetre.e_Classe['state']= fenetre.tkinter.NORMAL
def entries_switch_DISABLED():
  fenetre.e_Numero['state']= fenetre.tkinter.DISABLED
  fenetre.e_Nom['state']= fenetre.tkinter.DISABLED
  fenetre.e_Adresse['state']= fenetre.tkinter.DISABLED
  fenetre.e_Mail['state']= fenetre.tkinter.DISABLED
  fenetre.e_Classe['state']= fenetre.tkinter.DISABLED
def buttons_switch_NORMAL():
  fenetre.boutton_modifier['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_ajouter['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_rechercher['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_supprimer['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_valider['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_annuler['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_deb['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_fin['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_suiv['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_prec['state']= fenetre.tkinter.NORMAL
def buttons_switch_DISABLED():
  fenetre.boutton_modifier['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_ajouter['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_rechercher['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_supprimer['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_valider['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_annuler['state']= fenetre.tkinter.NORMAL
  fenetre.boutton_deb['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_fin['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_suiv['state']= fenetre.tkinter.DISABLED
  fenetre.boutton_prec['state']= fenetre.tkinter.DISABLED
