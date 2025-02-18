#
# class Playmarket():
#
#      def get_game(self,db_games):
#          db_games = {
#           'apex':[30, 1],
#           'dota2':[0, 30],
#
#           'MK': [0, 120],
#           'CODMW': [10, 110]
#           }
#           self.db_games
#
#      def get_wallet(self,db_wollet):
#          db_wollet = {
#             1:[1234123412341234, 1234, 10000000],
#             2:[4321432143214321, 4321, 0.5]
#               }
#          self.db_wollet
#
#       def get_users(self,db_users,db_games,db_wollet):
#           db_users = {
#               "user1": ["corutin", {'games': [db_games['MK'], db_games['dota2']]}, {'wollet': db_wollet[1]}],
#               'user2': ["projok", {'games': [db_games['MK']]}, {'wollet': db_wollet[2]}]
#                }
#           self.db_users
#
#       def main(self,user,db_users):
#           user = input('entr your user name = ')
#           if user not in db_users:
#              print("tur joqal, qoy-boq")
#              return 'tur joqal, qoy-boq'
#       def get_game(self,game,db_games,db_users,user):
#           game = int(input("chuse the game  = "))
#           if game == 1:
#           if db_users[user][2]['wollet'][2] >= db_games['apex'][0]:
#               db_users[user][2]['wollet'][2] -= db_games['apex'][0]
#               print(f"siz shu apex sotib oldingiz!!!!")
#           else:
#              print("yoqolib qol")
#              return 'yoqolib qol'
#
#      def get(self,game,db_users,db_games,user):
#          if game == 2:
#          if db_users[user][2]['wollet'][2] >= db_games['apex'][0]:
#             db_users[user][2]['wollet'][2] - db_games['apex'][0]
#             print(f"siz shu apex sotib oldingiz!!!!")
#          else:
#             print("yoqolib qol")
#             return 'yoqolib qol'
#          if game == 3:
#             print(db_users[user][2]['wollet'][2] - db_games['MK'][0])
#          if game == 4:
#             print(db_users[user][2]['wollet'][2] - db_games['CODMW'][0])
#
#             print(db_users[user][2]['wollet'][2])
#














