import requests
import json
from prettytable import PrettyTable

class BankDanychLokalnych:

    def tematy():
            
        #anonymous api
        tematy_glowne= "https://bdl.stat.gov.pl/api/v1/subjects?lang=pl&format=json"

        odpowiedz = requests.get(tematy_glowne)
        dane = json.loads(odpowiedz._content)

        tabela = PrettyTable()
        tabela.field_names = ['ID','Nazwa']

        for result in dane["results"]:
            tabela.add_row([result["id"], result["name"]])
            drildown = result["hasVariables"]
            x = [tabela,drildown]

        return x
    
    def subtematy(temat):

        #anonymous api
        url = f"https://bdl.stat.gov.pl/api/v1/subjects?parent-id={temat}&format=json"

        odpowiedz = requests.get(url)
        dane = json.loads(odpowiedz._content)

        tabela = PrettyTable()
        tabela.field_names = ['ID','Subtemat']

        for result in dane["results"]:
            tabela.add_row([result["id"], result["name"],])
            drildown = result["hasVariables"]
            x=[tabela,drildown]

        return x
    
    def dane(zmienna):
        
        #anonymous api
        #dane dla całej Polski (mozna dostosowac skrypt)
        url = f"https://bdl.stat.gov.pl/api/v1/data/by-variable/{zmienna}?format=json"

        odpowiedz = requests.get(url)
        dane = json.loads(odpowiedz._content)

        tabela = PrettyTable()
        tabela.field_names = ['Rok','Region','Wartość']

        for result in dane["results"]:
            for value in result["values"]:
                tabela.add_row([value["year"], result["name"], value["val"]])

        
        return tabela