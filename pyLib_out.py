#from deep_translator import GoogleTranslator

# translator = GoogleTranslator(source='uz', target='en')
# result = translator.translate("Python - dunyodagi eng mashhur dasturlash tili")
# print(result)  # Salom, qalaysiz?


# msg="Tarjima uchun so\'z kiriting (chiqib ketish uchun (q) deb yozing)>>>"
#
# while True:
#     text=input(msg)
#     if text=='q':
#         break
#     else:
#         translator = GoogleTranslator(source='uz', target='en')
#         result = translator.translate(text)
#         print(result)


# import requests
# from pprint import pprint

#from websockets.legacy.http import read_request

# sahifa="https://kun.uz/news/main"
# r=requests.get(sahifa)
# pprint(r.text)
#

# country = "Uzbekistan"
# url = f"https://restcountries.com/v3.1/name/{country}"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()[0]
#     print("Country Name:", data["name"]["common"])
#     print("Capital:", data["capital"][0])
#     print("Region:", data["region"])
#     print("Population:", data["population"])
# else:
#     print(f"Error {response.status_code}: {response.text}")


# url="https://api.adviceslip.com/advice"
# r=requests.get(url)
# advice=r.json()['slip']['advice']
# print(advice)
#
#
# translator = GoogleTranslator(source='en', target='uz')
# result = translator.translate(advice)
# print(result)  # Salom, qalaysiz?


# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#
# while True:
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y:y+w, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
#
#     cv2.imshow('frame', frame)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from words_list import words
#
# print(fuzz.ratio("salom","assalom"))
# print(fuzz.ratio("salom","salim"))
#
# text='salom'
# matches=process.extract(text, words, limit=3)
# print(matches)

# text='talba'
# match=process.extractOne(text,words)
# print(match)
#

#translator = GoogleTranslator(source='uz', target='en')
# result = translator.translate("Python - dunyodagi eng mashhur dasturlash tili")
# print(result)  # Salom, qalaysiz?

#
# import wx
# from deep_translator import GoogleTranslator
# translator = GoogleTranslator(source='uz', target='en')
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title='o\'zbek-ingliz lug\'ati')
#         panel=wx.Panel()
#         my_sizer=wx.BoxSizer(wx.VERTICAL)
#         self.text_ctrl=wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.All | wx.EXPAND, 5)
#         my_btn=wx.Button(panel,label='TARJIMA')
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn, 0, wx.All | wx.CENTER, 5)
#
#         self.text_out=wx.TextCtrl(panel,style=wx.TE_READONLY)
#         my_sizer.Add(self.text_out, 0, wx.All | wx.EXPAND, 5)
#         self.Show()
#
#     def on_press(self, event):
#         value=self.text_ctrl.GetValue()
#         if not value:
#             self.text_ctrl.SetValue('So\'z kiritmadingiz')
#         else:
#             translator = GoogleTranslator(value,source='uz', target='en')
#             self.text_out.SetValue(translator.text.capitalize())
#
# if __name__=='__main__':
#     app=wx.App()
#     frame=MyFrame()
#     app.MainLoop()
#

#
# import wx
# from deep_translator import GoogleTranslator
#
# translator = GoogleTranslator(source='uz', target='en')
#
#
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title="O'zbek-Ingliz Lug'ati")
#
#         panel = wx.Panel(self)  # Fixed: Added 'self' as the parent
#         my_sizer = wx.BoxSizer(wx.VERTICAL)
#
#         # Input Text Control
#         self.text_ctrl = wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)  # Fixed: Changed 'wx.All' to 'wx.ALL'
#
#         # Translate Button
#         my_btn = wx.Button(panel, label='TARJIMA')
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
#
#         # Output Text Control (Read-only)
#         self.text_out = wx.TextCtrl(panel, style=wx.TE_READONLY)
#         my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)
#
#         panel.SetSizer(my_sizer)  # Important: Set the sizer for the panel
#         self.Show()
#
#     def on_press(self,event):
#         value = self.text_ctrl.GetValue()
#         if not value:
#             self.text_out.SetValue("So'z kiritmadingiz")
#         else:
#             try:
#                 translation = translator.translate(value)  # Fixed: Correct usage of GoogleTranslator
#                 self.text_out.SetValue(translation.capitalize())
#             except Exception as e:
#                 self.text_out.SetValue(f"Xatolik: {e}")
#
#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = MyFrame()
#     app.MainLoop()


import random as r
n=100
numbers=list(range(1,100+1))
x=numbers.pop(r.randint(1,n+1))
print(x)

summa=n*(n+1)/2
print(summa-sum(numbers))














