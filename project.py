import json
import beaupy
 
#==================================================================== Login ===================================================================================================================
 
def login():
   email = input("\nEmail: ")
   passWord=input("\nPass-Word: ")
 
   with open('teachers.json', 'r') as f:
      data = json.load(f)
   
   for d in data:
      if d["email"] == email and d["password"] == passWord:
         callMenu(email)
         break
   else:
      print("Email or password is wrong")
 
       
#==================================================================== Verificacao do email ===================================================================================================================
 
def callMenu(email):
   if "@" in email and "." in email:
        domain = email.split('@')[1].split('.')[0]
 
   match domain:
    case "admin":
        adminMenu()#---> Menu dos Admin
    case "student":
        print("")#---> Menu dos Alunos
    case "staff":
        print("")#---> Menu dos Docentes
    case _:
        print("Erro")
   
#==================================================================== Admin Stuff ===================================================================================================================
#Menu Principal do  Admin
 
def adminMenu():
 while True:
    print("\n------ Admin Menu ------")
    menuAdmin = ["1. Gerir Alunos","2. Gerir Docentes","3. Gerir Uc's", "4. Gerir Matriculas","5. Sair"]
   
    navigate = beaupy.select(menuAdmin)
 
    if navigate == "1. Gerir Alunos":
       GerirAlunos_Menu() #---> Tudo haver com Alunos
    elif navigate== "2. Gerir Docentes":
       GerirDocentes_Menu() #---> Tudo haver com Docentes
    elif navigate== "3. Gerir Uc's":
      GerirUCs_Menus() #---> Tudo haver com UC's
    elif navigate== "4. Gerir Matriculas":
        GerirMatriculas_Menus() #---> Ainda n sei bem
    elif navigate== "5. Sair":
       print("GoodBye.")
       break
 
#==================================================================== Admin Aluno Stuff ===================================================================================================================
 
# Gerir Alunos
 
def GerirAlunos_Menu():
 while True:
    print ("\n------ Gerir Alunos ------")
    GerirAlunos = ["1. Consultar Alunos", "2. Inserir Alunos", "3. Voltar"]
    
    navigate = beaupy.select(GerirAlunos)
 
    if navigate =="1. Consultar Alunos":
        ConultarAlunos_Menu() #---> Consultar deve monstrar tds os alunos, respetivas UC's
    elif navigate ==  "2. Inserir Alunos":
        print("Inserir") #---> Deve criar um Aluno novo criando um email para ele
    elif navigate == "3. Voltar":
       return
 
def printStudent():
   with open('students.json', 'r') as f:
      data = json.load(f)
      for d in data:
         print(d["id"])
         print(d["names"])
 
  
   
 
def ConultarAlunos_Menu():
 
 while True:
    print("\n------ Consultar Alunos ------")
    ConslutarAlunos =  ["1. Editar Aluno", "2. Ativar Aluno","3. Desativar Aluno", "4. Voltar"]
    
    navigate = beaupy.select(ConslutarAlunos)
    
    if navigate == "1. Editar Aluno":
       printStudent()
    elif navigate == "2. Ativar Aluno":
       print("Ativado")
    elif navigate == "3. Desativar Aluno":
       print("Desativado")
    elif navigate == "4. Voltar":
       return
 
#==================================================================== Admin Docente Stuff ===================================================================================================================
 
# Gerir Docntes
 
def GerirDocentes_Menu():
 while True:
    print(("\n------ Gerir Docentes ------"))
    GerirDocentes = ["1. Consultar Docente", "2. Inserir Docente", "3. Voltar"]
 
    navigate = beaupy.select(GerirDocentes)
    
    if navigate =="1. Consultar Docentes":
        print("Consultar") #---> Consultar deve monstrar tds os Docentes, respetivas UC's
    elif navigate ==  "2. Inserir Docenetes":
        print("Inserir") #---> Deve criar um Docente novo criando um email para ele
    elif navigate == "3. Voltar":
        return
 
 
 
 
 
 
#==================================================================== Admin UC's Stuff ===================================================================================================================
 
# Gerir UC's
 
def GerirUCs_Menus():
 while True:
    print(("\n------ Gerir UC's------"))
    GerirUCs = ["1. Consultar UC", "2. Inserir UC", "3. Voltar"]
 
    navigate = beaupy.select(GerirUCs)
 
    if navigate == "1. Consultar UC":
       print("UC")
    elif navigate == "2. Inserir UC":
       print("Inserir UC")
    elif navigate == "3. Voltar":
        return
 
 
 
#==================================================================== Admin Matriculas Stuff ===================================================================================================================
 
# Gerir Matriculas
 
def GerirMatriculas_Menus():
 while True:
    print(("\n------ Gerir Matriculas------"))
    
    GerirMatricula = ["1. Consultar Matriculas","2. Inserir Matricula", "3. Voltar"]
 
    navigate = beaupy.select(GerirMatricula)
 
    if navigate == "1. Consultar Matriculas":
       print("Consultar Matricula")
    elif navigate == "2. Inserir Matricula":
       print("Inserir MAtricula")
    elif navigate == "3. Voltar":
        return
 
 
printStudent()
