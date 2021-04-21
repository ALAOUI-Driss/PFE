import fenetre
import bouttons_fonctions
import bouttons_nav
import sql

num_true=0

def action_ajouter():
  bouttons_fonctions.is_ajouter=1
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.buttons_switch_DISABLED()
def action_modifier():
  global num_true
  bouttons_fonctions.is_modifier=1
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.buttons_switch_DISABLED()
  num_true=bouttons_fonctions.fenetre.e_Numero.get()

def action_supprimer():
  if(sql.action_supprimer_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0])==0) : bouttons_nav.action_deb()
  else : fenetre.tkinter.messagebox.showwarning("Erreur","La table doit contenir au moins un element")

def action_rechercher():
  bouttons_fonctions.is_rechercher=1
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.buttons_switch_DISABLED()


def action_valider():
  bouttons_fonctions.do_getting()
  bouttons_fonctions.entries_switch_DISABLED()
  bouttons_fonctions.buttons_switch_NORMAL()
  if(bouttons_fonctions.is_rechercher==1) : valider_rechercher()
  else :
    if(bouttons_fonctions.current_info[0]==''):
      fenetre.tkinter.messagebox.showwarning("Erreur","Le numero d'etudiant est obligatoire")
      bouttons_fonctions.is_ajouter=0
      bouttons_fonctions.is_modifier=0
      bouttons_nav.action_deb()
      return
    try:
      bouttons_fonctions.current_info[0]=int(bouttons_fonctions.current_info[0])
    except ValueError :
      fenetre.tkinter.messagebox.showwarning("Erreur","Le premier champs doit etre un numero entier strictement positif")
      bouttons_fonctions.is_ajouter=0
      bouttons_fonctions.is_modifier=0
      bouttons_nav.action_deb()
    else:
      if(bouttons_fonctions.current_info[0]<=0):
        fenetre.tkinter.messagebox.showwarning("Erreur","Le numero doit etre strictement positif")
        bouttons_fonctions.is_ajouter=0
        bouttons_fonctions.is_modifier=0
        bouttons_nav.action_deb()
      elif(bouttons_fonctions.is_modifier==1): valider_modifier()
      elif(bouttons_fonctions.is_ajouter==1): valider_ajouter()

def valider_modifier():
    global num_true
    if(sql.check_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0]) == 1 \
    and int(bouttons_fonctions.current_info[0]) != int(num_true)):
            fenetre.tkinter.messagebox.showwarning("Erreur","Ce numero est deja occupe")
            bouttons_fonctions.is_ajouter=0
            bouttons_fonctions.is_modifier=0
            bouttons_nav.action_deb()
    else:
        sql.action_modifier_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info,num_true)
        bouttons_fonctions.is_ajouter=0
        bouttons_fonctions.is_modifier=0
        if (int(bouttons_fonctions.current_info[0]) == int(sql.premier(bouttons_fonctions.current_table))) :
          fenetre.boutton_prec['state']=fenetre.tkinter.DISABLED
        if (int(bouttons_fonctions.current_info[0]) == int(sql.dernier(bouttons_fonctions.current_table))) :
          fenetre.boutton_suiv['state']=fenetre.tkinter.DISABLED
        fenetre.boutton_count['text']= \
          str(sql.action_count(bouttons_fonctions.current_table, bouttons_fonctions.current_info[0]))+ '/'+ \
          str(sql.total_sql(bouttons_fonctions.current_table))
        


def valider_ajouter():
    if(sql.check_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0])==1):
        fenetre.tkinter.messagebox.showwarning("Erreur","Ce numero est deja occupe")
        bouttons_fonctions.is_ajouter=0
        bouttons_fonctions.is_modifier=0
        bouttons_nav.action_deb()
    else:
        sql.action_ajouter_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info)
        bouttons_fonctions.is_ajouter=0
        bouttons_fonctions.is_modifier=0
        if (int(bouttons_fonctions.current_info[0]) == int(sql.premier(bouttons_fonctions.current_table))) :
          fenetre.boutton_prec['state']=fenetre.tkinter.DISABLED
        if (int(bouttons_fonctions.current_info[0]) == int(sql.dernier(bouttons_fonctions.current_table))) :
          fenetre.boutton_suiv['state']=fenetre.tkinter.DISABLED
          fenetre.boutton_count['text']= \
            str(sql.action_count(bouttons_fonctions.current_table, bouttons_fonctions.current_info[0]))+ '/'+ \
            str(sql.total_sql(bouttons_fonctions.current_table))

def valider_rechercher():
  bouttons_fonctions.buttons_switch_DISABLED()
  if bouttons_fonctions.current_info[0]=='' : bouttons_fonctions.current_info[0]='%'
  if bouttons_fonctions.current_info[1]=='' : bouttons_fonctions.current_info[1]='%'
  if bouttons_fonctions.current_info[2]=='' : bouttons_fonctions.current_info[2]='%'
  if bouttons_fonctions.current_info[3]=='' : bouttons_fonctions.current_info[3]='%'
  if bouttons_fonctions.current_info[4]=='' : bouttons_fonctions.current_info[4]='%'
  sql.action_rechercher_sql(bouttons_fonctions.current_info)
  bouttons_fonctions.current_table='my_view'
  if(sql.total_sql(bouttons_fonctions.current_table)!=0):
    bouttons_nav.action_deb()
  else:
    fenetre.tkinter.messagebox.showwarning("Erreur","Aucun element ne correspond a votre requete")
    action_annuler()

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
fenetre.boutton_valider.config(command=action_valider)
fenetre.boutton_annuler.config(command=action_annuler)
fenetre.boutton_ajouter.config(command=action_ajouter)
fenetre.boutton_supprimer.config(command=action_supprimer)
fenetre.boutton_rechercher.config(command=action_rechercher)