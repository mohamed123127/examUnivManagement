# Auto-generated mock DB from MySQL

from datetime import date, time

fake_db = {
    "roles": [
        {
            "id": 1,
            "name": "Doyen"
        },
        {
            "id": 2,
            "name": "Vice-doyen"
        },
        {
            "id": 3,
            "name": "Administrateur examens"
        },
        {
            "id": 4,
            "name": "Chef de d\u00e9partement"
        },
        {
            "id": 5,
            "name": "\u00c9tudiant"
        },
        {
            "id": 6,
            "name": "Professeur"
        }
    ],
    "departments": [
        {
            "id": 1,
            "name": "Informatique"
        },
        {
            "id": 2,
            "name": "Math\u00e9matiques"
        },
        {
            "id": 3,
            "name": "Physique"
        },
        {
            "id": 4,
            "name": "Chimie"
        },
        {
            "id": 5,
            "name": "Biologie"
        },
        {
            "id": 6,
            "name": "\u00c9conomie"
        },
        {
            "id": 7,
            "name": "\u00c9lectronique"
        }
    ],
    "formations": [
        {
            "id": 1,
            "name": "LMD Informatique",
            "department_id": 1
        },
        {
            "id": 2,
            "name": "Licence Professionnelle Informatique",
            "department_id": 1
        },
        {
            "id": 3,
            "name": "Ing\u00e9nieur Informatique",
            "department_id": 1
        },
        {
            "id": 4,
            "name": "LMD Math\u00e9matiques",
            "department_id": 2
        },
        {
            "id": 5,
            "name": "LMD Physique",
            "department_id": 3
        },
        {
            "id": 6,
            "name": "LMD Chimie",
            "department_id": 4
        },
        {
            "id": 7,
            "name": "LMD Biologie",
            "department_id": 5
        },
        {
            "id": 8,
            "name": "LMD \u00c9conomie",
            "department_id": 6
        },
        {
            "id": 9,
            "name": "LMD \u00c9lectronique",
            "department_id": 7
        }
    ],
    "formation_years": [
        {
            "id": 1,
            "formation_id": 1,
            "year": "Licence 1"
        },
        {
            "id": 2,
            "formation_id": 1,
            "year": "Licence 2"
        },
        {
            "id": 3,
            "formation_id": 1,
            "year": "Licence 3"
        },
        {
            "id": 4,
            "formation_id": 1,
            "year": "Master 1"
        },
        {
            "id": 5,
            "formation_id": 1,
            "year": "Master 2"
        },
        {
            "id": 6,
            "formation_id": 2,
            "year": "Licence 1"
        },
        {
            "id": 7,
            "formation_id": 2,
            "year": "Licence 2"
        },
        {
            "id": 8,
            "formation_id": 2,
            "year": "Licence 3"
        },
        {
            "id": 9,
            "formation_id": 3,
            "year": "Ing\u00e9nieur 1"
        },
        {
            "id": 10,
            "formation_id": 3,
            "year": "Ing\u00e9nieur 2"
        },
        {
            "id": 11,
            "formation_id": 3,
            "year": "Ing\u00e9nieur 3"
        },
        {
            "id": 12,
            "formation_id": 3,
            "year": "Ing\u00e9nieur 4"
        },
        {
            "id": 13,
            "formation_id": 3,
            "year": "Ing\u00e9nieur 5"
        },
        {
            "id": 14,
            "formation_id": 4,
            "year": "Licence 1"
        },
        {
            "id": 15,
            "formation_id": 4,
            "year": "Licence 2"
        },
        {
            "id": 16,
            "formation_id": 4,
            "year": "Licence 3"
        },
        {
            "id": 17,
            "formation_id": 4,
            "year": "Master 1"
        },
        {
            "id": 18,
            "formation_id": 4,
            "year": "Master 2"
        },
        {
            "id": 19,
            "formation_id": 5,
            "year": "Licence 1"
        },
        {
            "id": 20,
            "formation_id": 5,
            "year": "Licence 2"
        },
        {
            "id": 21,
            "formation_id": 5,
            "year": "Licence 3"
        },
        {
            "id": 22,
            "formation_id": 5,
            "year": "Master 1"
        },
        {
            "id": 23,
            "formation_id": 5,
            "year": "Master 2"
        },
        {
            "id": 24,
            "formation_id": 6,
            "year": "Licence 1"
        },
        {
            "id": 25,
            "formation_id": 6,
            "year": "Licence 2"
        },
        {
            "id": 26,
            "formation_id": 6,
            "year": "Licence 3"
        },
        {
            "id": 27,
            "formation_id": 6,
            "year": "Master 1"
        },
        {
            "id": 28,
            "formation_id": 6,
            "year": "Master 2"
        },
        {
            "id": 29,
            "formation_id": 7,
            "year": "Licence 1"
        },
        {
            "id": 30,
            "formation_id": 7,
            "year": "Licence 2"
        },
        {
            "id": 31,
            "formation_id": 7,
            "year": "Licence 3"
        },
        {
            "id": 32,
            "formation_id": 7,
            "year": "Master 1"
        },
        {
            "id": 33,
            "formation_id": 7,
            "year": "Master 2"
        },
        {
            "id": 34,
            "formation_id": 8,
            "year": "Licence 1"
        },
        {
            "id": 35,
            "formation_id": 8,
            "year": "Licence 2"
        },
        {
            "id": 36,
            "formation_id": 8,
            "year": "Licence 3"
        },
        {
            "id": 37,
            "formation_id": 8,
            "year": "Master 1"
        },
        {
            "id": 38,
            "formation_id": 8,
            "year": "Master 2"
        },
        {
            "id": 39,
            "formation_id": 9,
            "year": "Licence 1"
        },
        {
            "id": 40,
            "formation_id": 9,
            "year": "Licence 2"
        },
        {
            "id": 41,
            "formation_id": 9,
            "year": "Licence 3"
        },
        {
            "id": 42,
            "formation_id": 9,
            "year": "Master 1"
        },
        {
            "id": 43,
            "formation_id": 9,
            "year": "Master 2"
        }
    ],
    "modules": [
        {
            "id": 1,
            "name": "Programmation 1"
        },
        {
            "id": 2,
            "name": "Algorithmique"
        },
        {
            "id": 3,
            "name": "Math\u00e9matiques pour l\u2019info"
        },
        {
            "id": 4,
            "name": "Introduction aux bases de donn\u00e9es"
        },
        {
            "id": 5,
            "name": "Syst\u00e8mes d\u2019exploitation"
        },
        {
            "id": 6,
            "name": "Programmation 2"
        },
        {
            "id": 7,
            "name": "Structures de donn\u00e9es"
        },
        {
            "id": 8,
            "name": "Architecture des ordinateurs"
        },
        {
            "id": 9,
            "name": "Bases de donn\u00e9es avanc\u00e9es"
        },
        {
            "id": 10,
            "name": "R\u00e9seaux informatiques"
        },
        {
            "id": 11,
            "name": "Programmation Web"
        },
        {
            "id": 12,
            "name": "Intelligence Artificielle"
        },
        {
            "id": 13,
            "name": "Algorithmique avanc\u00e9e"
        },
        {
            "id": 14,
            "name": "S\u00e9curit\u00e9 informatique"
        },
        {
            "id": 15,
            "name": "Syst\u00e8mes distribu\u00e9s"
        },
        {
            "id": 16,
            "name": "Machine Learning"
        },
        {
            "id": 17,
            "name": "Big Data"
        },
        {
            "id": 18,
            "name": "Cloud Computing"
        },
        {
            "id": 19,
            "name": "Gestion de projet logiciel"
        },
        {
            "id": 20,
            "name": "Architecture avanc\u00e9e"
        },
        {
            "id": 21,
            "name": "Deep Learning"
        },
        {
            "id": 22,
            "name": "Data Mining"
        },
        {
            "id": 23,
            "name": "IoT"
        },
        {
            "id": 24,
            "name": "DevOps"
        },
        {
            "id": 25,
            "name": "Blockchain"
        },
        {
            "id": 26,
            "name": "Gestion de projets IT"
        },
        {
            "id": 27,
            "name": "D\u00e9veloppement web avanc\u00e9"
        },
        {
            "id": 28,
            "name": "Bases de donn\u00e9es professionnelles"
        },
        {
            "id": 29,
            "name": "S\u00e9curit\u00e9 et r\u00e9seaux"
        },
        {
            "id": 30,
            "name": "DevOps"
        },
        {
            "id": 31,
            "name": "Big Data"
        },
        {
            "id": 32,
            "name": "Machine Learning appliqu\u00e9"
        },
        {
            "id": 33,
            "name": "Programmation mobile"
        },
        {
            "id": 34,
            "name": "R\u00e9seaux avanc\u00e9s"
        },
        {
            "id": 35,
            "name": "Cloud & virtualisation"
        },
        {
            "id": 36,
            "name": "IA avanc\u00e9e"
        },
        {
            "id": 37,
            "name": "Blockchain"
        },
        {
            "id": 38,
            "name": "DevOps avanc\u00e9"
        },
        {
            "id": 39,
            "name": "IoT"
        },
        {
            "id": 40,
            "name": "Projet professionnel"
        },
        {
            "id": 41,
            "name": "Programmation orient\u00e9e objet"
        },
        {
            "id": 42,
            "name": "Bases de donn\u00e9es"
        },
        {
            "id": 43,
            "name": "R\u00e9seaux"
        },
        {
            "id": 44,
            "name": "Syst\u00e8mes temps r\u00e9el"
        },
        {
            "id": 45,
            "name": "Cloud"
        },
        {
            "id": 46,
            "name": "IA appliqu\u00e9e"
        },
        {
            "id": 47,
            "name": "Big Data Analytics"
        },
        {
            "id": 48,
            "name": "Cybers\u00e9curit\u00e9"
        },
        {
            "id": 49,
            "name": "Mobile"
        },
        {
            "id": 50,
            "name": "Syst\u00e8mes distribu\u00e9s"
        },
        {
            "id": 51,
            "name": "IoT & embarqu\u00e9"
        },
        {
            "id": 52,
            "name": "DevOps & CI/CD"
        },
        {
            "id": 53,
            "name": "Blockchain avanc\u00e9e"
        },
        {
            "id": 54,
            "name": "Microservices"
        },
        {
            "id": 55,
            "name": "Cloud avanc\u00e9"
        },
        {
            "id": 56,
            "name": "Analyse de donn\u00e9es"
        },
        {
            "id": 57,
            "name": "Deep Learning avanc\u00e9"
        },
        {
            "id": 58,
            "name": "R\u00e9seaux avanc\u00e9s"
        },
        {
            "id": 59,
            "name": "S\u00e9curit\u00e9 offensive"
        },
        {
            "id": 60,
            "name": "Parall\u00e9lisme"
        },
        {
            "id": 61,
            "name": "Projet industriel"
        },
        {
            "id": 62,
            "name": "Optimisation"
        },
        {
            "id": 63,
            "name": "IA avanc\u00e9e"
        },
        {
            "id": 64,
            "name": "Cloud hybride"
        },
        {
            "id": 65,
            "name": "Syst\u00e8mes distribu\u00e9s avanc\u00e9s"
        },
        {
            "id": 66,
            "name": "Analyse 1"
        },
        {
            "id": 67,
            "name": "Alg\u00e8bre 1"
        },
        {
            "id": 68,
            "name": "G\u00e9om\u00e9trie"
        },
        {
            "id": 69,
            "name": "Probabilit\u00e9s"
        },
        {
            "id": 70,
            "name": "Analyse 2"
        },
        {
            "id": 71,
            "name": "Alg\u00e8bre 2"
        },
        {
            "id": 72,
            "name": "Topologie"
        },
        {
            "id": 73,
            "name": "Statistiques"
        },
        {
            "id": 74,
            "name": "Analyse complexe"
        },
        {
            "id": 75,
            "name": "\u00c9quations diff\u00e9rentielles"
        },
        {
            "id": 76,
            "name": "Math\u00e9matiques appliqu\u00e9es"
        },
        {
            "id": 77,
            "name": "Probabilit\u00e9s avanc\u00e9es"
        },
        {
            "id": 78,
            "name": "Statistiques avanc\u00e9es"
        },
        {
            "id": 79,
            "name": "Optimisation"
        },
        {
            "id": 80,
            "name": "Alg\u00e8bre avanc\u00e9e"
        },
        {
            "id": 81,
            "name": "Analyse num\u00e9rique"
        },
        {
            "id": 82,
            "name": "Math\u00e9matiques computationnelles"
        },
        {
            "id": 83,
            "name": "Th\u00e9orie des graphes"
        },
        {
            "id": 84,
            "name": "Analyse num\u00e9rique avanc\u00e9e"
        },
        {
            "id": 85,
            "name": "Applications statistiques"
        },
        {
            "id": 86,
            "name": "M\u00e9canique 1"
        },
        {
            "id": 87,
            "name": "\u00c9lectricit\u00e9 1"
        },
        {
            "id": 88,
            "name": "Thermodynamique"
        },
        {
            "id": 89,
            "name": "Physique exp\u00e9rimentale"
        },
        {
            "id": 90,
            "name": "M\u00e9canique 2"
        },
        {
            "id": 91,
            "name": "\u00c9lectricit\u00e9 2"
        },
        {
            "id": 92,
            "name": "Optique"
        },
        {
            "id": 93,
            "name": "Physique appliqu\u00e9e"
        },
        {
            "id": 94,
            "name": "Physique quantique"
        },
        {
            "id": 95,
            "name": "Physique nucl\u00e9aire"
        },
        {
            "id": 96,
            "name": "Optique avanc\u00e9e"
        },
        {
            "id": 97,
            "name": "\u00c9lectricit\u00e9 avanc\u00e9e"
        },
        {
            "id": 98,
            "name": "Physique th\u00e9orique"
        },
        {
            "id": 99,
            "name": "Physique des mat\u00e9riaux"
        },
        {
            "id": 100,
            "name": "Astrophysique"
        },
        {
            "id": 101,
            "name": "Physique exp\u00e9rimentale avanc\u00e9e"
        },
        {
            "id": 102,
            "name": "Physique computationnelle"
        },
        {
            "id": 103,
            "name": "M\u00e9canique des fluides"
        },
        {
            "id": 104,
            "name": "\u00c9nergie"
        },
        {
            "id": 105,
            "name": "Plasmas"
        },
        {
            "id": 106,
            "name": "Chimie g\u00e9n\u00e9rale"
        },
        {
            "id": 107,
            "name": "Chimie organique 1"
        },
        {
            "id": 108,
            "name": "Chimie inorganique 1"
        },
        {
            "id": 109,
            "name": "Physico-chimie"
        },
        {
            "id": 110,
            "name": "Chimie organique 2"
        },
        {
            "id": 111,
            "name": "Chimie inorganique 2"
        },
        {
            "id": 112,
            "name": "Chimie analytique"
        },
        {
            "id": 113,
            "name": "Biochimie"
        },
        {
            "id": 114,
            "name": "Chimie physique avanc\u00e9e"
        },
        {
            "id": 115,
            "name": "Chimie industrielle"
        },
        {
            "id": 116,
            "name": "Chimie organique avanc\u00e9e"
        },
        {
            "id": 117,
            "name": "Chimie analytique avanc\u00e9e"
        },
        {
            "id": 118,
            "name": "Chimie des mat\u00e9riaux"
        },
        {
            "id": 119,
            "name": "Chimie th\u00e9orique"
        },
        {
            "id": 120,
            "name": "Chimie sp\u00e9cialis\u00e9e"
        },
        {
            "id": 121,
            "name": "Chimie analytique sp\u00e9cialis\u00e9e"
        },
        {
            "id": 122,
            "name": "Chimie computationnelle"
        },
        {
            "id": 123,
            "name": "Chimie pharmaceutique"
        },
        {
            "id": 124,
            "name": "Chimie environnementale"
        },
        {
            "id": 125,
            "name": "Chimie appliqu\u00e9e"
        },
        {
            "id": 126,
            "name": "Biologie cellulaire"
        },
        {
            "id": 127,
            "name": "Biologie mol\u00e9culaire"
        },
        {
            "id": 128,
            "name": "Anatomie"
        },
        {
            "id": 129,
            "name": "Physiologie"
        },
        {
            "id": 130,
            "name": "G\u00e9n\u00e9tique"
        },
        {
            "id": 131,
            "name": "Microbiologie"
        },
        {
            "id": 132,
            "name": "Biochimie"
        },
        {
            "id": 133,
            "name": "\u00c9cologie"
        },
        {
            "id": 134,
            "name": "Biologie animale"
        },
        {
            "id": 135,
            "name": "Biologie v\u00e9g\u00e9tale"
        },
        {
            "id": 136,
            "name": "Immunologie"
        },
        {
            "id": 137,
            "name": "Physiologie avanc\u00e9e"
        },
        {
            "id": 138,
            "name": "Biotechnologie"
        },
        {
            "id": 139,
            "name": "Biologie cellulaire avanc\u00e9e"
        },
        {
            "id": 140,
            "name": "Microbiologie appliqu\u00e9e"
        },
        {
            "id": 141,
            "name": "G\u00e9n\u00e9tique avanc\u00e9e"
        },
        {
            "id": 142,
            "name": "Bioinformatique"
        },
        {
            "id": 143,
            "name": "Biologie mol\u00e9culaire avanc\u00e9e"
        },
        {
            "id": 144,
            "name": "\u00c9cologie appliqu\u00e9e"
        },
        {
            "id": 145,
            "name": "Biologie exp\u00e9rimentale"
        },
        {
            "id": 146,
            "name": "Micro\u00e9conomie 1"
        },
        {
            "id": 147,
            "name": "Macro\u00e9conomie 1"
        },
        {
            "id": 148,
            "name": "Statistiques \u00e9conomiques"
        },
        {
            "id": 149,
            "name": "Gestion"
        },
        {
            "id": 150,
            "name": "Micro\u00e9conomie 2"
        },
        {
            "id": 151,
            "name": "Macro\u00e9conomie 2"
        },
        {
            "id": 152,
            "name": "\u00c9conomie mon\u00e9taire"
        },
        {
            "id": 153,
            "name": "Statistiques appliqu\u00e9es"
        },
        {
            "id": 154,
            "name": "Finance"
        },
        {
            "id": 155,
            "name": "Comptabilit\u00e9"
        },
        {
            "id": 156,
            "name": "\u00c9conomie internationale"
        },
        {
            "id": 157,
            "name": "Gestion avanc\u00e9e"
        },
        {
            "id": 158,
            "name": "Analyse \u00e9conomique"
        },
        {
            "id": 159,
            "name": "Finance appliqu\u00e9e"
        },
        {
            "id": 160,
            "name": "\u00c9conomie des entreprises"
        },
        {
            "id": 161,
            "name": "Macro\u00e9conomie avanc\u00e9e"
        },
        {
            "id": 162,
            "name": "\u00c9conomie politique"
        },
        {
            "id": 163,
            "name": "Finance internationale"
        },
        {
            "id": 164,
            "name": "\u00c9conomie num\u00e9rique"
        },
        {
            "id": 165,
            "name": "Projet \u00e9conomique"
        },
        {
            "id": 166,
            "name": "Circuits \u00e9lectriques"
        },
        {
            "id": 167,
            "name": "\u00c9lectronique analogique"
        },
        {
            "id": 168,
            "name": "Math\u00e9matiques appliqu\u00e9es"
        },
        {
            "id": 169,
            "name": "Programmation"
        },
        {
            "id": 170,
            "name": "\u00c9lectronique num\u00e9rique"
        },
        {
            "id": 171,
            "name": "Microprocesseurs"
        },
        {
            "id": 172,
            "name": "Automatique"
        },
        {
            "id": 173,
            "name": "T\u00e9l\u00e9communications"
        },
        {
            "id": 174,
            "name": "Syst\u00e8mes embarqu\u00e9s"
        },
        {
            "id": 175,
            "name": "Instrumentation"
        },
        {
            "id": 176,
            "name": "Robotique"
        },
        {
            "id": 177,
            "name": "\u00c9lectronique avanc\u00e9e"
        },
        {
            "id": 178,
            "name": "\u00c9lectronique de puissance"
        },
        {
            "id": 179,
            "name": "Traitement du signal"
        },
        {
            "id": 180,
            "name": "Communication sans fil"
        },
        {
            "id": 181,
            "name": "R\u00e9seaux"
        },
        {
            "id": 182,
            "name": "Syst\u00e8mes intelligents"
        },
        {
            "id": 183,
            "name": "Micro\u00e9lectronique"
        },
        {
            "id": 184,
            "name": "Robotique avanc\u00e9e"
        },
        {
            "id": 185,
            "name": "Projet industriel"
        }
    ],
    "formation_year_modules": [
        {
            "id": 186,
            "formation_year_id": 1,
            "module_id": 1
        },
        {
            "id": 187,
            "formation_year_id": 1,
            "module_id": 2
        },
        {
            "id": 188,
            "formation_year_id": 1,
            "module_id": 3
        },
        {
            "id": 189,
            "formation_year_id": 1,
            "module_id": 4
        },
        {
            "id": 190,
            "formation_year_id": 1,
            "module_id": 5
        },
        {
            "id": 191,
            "formation_year_id": 2,
            "module_id": 6
        },
        {
            "id": 192,
            "formation_year_id": 2,
            "module_id": 7
        },
        {
            "id": 193,
            "formation_year_id": 2,
            "module_id": 8
        },
        {
            "id": 194,
            "formation_year_id": 2,
            "module_id": 9
        },
        {
            "id": 195,
            "formation_year_id": 2,
            "module_id": 10
        },
        {
            "id": 196,
            "formation_year_id": 3,
            "module_id": 11
        },
        {
            "id": 197,
            "formation_year_id": 3,
            "module_id": 12
        },
        {
            "id": 198,
            "formation_year_id": 3,
            "module_id": 13
        },
        {
            "id": 199,
            "formation_year_id": 3,
            "module_id": 14
        },
        {
            "id": 200,
            "formation_year_id": 3,
            "module_id": 15
        },
        {
            "id": 201,
            "formation_year_id": 4,
            "module_id": 16
        },
        {
            "id": 202,
            "formation_year_id": 4,
            "module_id": 17
        },
        {
            "id": 203,
            "formation_year_id": 4,
            "module_id": 18
        },
        {
            "id": 204,
            "formation_year_id": 4,
            "module_id": 19
        },
        {
            "id": 205,
            "formation_year_id": 4,
            "module_id": 20
        },
        {
            "id": 206,
            "formation_year_id": 5,
            "module_id": 21
        },
        {
            "id": 207,
            "formation_year_id": 5,
            "module_id": 22
        },
        {
            "id": 208,
            "formation_year_id": 5,
            "module_id": 23
        },
        {
            "id": 209,
            "formation_year_id": 5,
            "module_id": 24
        },
        {
            "id": 210,
            "formation_year_id": 5,
            "module_id": 25
        },
        {
            "id": 211,
            "formation_year_id": 6,
            "module_id": 26
        },
        {
            "id": 212,
            "formation_year_id": 6,
            "module_id": 27
        },
        {
            "id": 213,
            "formation_year_id": 6,
            "module_id": 28
        },
        {
            "id": 214,
            "formation_year_id": 6,
            "module_id": 29
        },
        {
            "id": 215,
            "formation_year_id": 6,
            "module_id": 30
        },
        {
            "id": 216,
            "formation_year_id": 7,
            "module_id": 31
        },
        {
            "id": 217,
            "formation_year_id": 7,
            "module_id": 32
        },
        {
            "id": 218,
            "formation_year_id": 7,
            "module_id": 33
        },
        {
            "id": 219,
            "formation_year_id": 7,
            "module_id": 34
        },
        {
            "id": 220,
            "formation_year_id": 7,
            "module_id": 35
        },
        {
            "id": 221,
            "formation_year_id": 8,
            "module_id": 36
        },
        {
            "id": 222,
            "formation_year_id": 8,
            "module_id": 37
        },
        {
            "id": 223,
            "formation_year_id": 8,
            "module_id": 38
        },
        {
            "id": 224,
            "formation_year_id": 8,
            "module_id": 39
        },
        {
            "id": 225,
            "formation_year_id": 8,
            "module_id": 40
        },
        {
            "id": 226,
            "formation_year_id": 9,
            "module_id": 41
        },
        {
            "id": 227,
            "formation_year_id": 9,
            "module_id": 42
        },
        {
            "id": 228,
            "formation_year_id": 9,
            "module_id": 43
        },
        {
            "id": 229,
            "formation_year_id": 9,
            "module_id": 44
        },
        {
            "id": 230,
            "formation_year_id": 9,
            "module_id": 45
        },
        {
            "id": 231,
            "formation_year_id": 10,
            "module_id": 46
        },
        {
            "id": 232,
            "formation_year_id": 10,
            "module_id": 47
        },
        {
            "id": 233,
            "formation_year_id": 10,
            "module_id": 48
        },
        {
            "id": 234,
            "formation_year_id": 10,
            "module_id": 49
        },
        {
            "id": 235,
            "formation_year_id": 10,
            "module_id": 50
        },
        {
            "id": 236,
            "formation_year_id": 11,
            "module_id": 51
        },
        {
            "id": 237,
            "formation_year_id": 11,
            "module_id": 52
        },
        {
            "id": 238,
            "formation_year_id": 11,
            "module_id": 53
        },
        {
            "id": 239,
            "formation_year_id": 11,
            "module_id": 54
        },
        {
            "id": 240,
            "formation_year_id": 11,
            "module_id": 55
        },
        {
            "id": 241,
            "formation_year_id": 12,
            "module_id": 56
        },
        {
            "id": 242,
            "formation_year_id": 12,
            "module_id": 57
        },
        {
            "id": 243,
            "formation_year_id": 12,
            "module_id": 58
        },
        {
            "id": 244,
            "formation_year_id": 12,
            "module_id": 59
        },
        {
            "id": 245,
            "formation_year_id": 12,
            "module_id": 60
        },
        {
            "id": 246,
            "formation_year_id": 13,
            "module_id": 61
        },
        {
            "id": 247,
            "formation_year_id": 13,
            "module_id": 62
        },
        {
            "id": 248,
            "formation_year_id": 13,
            "module_id": 63
        },
        {
            "id": 249,
            "formation_year_id": 13,
            "module_id": 64
        },
        {
            "id": 250,
            "formation_year_id": 13,
            "module_id": 65
        },
        {
            "id": 251,
            "formation_year_id": 14,
            "module_id": 66
        },
        {
            "id": 252,
            "formation_year_id": 14,
            "module_id": 67
        },
        {
            "id": 253,
            "formation_year_id": 14,
            "module_id": 68
        },
        {
            "id": 254,
            "formation_year_id": 14,
            "module_id": 69
        },
        {
            "id": 255,
            "formation_year_id": 15,
            "module_id": 70
        },
        {
            "id": 256,
            "formation_year_id": 15,
            "module_id": 71
        },
        {
            "id": 257,
            "formation_year_id": 15,
            "module_id": 72
        },
        {
            "id": 258,
            "formation_year_id": 15,
            "module_id": 73
        },
        {
            "id": 259,
            "formation_year_id": 16,
            "module_id": 74
        },
        {
            "id": 260,
            "formation_year_id": 16,
            "module_id": 75
        },
        {
            "id": 261,
            "formation_year_id": 16,
            "module_id": 76
        },
        {
            "id": 262,
            "formation_year_id": 16,
            "module_id": 77
        },
        {
            "id": 263,
            "formation_year_id": 17,
            "module_id": 78
        },
        {
            "id": 264,
            "formation_year_id": 17,
            "module_id": 79
        },
        {
            "id": 265,
            "formation_year_id": 17,
            "module_id": 80
        },
        {
            "id": 266,
            "formation_year_id": 17,
            "module_id": 81
        },
        {
            "id": 267,
            "formation_year_id": 18,
            "module_id": 82
        },
        {
            "id": 268,
            "formation_year_id": 18,
            "module_id": 83
        },
        {
            "id": 269,
            "formation_year_id": 18,
            "module_id": 84
        },
        {
            "id": 270,
            "formation_year_id": 18,
            "module_id": 85
        },
        {
            "id": 271,
            "formation_year_id": 19,
            "module_id": 86
        },
        {
            "id": 272,
            "formation_year_id": 19,
            "module_id": 87
        },
        {
            "id": 273,
            "formation_year_id": 19,
            "module_id": 88
        },
        {
            "id": 274,
            "formation_year_id": 19,
            "module_id": 89
        },
        {
            "id": 275,
            "formation_year_id": 20,
            "module_id": 90
        },
        {
            "id": 276,
            "formation_year_id": 20,
            "module_id": 91
        },
        {
            "id": 277,
            "formation_year_id": 20,
            "module_id": 92
        },
        {
            "id": 278,
            "formation_year_id": 20,
            "module_id": 93
        },
        {
            "id": 279,
            "formation_year_id": 21,
            "module_id": 94
        },
        {
            "id": 280,
            "formation_year_id": 21,
            "module_id": 95
        },
        {
            "id": 281,
            "formation_year_id": 21,
            "module_id": 96
        },
        {
            "id": 282,
            "formation_year_id": 21,
            "module_id": 97
        },
        {
            "id": 283,
            "formation_year_id": 22,
            "module_id": 98
        },
        {
            "id": 284,
            "formation_year_id": 22,
            "module_id": 99
        },
        {
            "id": 285,
            "formation_year_id": 22,
            "module_id": 100
        },
        {
            "id": 286,
            "formation_year_id": 22,
            "module_id": 101
        },
        {
            "id": 287,
            "formation_year_id": 23,
            "module_id": 102
        },
        {
            "id": 288,
            "formation_year_id": 23,
            "module_id": 103
        },
        {
            "id": 289,
            "formation_year_id": 23,
            "module_id": 104
        },
        {
            "id": 290,
            "formation_year_id": 23,
            "module_id": 105
        },
        {
            "id": 291,
            "formation_year_id": 24,
            "module_id": 106
        },
        {
            "id": 292,
            "formation_year_id": 24,
            "module_id": 107
        },
        {
            "id": 293,
            "formation_year_id": 24,
            "module_id": 108
        },
        {
            "id": 294,
            "formation_year_id": 24,
            "module_id": 109
        },
        {
            "id": 295,
            "formation_year_id": 25,
            "module_id": 110
        },
        {
            "id": 296,
            "formation_year_id": 25,
            "module_id": 111
        },
        {
            "id": 297,
            "formation_year_id": 25,
            "module_id": 112
        },
        {
            "id": 298,
            "formation_year_id": 25,
            "module_id": 113
        },
        {
            "id": 299,
            "formation_year_id": 26,
            "module_id": 114
        },
        {
            "id": 300,
            "formation_year_id": 26,
            "module_id": 115
        },
        {
            "id": 301,
            "formation_year_id": 26,
            "module_id": 116
        },
        {
            "id": 302,
            "formation_year_id": 26,
            "module_id": 117
        },
        {
            "id": 303,
            "formation_year_id": 27,
            "module_id": 118
        },
        {
            "id": 304,
            "formation_year_id": 27,
            "module_id": 119
        },
        {
            "id": 305,
            "formation_year_id": 27,
            "module_id": 120
        },
        {
            "id": 306,
            "formation_year_id": 27,
            "module_id": 121
        },
        {
            "id": 307,
            "formation_year_id": 28,
            "module_id": 122
        },
        {
            "id": 308,
            "formation_year_id": 28,
            "module_id": 123
        },
        {
            "id": 309,
            "formation_year_id": 28,
            "module_id": 124
        },
        {
            "id": 310,
            "formation_year_id": 28,
            "module_id": 125
        },
        {
            "id": 311,
            "formation_year_id": 29,
            "module_id": 126
        },
        {
            "id": 312,
            "formation_year_id": 29,
            "module_id": 127
        },
        {
            "id": 313,
            "formation_year_id": 29,
            "module_id": 128
        },
        {
            "id": 314,
            "formation_year_id": 29,
            "module_id": 129
        },
        {
            "id": 315,
            "formation_year_id": 30,
            "module_id": 130
        },
        {
            "id": 316,
            "formation_year_id": 30,
            "module_id": 131
        },
        {
            "id": 317,
            "formation_year_id": 30,
            "module_id": 132
        },
        {
            "id": 318,
            "formation_year_id": 30,
            "module_id": 133
        },
        {
            "id": 319,
            "formation_year_id": 31,
            "module_id": 134
        },
        {
            "id": 320,
            "formation_year_id": 31,
            "module_id": 135
        },
        {
            "id": 321,
            "formation_year_id": 31,
            "module_id": 136
        },
        {
            "id": 322,
            "formation_year_id": 31,
            "module_id": 137
        },
        {
            "id": 323,
            "formation_year_id": 32,
            "module_id": 138
        },
        {
            "id": 324,
            "formation_year_id": 32,
            "module_id": 139
        },
        {
            "id": 325,
            "formation_year_id": 32,
            "module_id": 140
        },
        {
            "id": 326,
            "formation_year_id": 32,
            "module_id": 141
        },
        {
            "id": 327,
            "formation_year_id": 33,
            "module_id": 142
        },
        {
            "id": 328,
            "formation_year_id": 33,
            "module_id": 143
        },
        {
            "id": 329,
            "formation_year_id": 33,
            "module_id": 144
        },
        {
            "id": 330,
            "formation_year_id": 33,
            "module_id": 145
        },
        {
            "id": 331,
            "formation_year_id": 34,
            "module_id": 146
        },
        {
            "id": 332,
            "formation_year_id": 34,
            "module_id": 147
        },
        {
            "id": 333,
            "formation_year_id": 34,
            "module_id": 148
        },
        {
            "id": 334,
            "formation_year_id": 34,
            "module_id": 149
        },
        {
            "id": 335,
            "formation_year_id": 35,
            "module_id": 150
        },
        {
            "id": 336,
            "formation_year_id": 35,
            "module_id": 151
        },
        {
            "id": 337,
            "formation_year_id": 35,
            "module_id": 152
        },
        {
            "id": 338,
            "formation_year_id": 35,
            "module_id": 153
        },
        {
            "id": 339,
            "formation_year_id": 36,
            "module_id": 154
        },
        {
            "id": 340,
            "formation_year_id": 36,
            "module_id": 155
        },
        {
            "id": 341,
            "formation_year_id": 36,
            "module_id": 156
        },
        {
            "id": 342,
            "formation_year_id": 36,
            "module_id": 157
        },
        {
            "id": 343,
            "formation_year_id": 37,
            "module_id": 158
        },
        {
            "id": 344,
            "formation_year_id": 37,
            "module_id": 159
        },
        {
            "id": 345,
            "formation_year_id": 37,
            "module_id": 160
        },
        {
            "id": 346,
            "formation_year_id": 37,
            "module_id": 161
        },
        {
            "id": 347,
            "formation_year_id": 38,
            "module_id": 162
        },
        {
            "id": 348,
            "formation_year_id": 38,
            "module_id": 163
        },
        {
            "id": 349,
            "formation_year_id": 38,
            "module_id": 164
        },
        {
            "id": 350,
            "formation_year_id": 38,
            "module_id": 165
        },
        {
            "id": 351,
            "formation_year_id": 39,
            "module_id": 166
        },
        {
            "id": 352,
            "formation_year_id": 39,
            "module_id": 167
        },
        {
            "id": 353,
            "formation_year_id": 39,
            "module_id": 168
        },
        {
            "id": 354,
            "formation_year_id": 39,
            "module_id": 169
        },
        {
            "id": 355,
            "formation_year_id": 40,
            "module_id": 170
        },
        {
            "id": 356,
            "formation_year_id": 40,
            "module_id": 171
        },
        {
            "id": 357,
            "formation_year_id": 40,
            "module_id": 172
        },
        {
            "id": 358,
            "formation_year_id": 40,
            "module_id": 173
        },
        {
            "id": 359,
            "formation_year_id": 41,
            "module_id": 174
        },
        {
            "id": 360,
            "formation_year_id": 41,
            "module_id": 175
        },
        {
            "id": 361,
            "formation_year_id": 41,
            "module_id": 176
        },
        {
            "id": 362,
            "formation_year_id": 41,
            "module_id": 177
        },
        {
            "id": 363,
            "formation_year_id": 42,
            "module_id": 178
        },
        {
            "id": 364,
            "formation_year_id": 42,
            "module_id": 179
        },
        {
            "id": 365,
            "formation_year_id": 42,
            "module_id": 180
        },
        {
            "id": 366,
            "formation_year_id": 42,
            "module_id": 181
        },
        {
            "id": 367,
            "formation_year_id": 43,
            "module_id": 182
        },
        {
            "id": 368,
            "formation_year_id": 43,
            "module_id": 183
        },
        {
            "id": 369,
            "formation_year_id": 43,
            "module_id": 184
        },
        {
            "id": 370,
            "formation_year_id": 43,
            "module_id": 185
        },
        {
            "id": 371,
            "formation_year_id": 1,
            "module_id": 66
        },
        {
            "id": 372,
            "formation_year_id": 1,
            "module_id": 67
        },
        {
            "id": 373,
            "formation_year_id": 2,
            "module_id": 70
        },
        {
            "id": 374,
            "formation_year_id": 2,
            "module_id": 71
        },
        {
            "id": 375,
            "formation_year_id": 9,
            "module_id": 66
        },
        {
            "id": 376,
            "formation_year_id": 9,
            "module_id": 67
        },
        {
            "id": 377,
            "formation_year_id": 10,
            "module_id": 70
        },
        {
            "id": 378,
            "formation_year_id": 10,
            "module_id": 71
        }
    ],
    "groups": [
        {
            "id": 1,
            "group_number": 1,
            "formation_year_id": 1
        },
        {
            "id": 2,
            "group_number": 2,
            "formation_year_id": 1
        },
        {
            "id": 3,
            "group_number": 3,
            "formation_year_id": 1
        },
        {
            "id": 4,
            "group_number": 1,
            "formation_year_id": 2
        },
        {
            "id": 5,
            "group_number": 2,
            "formation_year_id": 2
        },
        {
            "id": 6,
            "group_number": 3,
            "formation_year_id": 2
        },
        {
            "id": 7,
            "group_number": 1,
            "formation_year_id": 3
        },
        {
            "id": 8,
            "group_number": 2,
            "formation_year_id": 3
        },
        {
            "id": 9,
            "group_number": 3,
            "formation_year_id": 3
        },
        {
            "id": 10,
            "group_number": 1,
            "formation_year_id": 4
        },
        {
            "id": 11,
            "group_number": 2,
            "formation_year_id": 4
        },
        {
            "id": 12,
            "group_number": 3,
            "formation_year_id": 4
        },
        {
            "id": 13,
            "group_number": 1,
            "formation_year_id": 5
        },
        {
            "id": 14,
            "group_number": 2,
            "formation_year_id": 5
        },
        {
            "id": 15,
            "group_number": 1,
            "formation_year_id": 6
        },
        {
            "id": 16,
            "group_number": 2,
            "formation_year_id": 6
        },
        {
            "id": 17,
            "group_number": 3,
            "formation_year_id": 6
        },
        {
            "id": 18,
            "group_number": 1,
            "formation_year_id": 7
        },
        {
            "id": 19,
            "group_number": 2,
            "formation_year_id": 7
        },
        {
            "id": 20,
            "group_number": 3,
            "formation_year_id": 7
        },
        {
            "id": 21,
            "group_number": 1,
            "formation_year_id": 8
        },
        {
            "id": 22,
            "group_number": 2,
            "formation_year_id": 8
        },
        {
            "id": 23,
            "group_number": 3,
            "formation_year_id": 8
        },
        {
            "id": 24,
            "group_number": 1,
            "formation_year_id": 9
        },
        {
            "id": 25,
            "group_number": 2,
            "formation_year_id": 9
        },
        {
            "id": 26,
            "group_number": 3,
            "formation_year_id": 9
        },
        {
            "id": 27,
            "group_number": 1,
            "formation_year_id": 10
        },
        {
            "id": 28,
            "group_number": 2,
            "formation_year_id": 10
        },
        {
            "id": 29,
            "group_number": 3,
            "formation_year_id": 10
        },
        {
            "id": 30,
            "group_number": 1,
            "formation_year_id": 11
        },
        {
            "id": 31,
            "group_number": 2,
            "formation_year_id": 11
        },
        {
            "id": 32,
            "group_number": 3,
            "formation_year_id": 11
        },
        {
            "id": 33,
            "group_number": 1,
            "formation_year_id": 12
        },
        {
            "id": 34,
            "group_number": 2,
            "formation_year_id": 12
        },
        {
            "id": 35,
            "group_number": 3,
            "formation_year_id": 12
        },
        {
            "id": 36,
            "group_number": 1,
            "formation_year_id": 13
        },
        {
            "id": 37,
            "group_number": 2,
            "formation_year_id": 13
        },
        {
            "id": 38,
            "group_number": 3,
            "formation_year_id": 13
        },
        {
            "id": 39,
            "group_number": 1,
            "formation_year_id": 14
        },
        {
            "id": 40,
            "group_number": 2,
            "formation_year_id": 14
        },
        {
            "id": 41,
            "group_number": 3,
            "formation_year_id": 14
        },
        {
            "id": 42,
            "group_number": 1,
            "formation_year_id": 15
        },
        {
            "id": 43,
            "group_number": 2,
            "formation_year_id": 15
        },
        {
            "id": 44,
            "group_number": 3,
            "formation_year_id": 15
        },
        {
            "id": 45,
            "group_number": 1,
            "formation_year_id": 16
        },
        {
            "id": 46,
            "group_number": 2,
            "formation_year_id": 16
        },
        {
            "id": 47,
            "group_number": 3,
            "formation_year_id": 16
        },
        {
            "id": 48,
            "group_number": 1,
            "formation_year_id": 17
        },
        {
            "id": 49,
            "group_number": 2,
            "formation_year_id": 17
        },
        {
            "id": 50,
            "group_number": 1,
            "formation_year_id": 18
        },
        {
            "id": 51,
            "group_number": 2,
            "formation_year_id": 18
        },
        {
            "id": 52,
            "group_number": 1,
            "formation_year_id": 19
        },
        {
            "id": 53,
            "group_number": 2,
            "formation_year_id": 19
        },
        {
            "id": 54,
            "group_number": 1,
            "formation_year_id": 20
        },
        {
            "id": 55,
            "group_number": 2,
            "formation_year_id": 20
        },
        {
            "id": 56,
            "group_number": 3,
            "formation_year_id": 20
        },
        {
            "id": 57,
            "group_number": 1,
            "formation_year_id": 21
        },
        {
            "id": 58,
            "group_number": 2,
            "formation_year_id": 21
        },
        {
            "id": 59,
            "group_number": 3,
            "formation_year_id": 21
        },
        {
            "id": 60,
            "group_number": 1,
            "formation_year_id": 22
        },
        {
            "id": 61,
            "group_number": 2,
            "formation_year_id": 22
        },
        {
            "id": 62,
            "group_number": 1,
            "formation_year_id": 23
        },
        {
            "id": 63,
            "group_number": 2,
            "formation_year_id": 23
        },
        {
            "id": 64,
            "group_number": 1,
            "formation_year_id": 24
        },
        {
            "id": 65,
            "group_number": 2,
            "formation_year_id": 24
        },
        {
            "id": 66,
            "group_number": 1,
            "formation_year_id": 25
        },
        {
            "id": 67,
            "group_number": 2,
            "formation_year_id": 25
        },
        {
            "id": 68,
            "group_number": 3,
            "formation_year_id": 25
        },
        {
            "id": 69,
            "group_number": 1,
            "formation_year_id": 26
        },
        {
            "id": 70,
            "group_number": 2,
            "formation_year_id": 26
        },
        {
            "id": 71,
            "group_number": 3,
            "formation_year_id": 26
        },
        {
            "id": 72,
            "group_number": 1,
            "formation_year_id": 27
        },
        {
            "id": 73,
            "group_number": 2,
            "formation_year_id": 27
        },
        {
            "id": 74,
            "group_number": 1,
            "formation_year_id": 28
        },
        {
            "id": 75,
            "group_number": 2,
            "formation_year_id": 28
        },
        {
            "id": 76,
            "group_number": 1,
            "formation_year_id": 29
        },
        {
            "id": 77,
            "group_number": 2,
            "formation_year_id": 29
        },
        {
            "id": 78,
            "group_number": 1,
            "formation_year_id": 30
        },
        {
            "id": 79,
            "group_number": 2,
            "formation_year_id": 30
        },
        {
            "id": 80,
            "group_number": 3,
            "formation_year_id": 30
        },
        {
            "id": 81,
            "group_number": 1,
            "formation_year_id": 31
        },
        {
            "id": 82,
            "group_number": 2,
            "formation_year_id": 31
        },
        {
            "id": 83,
            "group_number": 3,
            "formation_year_id": 31
        },
        {
            "id": 84,
            "group_number": 1,
            "formation_year_id": 32
        },
        {
            "id": 85,
            "group_number": 2,
            "formation_year_id": 32
        },
        {
            "id": 86,
            "group_number": 1,
            "formation_year_id": 33
        },
        {
            "id": 87,
            "group_number": 2,
            "formation_year_id": 33
        },
        {
            "id": 88,
            "group_number": 1,
            "formation_year_id": 34
        },
        {
            "id": 89,
            "group_number": 2,
            "formation_year_id": 34
        },
        {
            "id": 90,
            "group_number": 3,
            "formation_year_id": 34
        },
        {
            "id": 91,
            "group_number": 1,
            "formation_year_id": 35
        },
        {
            "id": 92,
            "group_number": 2,
            "formation_year_id": 35
        },
        {
            "id": 93,
            "group_number": 3,
            "formation_year_id": 35
        },
        {
            "id": 94,
            "group_number": 1,
            "formation_year_id": 36
        },
        {
            "id": 95,
            "group_number": 2,
            "formation_year_id": 36
        },
        {
            "id": 96,
            "group_number": 3,
            "formation_year_id": 36
        },
        {
            "id": 97,
            "group_number": 1,
            "formation_year_id": 37
        },
        {
            "id": 98,
            "group_number": 2,
            "formation_year_id": 37
        },
        {
            "id": 99,
            "group_number": 3,
            "formation_year_id": 37
        },
        {
            "id": 100,
            "group_number": 1,
            "formation_year_id": 38
        },
        {
            "id": 101,
            "group_number": 2,
            "formation_year_id": 38
        },
        {
            "id": 102,
            "group_number": 1,
            "formation_year_id": 39
        },
        {
            "id": 103,
            "group_number": 2,
            "formation_year_id": 39
        },
        {
            "id": 104,
            "group_number": 1,
            "formation_year_id": 40
        },
        {
            "id": 105,
            "group_number": 2,
            "formation_year_id": 40
        },
        {
            "id": 106,
            "group_number": 3,
            "formation_year_id": 40
        },
        {
            "id": 107,
            "group_number": 1,
            "formation_year_id": 41
        },
        {
            "id": 108,
            "group_number": 2,
            "formation_year_id": 41
        },
        {
            "id": 109,
            "group_number": 3,
            "formation_year_id": 41
        },
        {
            "id": 110,
            "group_number": 1,
            "formation_year_id": 42
        },
        {
            "id": 111,
            "group_number": 2,
            "formation_year_id": 42
        },
        {
            "id": 112,
            "group_number": 1,
            "formation_year_id": 43
        },
        {
            "id": 113,
            "group_number": 2,
            "formation_year_id": 43
        }
    ],
    "professors": [
        {
            "id": 1,
            "first_name": "Mohamed",
            "last_name": "Maouch",
            "department_id": 1,
            "matricule": "20260000001"
        },
        {
            "id": 2,
            "first_name": "Ahmed",
            "last_name": "Gaceb",
            "department_id": 1,
            "matricule": "20260000002"
        },
        {
            "id": 3,
            "first_name": "Yacine",
            "last_name": "Boughanem",
            "department_id": 1,
            "matricule": "20260000003"
        },
        {
            "id": 4,
            "first_name": "yousra",
            "last_name": "Nessnese",
            "department_id": 1,
            "matricule": "20260000004"
        },
        {
            "id": 5,
            "first_name": "Nabil",
            "last_name": "Chaoueche",
            "department_id": 1,
            "matricule": "20260000005"
        },
        {
            "id": 6,
            "first_name": "Amine",
            "last_name": "Oueld babali",
            "department_id": 1,
            "matricule": "20260000006"
        },
        {
            "id": 7,
            "first_name": "Walid",
            "last_name": "Toumi",
            "department_id": 1,
            "matricule": "20260000007"
        },
        {
            "id": 8,
            "first_name": "Samir",
            "last_name": "Belkacem",
            "department_id": 1,
            "matricule": "20260000008"
        },
        {
            "id": 9,
            "first_name": "Fares",
            "last_name": "Mansouri",
            "department_id": 1,
            "matricule": "20260000009"
        },
        {
            "id": 10,
            "first_name": "Hichem",
            "last_name": "Larbi",
            "department_id": 1,
            "matricule": "20260000010"
        },
        {
            "id": 11,
            "first_name": "Riad",
            "last_name": "Khelifi",
            "department_id": 1,
            "matricule": "20260000011"
        },
        {
            "id": 12,
            "first_name": "Islam",
            "last_name": "Meziani",
            "department_id": 1,
            "matricule": "20260000012"
        },
        {
            "id": 13,
            "first_name": "Adel",
            "last_name": "Hamidi",
            "department_id": 1,
            "matricule": "20260000013"
        },
        {
            "id": 14,
            "first_name": "Sofiane",
            "last_name": "Benaissa",
            "department_id": 1,
            "matricule": "20260000014"
        },
        {
            "id": 15,
            "first_name": "Abdelkader",
            "last_name": "Rahmani",
            "department_id": 2,
            "matricule": "20260000015"
        },
        {
            "id": 16,
            "first_name": "Mustapha",
            "last_name": "Benali",
            "department_id": 2,
            "matricule": "20260000016"
        },
        {
            "id": 17,
            "first_name": "Noureddine",
            "last_name": "Haddad",
            "department_id": 2,
            "matricule": "20260000017"
        },
        {
            "id": 18,
            "first_name": "Lotfi",
            "last_name": "Dahmani",
            "department_id": 2,
            "matricule": "20260000018"
        },
        {
            "id": 19,
            "first_name": "Lakhdar",
            "last_name": "AitAhmed",
            "department_id": 2,
            "matricule": "20260000019"
        },
        {
            "id": 20,
            "first_name": "Salah",
            "last_name": "Mokhtari",
            "department_id": 2,
            "matricule": "20260000020"
        },
        {
            "id": 21,
            "first_name": "Kamel",
            "last_name": "Bouzid",
            "department_id": 2,
            "matricule": "20260000021"
        },
        {
            "id": 22,
            "first_name": "Brahim",
            "last_name": "Ouali",
            "department_id": 2,
            "matricule": "20260000022"
        },
        {
            "id": 23,
            "first_name": "Rachid",
            "last_name": "Kaci",
            "department_id": 3,
            "matricule": "20260000023"
        },
        {
            "id": 24,
            "first_name": "Mourad",
            "last_name": "Benyoucef",
            "department_id": 3,
            "matricule": "20260000024"
        },
        {
            "id": 25,
            "first_name": "Youssef",
            "last_name": "Amrani",
            "department_id": 3,
            "matricule": "20260000025"
        },
        {
            "id": 26,
            "first_name": "Hakim",
            "last_name": "Ziani",
            "department_id": 3,
            "matricule": "20260000026"
        },
        {
            "id": 27,
            "first_name": "Djamel",
            "last_name": "Bouhadjar",
            "department_id": 3,
            "matricule": "20260000027"
        },
        {
            "id": 28,
            "first_name": "Nasser",
            "last_name": "Belaid",
            "department_id": 3,
            "matricule": "20260000028"
        },
        {
            "id": 29,
            "first_name": "Farid",
            "last_name": "Boudiaf",
            "department_id": 3,
            "matricule": "20260000029"
        },
        {
            "id": 30,
            "first_name": "Amina",
            "last_name": "Boumaza",
            "department_id": 4,
            "matricule": "20260000030"
        },
        {
            "id": 31,
            "first_name": "Nadia",
            "last_name": "Kherroubi",
            "department_id": 4,
            "matricule": "20260000031"
        },
        {
            "id": 32,
            "first_name": "Samia",
            "last_name": "Benamar",
            "department_id": 4,
            "matricule": "20260000032"
        },
        {
            "id": 33,
            "first_name": "Lamia",
            "last_name": "Sahraoui",
            "department_id": 4,
            "matricule": "20260000033"
        },
        {
            "id": 34,
            "first_name": "Karima",
            "last_name": "Touil",
            "department_id": 4,
            "matricule": "20260000034"
        },
        {
            "id": 35,
            "first_name": "Souad",
            "last_name": "Bouchareb",
            "department_id": 4,
            "matricule": "20260000035"
        },
        {
            "id": 36,
            "first_name": "Fatima",
            "last_name": "Mecheri",
            "department_id": 4,
            "matricule": "20260000036"
        },
        {
            "id": 37,
            "first_name": "Khadidja",
            "last_name": "Benaouda",
            "department_id": 5,
            "matricule": "20260000037"
        },
        {
            "id": 38,
            "first_name": "Malika",
            "last_name": "Boulahcen",
            "department_id": 5,
            "matricule": "20260000038"
        },
        {
            "id": 39,
            "first_name": "Zohra",
            "last_name": "Boualem",
            "department_id": 5,
            "matricule": "20260000039"
        },
        {
            "id": 40,
            "first_name": "Naima",
            "last_name": "Bencheikh",
            "department_id": 5,
            "matricule": "20260000040"
        },
        {
            "id": 41,
            "first_name": "Houria",
            "last_name": "Belabbes",
            "department_id": 5,
            "matricule": "20260000041"
        },
        {
            "id": 42,
            "first_name": "Fouzia",
            "last_name": "Aouadi",
            "department_id": 5,
            "matricule": "20260000042"
        },
        {
            "id": 43,
            "first_name": "Salima",
            "last_name": "Messaoudi",
            "department_id": 5,
            "matricule": "20260000043"
        },
        {
            "id": 44,
            "first_name": "Yamina",
            "last_name": "Bouziane",
            "department_id": 5,
            "matricule": "20260000044"
        },
        {
            "id": 45,
            "first_name": "Abderrahmane",
            "last_name": "Ferhat",
            "department_id": 6,
            "matricule": "20260000045"
        },
        {
            "id": 46,
            "first_name": "Mounir",
            "last_name": "Benabdelkader",
            "department_id": 6,
            "matricule": "20260000046"
        },
        {
            "id": 47,
            "first_name": "Said",
            "last_name": "Kouadria",
            "department_id": 6,
            "matricule": "20260000047"
        },
        {
            "id": 48,
            "first_name": "Hakim",
            "last_name": "Teguia",
            "department_id": 6,
            "matricule": "20260000048"
        },
        {
            "id": 49,
            "first_name": "Noureddine",
            "last_name": "Bouchenafa",
            "department_id": 6,
            "matricule": "20260000049"
        },
        {
            "id": 50,
            "first_name": "Khaled",
            "last_name": "Merabet",
            "department_id": 6,
            "matricule": "20260000050"
        },
        {
            "id": 51,
            "first_name": "Reda",
            "last_name": "Saadallah",
            "department_id": 6,
            "matricule": "20260000051"
        },
        {
            "id": 52,
            "first_name": "Anis",
            "last_name": "Bouaziz",
            "department_id": 6,
            "matricule": "20260000052"
        },
        {
            "id": 53,
            "first_name": "Bilal",
            "last_name": "Khenissi",
            "department_id": 6,
            "matricule": "20260000053"
        },
        {
            "id": 54,
            "first_name": "Toufik",
            "last_name": "Benatia",
            "department_id": 7,
            "matricule": "20260000054"
        },
        {
            "id": 55,
            "first_name": "Mounir",
            "last_name": "Kaci",
            "department_id": 7,
            "matricule": "20260000055"
        },
        {
            "id": 56,
            "first_name": "Azzedine",
            "last_name": "Belhadj",
            "department_id": 7,
            "matricule": "20260000056"
        },
        {
            "id": 57,
            "first_name": "Samy",
            "last_name": "Belaidi",
            "department_id": 7,
            "matricule": "20260000057"
        },
        {
            "id": 58,
            "first_name": "Hocine",
            "last_name": "Ghomari",
            "department_id": 7,
            "matricule": "20260000058"
        },
        {
            "id": 59,
            "first_name": "Nadir",
            "last_name": "Bensalem",
            "department_id": 7,
            "matricule": "20260000059"
        },
        {
            "id": 60,
            "first_name": "Youcef",
            "last_name": "AitMokhtar",
            "department_id": 7,
            "matricule": "20260000060"
        }
    ],
    "classrooms": [
        {
            "id": 1,
            "name": "100",
            "capacity": 40,
            "type": "amphi",
            "department_id": 1
        },
        {
            "id": 2,
            "name": "101",
            "capacity": 40,
            "type": "amphi",
            "department_id": 1
        },
        {
            "id": 3,
            "name": "1",
            "capacity": 40,
            "type": "amphi",
            "department_id": 1
        },
        {
            "id": 4,
            "name": "2",
            "capacity": 40,
            "type": "amphi",
            "department_id": 1
        },
        {
            "id": 5,
            "name": "3",
            "capacity": 40,
            "type": "amphi",
            "department_id": 1
        },
        {
            "id": 6,
            "name": "4",
            "capacity": 40,
            "type": "amphi",
            "department_id": 1
        },
        {
            "id": 7,
            "name": "A",
            "capacity": 40,
            "type": "amphi",
            "department_id": 2
        },
        {
            "id": 8,
            "name": "B",
            "capacity": 40,
            "type": "amphi",
            "department_id": 2
        },
        {
            "id": 9,
            "name": "7",
            "capacity": 40,
            "type": "amphi",
            "department_id": 3
        },
        {
            "id": 10,
            "name": "8",
            "capacity": 40,
            "type": "amphi",
            "department_id": 3
        },
        {
            "id": 11,
            "name": "9",
            "capacity": 40,
            "type": "amphi",
            "department_id": 3
        },
        {
            "id": 12,
            "name": "10",
            "capacity": 40,
            "type": "amphi",
            "department_id": 3
        },
        {
            "id": 13,
            "name": "11",
            "capacity": 40,
            "type": "amphi",
            "department_id": 3
        },
        {
            "id": 14,
            "name": "12",
            "capacity": 40,
            "type": "amphi",
            "department_id": 3
        },
        {
            "id": 15,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 16,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 17,
            "name": "CC3",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 18,
            "name": "4.100",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 19,
            "name": "4.202",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 20,
            "name": "5.300",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 21,
            "name": "5.301",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 22,
            "name": "6.101",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 23,
            "name": "6.102",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 24,
            "name": "6.103",
            "capacity": 20,
            "type": "class",
            "department_id": 1
        },
        {
            "id": 25,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 26,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 27,
            "name": "3.100",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 28,
            "name": "3.200",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 29,
            "name": "4.101",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 30,
            "name": "4.102",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 31,
            "name": "5.201",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 32,
            "name": "5.202",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 33,
            "name": "6.001",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 34,
            "name": "6.002",
            "capacity": 20,
            "type": "class",
            "department_id": 2
        },
        {
            "id": 35,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 36,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 37,
            "name": "CC3",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 38,
            "name": "2.100",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 39,
            "name": "2.200",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 40,
            "name": "3.101",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 41,
            "name": "3.102",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 42,
            "name": "4.201",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 43,
            "name": "4.202",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 44,
            "name": "5.101",
            "capacity": 20,
            "type": "class",
            "department_id": 3
        },
        {
            "id": 45,
            "name": "C1",
            "capacity": 40,
            "type": "amphi",
            "department_id": 4
        },
        {
            "id": 46,
            "name": "C2",
            "capacity": 40,
            "type": "amphi",
            "department_id": 4
        },
        {
            "id": 47,
            "name": "BioA",
            "capacity": 40,
            "type": "amphi",
            "department_id": 5
        },
        {
            "id": 48,
            "name": "BioB",
            "capacity": 40,
            "type": "amphi",
            "department_id": 5
        },
        {
            "id": 49,
            "name": "E1",
            "capacity": 40,
            "type": "amphi",
            "department_id": 6
        },
        {
            "id": 50,
            "name": "E2",
            "capacity": 40,
            "type": "amphi",
            "department_id": 6
        },
        {
            "id": 51,
            "name": "EL1",
            "capacity": 40,
            "type": "amphi",
            "department_id": 7
        },
        {
            "id": 52,
            "name": "EL2",
            "capacity": 40,
            "type": "amphi",
            "department_id": 7
        },
        {
            "id": 53,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 54,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 55,
            "name": "CC3",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 56,
            "name": "1.101",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 57,
            "name": "1.102",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 58,
            "name": "2.201",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 59,
            "name": "2.202",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 60,
            "name": "3.301",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 61,
            "name": "3.302",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 62,
            "name": "4.401",
            "capacity": 20,
            "type": "class",
            "department_id": 4
        },
        {
            "id": 63,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 64,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 65,
            "name": "CC3",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 66,
            "name": "1.110",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 67,
            "name": "1.120",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 68,
            "name": "2.210",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 69,
            "name": "2.220",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 70,
            "name": "3.310",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 71,
            "name": "3.320",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 72,
            "name": "4.410",
            "capacity": 20,
            "type": "class",
            "department_id": 5
        },
        {
            "id": 73,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 74,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 75,
            "name": "CC3",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 76,
            "name": "1.201",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 77,
            "name": "1.202",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 78,
            "name": "2.301",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 79,
            "name": "2.302",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 80,
            "name": "3.401",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 81,
            "name": "3.402",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 82,
            "name": "4.501",
            "capacity": 20,
            "type": "class",
            "department_id": 6
        },
        {
            "id": 83,
            "name": "CC1",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 84,
            "name": "CC2",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 85,
            "name": "CC3",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 86,
            "name": "1.301",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 87,
            "name": "1.302",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 88,
            "name": "2.401",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 89,
            "name": "2.402",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 90,
            "name": "3.501",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 91,
            "name": "3.502",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        },
        {
            "id": 92,
            "name": "4.601",
            "capacity": 20,
            "type": "class",
            "department_id": 7
        }
    ],
    "exams" : [
        {"id": 8,  "module_id": 23,  "exam_date": date(2025, 12, 24), "exam_time": time(13, 45)}
        ],
    "exam_sessions" : [
    {"id": '8_1', "exam_id": 8,  "classroom_id": 1, "group_id": 1, "part": None}
    ],
    "exam_supervisions" : [
    {"id": 1, "exam_session_id": '8_1', "professor_id": 1}
    ]
}