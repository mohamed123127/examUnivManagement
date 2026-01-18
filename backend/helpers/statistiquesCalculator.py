from collections import Counter

db = None

def generaleStats():
    print('Generale statistiques')
    print('Total student groups:',len(db['groups']))
    print('Total professors:',len(db['professors']))
    print('Total amphis:',len([item for item in db['classrooms'] if item['type'] == "amphi"]))
    print('Total classes:',len([item for item in db['classrooms'] if item['type'] == "class"]))
    print("\n")
    return

def examStats():
    print('exams statistiques')
    examsNumber = len(db['modules'])
    modulesNumber = len(db['modules'])
    #calc commune modules
    modulesCounts = Counter(fym["module_id"] for fym in db['formation_year_modules'])
    communeModules = {module for module,count in modulesCounts.items() if count > 1}

    print("Total exams:", examsNumber)
    print("Total modules:", modulesNumber)
    print("Total commune modules:",len(communeModules))
    print("commune modules:",communeModules)
    print("\n")
    return 

def getStatistiques(DB):
    global db
    db = DB
    generaleStats()
    examStats()
    return

