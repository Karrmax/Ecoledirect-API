import requests
import json
import datetime 

class EcoleDirect:
    """ Permet de se connecter et faire des requetes a l'API d'école direct
    Allow to connect and make requests to Ecoledirect's API """


    def __init__(self, username = None, password = None):
        """Create a new EcoleDirect object"""

        self.token = None
        self.id = None
        if username is not None and password is not None:
            self.connect(username, password)
        

    def __req(self, url, payload):
        """this function make all requests to the api"""
        return requests.post(url, data = payload)


    def connect(self, username : str, password : str):
        """create an connection to the API"""

        connection = self.__req('https://api.ecoledirecte.com/v3/login.awp', """data={}"identifiant": "{}","motdepasse": "{}"{}""".format("{",username, password, "}"))
        if connection.json()['code'] != 200:
            print("error ! bad username or password")
        else:
            self.token = connection.json()['token']
            self.id = connection.json()['data']['accounts'][0]['id']
            
    

    def getWT(self, startDate = datetime.date.today().strftime("%Y-%m-%d"), endDate = (datetime.date.today() + datetime.timedelta(days=6) ).strftime("%Y-%m-%d")):
        """get the work time from the api"""
        if self.token is None or self.id is None:
            print("Error connection must be acitvate")
            return

        connection = self.__req('https://api.ecoledirecte.com/v3/E/{}/emploidutemps.awp?verbe=get&'.format(self.id), """data={}"token":"{}","dateDebut": "{}","dateFin": "{}","avecTrous": false,{}""".format("{", self.token,startDate,endDate, "}"))
        if connection.json()['code'] != 200:
            print("error ! bad username or password")
        else:
            # self.token = connection.json()['token']
            return connection.json()['data']
    

    def getHW(self):
        """get homework from the api"""
        if self.token is None or self.id is None:
            print("Error connection must be acitvate")
            return   

        connection = self.__req('https://api.ecoledirecte.com/v3/Eleves/{}/cahierdetexte.awp?verbe=get&'.format(self.id), """data={}"token":"{}"{}""".format("{", self.token, "}"))
        if connection.json()['code'] != 200:
            print("error ! bad username or password")
        else:
            # self.token = connection.json()['token']
            return connection.json()['data']
            


    def getNotes(self):
        """get notes from the api"""
        if self.token is None or self.id is None:
            print("Error connection must be acitvate")
            return 
            
        connection = self.__req('https://api.ecoledirecte.com/v3/eleves/{}/notes.awp?verbe=get&'.format(self.id), """data={}"token":"{}"{}""".format("{", self.token, "}"))
        if connection.json()['code'] != 200:
            print("error ! bad username or password")
        else:
            # self.token = connection.json()['token']
            return connection.json()['data']


    def getSL(self):
        """get notes from the api"""
        if self.token is None or self.id is None:
            print("Error connection must be acitvate")
            return 
            
        connection = self.__req('https://api.ecoledirecte.com/v3/eleves/{}/viescolaire.awp?verbe=get&='.format(self.id), """data={}"token":"{}"{}""".format("{", self.token, "}"))
        if connection.json()['code'] != 200:
            print("error ! bad username or password")
        else:
            # self.token = connection.json()['token']
            return connection.json()['data'] 