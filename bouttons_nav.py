import fenetre
import sql
import bouttons_fonctions

def action_deb():
  array=sql.action_deb_sql(bouttons_fonctions.current_table)
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.do_deleting()
  bouttons_fonctions.do_inserting(array)
  bouttons_fonctions.do_getting()
  fenetre.boutton_prec['state']=fenetre.tkinter.DISABLED
  if (int(bouttons_fonctions.current_info[0]) == int(sql.dernier(bouttons_fonctions.current_table))) :
    fenetre.boutton_suiv['state']=fenetre.tkinter.DISABLED
  else :
    fenetre.boutton_suiv['state']=fenetre.tkinter.NORMAL
  fenetre.boutton_count['text']='1/'+str(sql.total_sql(bouttons_fonctions.current_table))
  if(bouttons_fonctions.is_rechercher==0) :
    bouttons_fonctions.entries_switch_DISABLED()
  else :
    fenetre.boutton_deb['state']=fenetre.tkinter.NORMAL
    fenetre.boutton_fin['state']=fenetre.tkinter.NORMAL

def action_fin():
  array=sql.action_fin_sql(bouttons_fonctions.current_table)
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.do_deleting()
  bouttons_fonctions.do_inserting(array)
  bouttons_fonctions.do_getting()
  fenetre.boutton_suiv['state']=fenetre.tkinter.DISABLED
  if (int(bouttons_fonctions.current_info[0]) == int(sql.premier(bouttons_fonctions.current_table))) :
    fenetre.boutton_prec['state']=fenetre.tkinter.DISABLED
  else : fenetre.boutton_prec['state']=fenetre.tkinter.NORMAL
  fenetre.boutton_count['text']= \
    str(sql.action_count(bouttons_fonctions.current_table, bouttons_fonctions.current_info[0]))+ '/'+ \
    str(sql.total_sql(bouttons_fonctions.current_table))
  if(bouttons_fonctions.is_rechercher==0) : bouttons_fonctions.entries_switch_DISABLED()

def action_suiv():
  array=sql.action_suiv_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0])
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.do_deleting()
  bouttons_fonctions.do_inserting(array)
  bouttons_fonctions.do_getting()
  fenetre.boutton_prec['state']=fenetre.tkinter.NORMAL
  if (int(bouttons_fonctions.current_info[0]) == int(sql.dernier(bouttons_fonctions.current_table))) :
    fenetre.boutton_suiv['state']=fenetre.tkinter.DISABLED
  fenetre.boutton_count['text']= \
    str(sql.action_count(bouttons_fonctions.current_table, bouttons_fonctions.current_info[0]))+ '/'+ \
    str(sql.total_sql(bouttons_fonctions.current_table))
  if(bouttons_fonctions.is_rechercher==0) : bouttons_fonctions.entries_switch_DISABLED()

def action_prec():
  array=sql.action_prec_sql(bouttons_fonctions.current_table,bouttons_fonctions.current_info[0])
  bouttons_fonctions.entries_switch_NORMAL()
  bouttons_fonctions.do_deleting()
  bouttons_fonctions.do_inserting(array)
  bouttons_fonctions.do_getting()
  fenetre.boutton_suiv['state']=fenetre.tkinter.NORMAL
  if (int(bouttons_fonctions.current_info[0]) == int(sql.premier(bouttons_fonctions.current_table))) :
    fenetre.boutton_prec['state']=fenetre.tkinter.DISABLED
  fenetre.boutton_count['text']= \
    str(sql.action_count(bouttons_fonctions.current_table, bouttons_fonctions.current_info[0]))+ '/'+ \
    str(sql.total_sql(bouttons_fonctions.current_table))
  if(bouttons_fonctions.is_rechercher==0) : bouttons_fonctions.entries_switch_DISABLED()

  
fenetre.boutton_deb.config(command=action_deb)
fenetre.boutton_fin.config(command=action_fin)
fenetre.boutton_suiv.config(command=action_suiv)
fenetre.boutton_prec.config(command=action_prec)