import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="projet",
  autocommit=True
)
mycursor = mydb.cursor(buffered=True)


def premier(table):
  return(action_deb_sql(table)[0])
def dernier(table):
  return(action_fin_sql(table)[0])
def total_sql(table):
  mycursor.execute('SELECT COUNT(*) FROM ' + table)
  return(int(mycursor.fetchone()[0]))

def action_deb_sql(table):
  mycursor.execute('SELECT * FROM ' + table + ' ORDER BY numero LIMIT 1')
  return(mycursor.fetchone())

def action_fin_sql(table):
  mycursor.execute('SELECT * FROM ' + table + ' ORDER BY numero DESC LIMIT 1')
  return(mycursor.fetchone())

def action_suiv_sql(table,numero):
  req= 'SELECT * FROM ' + table + ' WHERE numero >= %s ORDER BY numero LIMIT 2'
  val=(int(numero),)
  mycursor.execute(req,val)
  return(mycursor.fetchall()[1])

def action_prec_sql(table,numero):
  req= 'SELECT * FROM ' + table + ' WHERE numero <= %s ORDER BY numero DESC LIMIT 2'
  val=(int(numero),)
  mycursor.execute(req,val)
  return(mycursor.fetchall()[1])

def action_count(table,numero):
  req= 'SELECT COUNT(numero) FROM ' + table + ' WHERE numero <= %s ORDER BY numero'
  val=(int(numero),)
  mycursor.execute(req,val)
  return(mycursor.fetchone()[0])

def check_sql(table,numero):
  req="SELECT COUNT(*) FROM " + table + " WHERE numero = %s"
  mycursor.execute(req,(numero,))
  if(mycursor.fetchone()[0]==0) : return(0)
  else : return(1)


def action_ajouter_sql(table,info):
    req = "INSERT INTO etudiant VALUES(%s,%s,%s,%s,%s)"
    val=(info[0],info[1],info[2],info[3],info[4])
    mycursor.execute(req,val)

def action_supprimer_sql(table, numero):
  if(total_sql(table)>1):
    req = "DELETE FROM " + table + " WHERE numero = %s"
    val=(numero,)
    mycursor.execute(req,val)
    return(0)
  else: return(1)

def action_modifier_sql(table, info,other):
  req="UPDATE " + table + " SET numero=%s, nom=%s, adresse=%s, mail=%s, classe=%s WHERE numero=%s"
  val=(info[0],info[1],info[2],info[3],info[4], other)
  mycursor.execute(req,val)

def action_rechercher_sql(info):
  req=("CREATE OR REPLACE VIEW my_view AS \
  SELECT * FROM etudiant WHERE \
	numero LIKE %s AND \
  nom LIKE %s AND \
  adresse LIKE %s AND \
  mail LIKE %s AND \
  classe LIKE %s")
  val=(info[0],info[1],info[2],info[3],info[4])
  mycursor.execute(req,val)


# mycursor.execute("SELECT * FROM etudiant")
# for x in mycursor.fetchall() : print(x)