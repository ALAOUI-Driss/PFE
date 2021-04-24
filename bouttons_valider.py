import fenetre
import sql
import bouttons_fonctions
import bouttons_interragir
import mail_checker



def action_valider():
  bouttons_fonctions.do_getting()
  if(bouttons_fonctions.is_rechercher==1) : valider_rechercher()
  else :
    if(bouttons_fonctions.current_info[0]==''):
      fenetre.tkinter.messagebox.showwarning("Erreur","Le numero d'etudiant est obligatoire")
      bouttons_interragir.do_cancel()
    else:
      try:
        bouttons_fonctions.current_info[0]=int(bouttons_fonctions.current_info[0])
      except ValueError :
        fenetre.tkinter.messagebox.showwarning("Erreur","Le premier champs doit etre un numero entier strictement positif")
        bouttons_interragir.do_cancel()
      else:
        if(bouttons_fonctions.current_info[0]<=0):
          fenetre.tkinter.messagebox.showwarning("Erreur","Le numero doit etre strictement positif")
          bouttons_interragir.do_cancel()
        elif(mail_checker.mail_check(bouttons_fonctions.current_info[3])==1):
          fenetre.tkinter.messagebox.showwarning("Erreur","Le mail n'est pas valide")
          bouttons_interragir.do_cancel()
        if(bouttons_fonctions.current_info[4]!=""):
          try:
            bouttons_fonctions.current_info[4]=int(bouttons_fonctions.current_info[4])
          except ValueError :
            fenetre.tkinter.messagebox.showwarning("Erreur","La classe doit etre un entier")
            bouttons_interragir.do_cancel()
        if(bouttons_fonctions.is_modifier==1): valider_modifier()
        if(bouttons_fonctions.is_ajouter==1): valider_ajouter()

def valider_modifier():
  if(sql.check_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0]) == 1 \
  and int(bouttons_fonctions.current_info[0]) != int(bouttons_interragir.num_origin)):
    fenetre.tkinter.messagebox.showwarning("Erreur","Ce numero est deja occupe")
    bouttons_interragir.do_cancel()
  else:
    sql.action_modifier_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info,bouttons_interragir.num_origin)
    bouttons_fonctions.is_ajouter=0
    bouttons_fonctions.is_modifier=0
    bouttons_fonctions.entries_switch_DISABLED()
    bouttons_fonctions.buttons_switch_NORMAL()
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
    bouttons_interragir.do_cancel()
  else:
    sql.action_ajouter_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info)
    bouttons_fonctions.is_ajouter=0
    bouttons_fonctions.is_modifier=0
    bouttons_fonctions.entries_switch_DISABLED()
    bouttons_fonctions.buttons_switch_NORMAL()
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
    bouttons_interragir.bouttons_nav.action_deb()
  else:
    fenetre.tkinter.messagebox.showwarning("Erreur","Aucun element ne correspond a votre requete")
    bouttons_interragir.action_annuler()

fenetre.boutton_valider.config(command=action_valider)