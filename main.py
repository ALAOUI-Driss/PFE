import bouttons_fonctions
import bouttons_interragir
import bouttons_nav

bouttons_nav.action_deb()
bouttons_fonctions.fenetre.window.mainloop()
bouttons_fonctions.sql.mycursor.close()
bouttons_fonctions.sql.mydb.close()