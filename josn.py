# ->1
# import json
# import googlemaps
# from myapikey import APIKEY
#
# gmaps=googlemaps.Client(APIKEY)
# data=gmaps.geocode('Olmazor, Toshkent, Uzbekistan')
# #print(data)
#
#
# g=json.dumps(data[0], indent=4, sort_keys=True)
# print(g)


#  ->2
#
# import json
# import requests
# from pprint import pprint
#
# """
# wikiurl
# """
# wikiurl='https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext&redirects=1&titles=Qo\'qon'
# response=requests.get(wikiurl)
# pprint(json.dumps(response.json(), indent=4))
#

# ->3

#import json
# x=10
# print(x)
# print(type(x))
# x_json=json.dumps(x)
# print(x_json)
# print(type(x_json))

# y=5.6
# y_json=json.dumps(y)
# print(y_json)
# print(type(y_json))

# m=True
# print(m)
# print(type(m))
# m_json=json.dumps(m)
# print(m_json)
# print(type(m_json))
# m1_json=json.loads(m_json)
# print(m1_json)
#
# sonlar=(2,4,5,6,10)
# print(type(sonlar))
# sonlar_json=json.dumps(sonlar)
# print(sonlar_json[4])
#
#
# bemor={
#     'ism':'Alijon Valiyev',
#     'yosh':30,
#     'oila':True,
#     'farzandlar':('Ahmad,Bonue'),
#     'allergiya':None,
#     'dorilar':[
#         {'nomi':'analgin', 'miqdori':0.5},
#         {'nomi':'Pandol', 'miqdor':1.2}
# ]
# }
#

# json_bemor=json.dumps(bemor,indent=4)
# print(json_bemor)
# print(type(json_bemor))
#
#
# bemor2=json.loads(json_bemor)
# from pprint import pprint
# pprint(bemor2)
# print(type(bemor2))

#print(bemor.keys())
#print(bemor['dorilar'])

# with open('bemor_json.txt','w') as file:
#     json.dump(bemor,file)

# with open('sonlar_json.txt','w') as files:
#     json.dump(sonlar,files)

# filename='bemor_json.txt'
# with open(filename) as f:
#     bemor=json.load(f)
# print(type(bemor))

# file='sonlar_json.txt'
# with open(file) as fi:
#     sonlar3=json.load(fi)
#
# print(sonlar3)
#



# sonlar=(2,4,5,6,10)
# file='bemor_json.txt'
# with open(file,'a') as fi:
#     json.dump(sonlar,fi)






















