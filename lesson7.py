"""
game, user , card, worlds,

"""

db_games={
    'apex':[30, 1 ],
    'dota2':[0, 30],
    'MK':[0, 120],
    'CODMW':[10, 110],

}

db_wollet={
    1:[1515161616164516,1234,10000000],
    2:[1561561351613161,1029,0.5]
}


db_users={

         "user1" : ["coruit", {'games':[db_games['MK'],db_games['dota2']]}, {'wollet':db_wollet[1]}],
           "user2":["projok",{'games':[db_games['MK']]},{'wollet':db_wollet[2]}]
       }

class Bankomat:

    def main(self):
        self.user=input('enter your user name = ')
    def dt_user(self,user):
        if user not in db_users:
            print("tur joqal, qoy-boq")
            return 'tur joqol, qoy-boq'
    def get_game(self,game):
        self.game=int(input("chuse the game = "))
        print(game)
    def get_ga(self,game,user):
        if game==1:
            self.use1=(db_users[user][2]['wollet'][2])














