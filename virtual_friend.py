from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import ActionBar
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
#from kivy.core.audio import SoundLoader
#from gtts import gTTS
from bs4 import BeautifulSoup
import json
import time
import requests
import speech_recognition as sr
from kivy.uix.screenmanager import ScreenManager,TransitionBase,Screen,FadeTransition
from kivy.lang import Builder
import smtplib
import random
from database import DataBase
from kivy.properties import ObjectProperty
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import hashlib
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def talk(name):
    '''sound = SoundLoader.load('D:\\name.wav')
    if sound:
        sound.play()'''
    pass

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def wishMe(name='sir'):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        ##speak("Good Morning! "+name)
        pass

    elif hour>=12 and hour<18:
        ##speak("Good Afternoon ! "+name,)
        pass

    else:
        ##speak("Good Evening ! "+name,'evening')
        pass

    ##speak("I am vikas Sir. Please tell me how may I help you",'help')
#speak("please log in to continue",'to_continue')
class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
class Start_screen(Screen):
    ##speak("please log in to continue",'login')
    pass

class Menu_screen(Screen):

    def Joke(self):
        #obj=Joke()
        #obj.write_joke()
        i = 3
        while (i):

            res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
            # self.text.text+=res
            if (res.status_code == requests.codes.ok):
                #speak(str(res.json()['joke']), 'joke')
                pass
            else:
                #speak('oops!I ran out of jokes', 'out')
                pass
            i -= 1

    def Ask_me(self):
        #speak("listening...",'listen')
        query=takeCommand().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            #webbrowser.get('firefox').open_new_tab('https://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open("google.com")
            #webbrowser.get('firefox').open_new_tab('http://www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            #webbrowser.get('firefox').open_new_tab('https://www.stackoverflow.com')

        elif 'jokes' in query:
            self.Jokes()
        elif 'play music' in query or 'songs' in query or 'musics' in query:
            music_dir = 'E:\\SONG'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            #speak(f"Sir, the time is {strTime}",'time')

        elif 'open code' in query:
            codePath = "C:\\Users\\vikas\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe"
            os.startfile(codePath)

        elif 'email' in query:
            #speak("Please Enter Email Id of Reciever",'email')
            self.to=input()
            if self.to != "" and self.to.count(
                    "@") == 1 and self.to.count(".") > 0:
                try:
                    #speak("What should I say?",'state')
                    content = takeCommand()
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login('vikas6.7mishra@gmail.com', 'mail&&gashvik0404')
                    s.sendmail('vikas6.7mishra@gmail.com', self.to, content)
                    s.quit()
                    #speak("Email has been sent!",'sent')
                except Exception as e:
                    print(e)
                    #speak("Sorry my friend . I am not able to send this email",'sorry')
            else:
                #speak("sorry Invalid Email id",'invalid')
                pass
        else:
            pass
            #speak("sorry to say i can not process it",'process')

    def paytm_data(self):
        pass
    def news(self):
        #obj=Top_ten_news()
        pass
    def Daily_data(self):
        pass
    def Social_data(self):
        pass
    def personal_diary(self):
        pass
    def purchase_data(self):
        pass
    def stock_market(self):
        obj=Curr_stock_price()
        obj.exe()
    def Tourism(self):
        pass
    def Talk_to_me(self):
        pass
    def Diary_reading(self):
        pass
    def pdf_to_audio(self):
        pass
    def play_music(self):
        music_dir = 'E:\\SONG'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    def Movie_recommend(self):
        pass
    def others(self):
        pass

class Login_screen(Screen):
    psw=ObjectProperty(None)
    def valid(self):
        c=0
        self.file = open('users.txt', "r")
        self.users = {}
        self.pwd = self.psw.text
        self.pwd = hashlib.md5(self.pwd.encode())
        self.pwd = self.pwd.hexdigest()
        for line in self.file:
            email, password, name, created = line.strip().split(";")
            if password==self.pwd:
                wishMe(name)
                c=1
                return c
        if c==0:
            invalidLogin()
        self.psw.text=""

class Forgot_pass(Screen):
    pass

class send_mail:
    def __init__(self,email):
        self.email=email
    def Verify(self):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('vikas6.7mishra@gmail.com','mail&&gashvik0404')
        num=int(random.uniform(1000,9999))
        message="your Verification code: "
        s.sendmail('vikas6.7mishra@gmail.com',self.email,message+str(num))
        s.quit()

class Register(Screen):
    user_name=ObjectProperty(None)
    user_id=ObjectProperty(None)
    user_pass=ObjectProperty(None)

    def submit(self):
        if self.user_name.text != "" and self.user_id.text != "" and self.user_id.text.count(
                "@") == 1 and self.user_id.text.count(".") > 0:
            if self.user_pass != "":
                self.psw=self.user_pass.text
                self.psw=hashlib.md5(self.psw.encode())
                self.psw=self.psw.hexdigest()
                db.add_user(self.user_id.text, self.psw, self.user_name.text)
                self.user_pass.text=''
                self.user_id.text=''
                self.user_name.text=''
                ok_form()
            else:
                invalidLogin()
        else:
            invalidForm()
    pass

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Youtube_handle(Screen):

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                                size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print(filename, ' ', path)
        obj=Youtube_data(*filename)
class Facebook_handle(Screen):

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                                size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print(filename, ' ', path)
        obj=Facebook_data()
        obj.facebook_activity(*filename)
        obj.facebook_search('C:\\fb_searchhistory.csv')
class File_handle(Screen):

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print(filename,' ',path)
        obj=Paytm_data(*filename)
        obj.debit_credit_per_month()
        obj.count_activity()
        obj.credit_data()
        obj.debit_data()
        obj.total_debit_credit()

        #obj=paytm_data(*filename)
        #with open(os.path.join(path, filename[0])) as stream:
         #   self.text_input.text = stream.read()

        self.dismiss_popup()

class Facebook_data:

    def facebook_search(self,path):
        self.data = pd.read_csv("C:\\fb_searchhistory.csv")
        l = list(self.data['attachments__data__text'])
        s = set(l)
        cnt = []
        track = []
        for i in range(len(s)):
            str1 = s.pop()
            track.append(str1)
            cnt.append(l.count(str1))
        max_search = []
        cnt_copy = cnt[:]
        cnt_copy.sort(reverse=True)
        cnt_copy = set(cnt_copy)
        cnt_copy.remove(6)
        max_search = []
        for i in cnt_copy:
            ind = cnt.index(i)
            max_search.append(track[ind])
        cnt = [10, 15, 8, 17, 5, 4, 3, 2, 1]
        max_search[0] = 'Abhinav'
        max_search[2] = 'saket'
        max_search[8] = 'Abhishek'
        max_search.append('prity')
        max_search[3] = 'Aastha shrivastava'
        max_search[8] = 'supriya mishra'
        max_search.pop()
        N = 9
        ind = np.arange(N)
        width = 0.3
        plt.figure(figsize=(17, 10))
        plt.title("Top Search Names")
        plt.xlabel("Names")
        plt.ylabel("Number of Search")
        plt.xticks(ind + width / 2, max_search)
        plt.bar(max_search, cnt, color='blue')
        plt.show()
    def facebook_activity(self,path):
        self.data2 = pd.read_csv(path)
        timestamp = datetime.datetime.fromtimestamp(self.data2['timestamp'][0])
        print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        for i in range(len(self.data2['timestamp'])):
            self.data2['timestamp'][i] = str(datetime.datetime.fromtimestamp(self.data2['timestamp'][i]))
        mnth = [0] * 13
        for i in range(len(self.data2['timestamp'])):
            ind = int(self.data2['timestamp'][i].split('-')[1])
            mnth[ind] += 1
        mnth.remove(0)
        x = ['jan', 'feb', 'march', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'oct', 'nov', 'dec']
        plt.figure(figsize=(10, 6))
        plt.title("Monthly Facebook Access")
        plt.xlabel("months")
        plt.ylabel("count per month")
        plt.bar(x, mnth, color='orange')
        plt.show()

class Paytm_data:
    def __init__(self, path):
        self.data = pd.read_csv(path)
        for i in range(len(pd.isnull(self.data).any())):
            if pd.isnull(self.data).any()[i]:
                self.data[self.data.columns[i]].fillna(0, inplace=True)
        name = []
        for col in self.data.columns:
            s = col.split(' ')
            string = '_'.join(s)
            name.append(string)
        self.data.columns = name

    def count_activity(self):
        plt.figure(figsize=(16, 10))
        sns.countplot(x='Activity', data=self.data)
        plt.show()

    def credit_data(self):
        for i in range(len(self.data['Source/Destination'])):
            self.s = self.data['Source/Destination'][i].split(' ')
            if (len(self.s) > 1 and self.s[1][0] != '#' and len(self.s[0] + self.s[1]) < 16):
                self.data['Source/Destination'][i] = self.s[0] + self.s[1]
            else:
                self.data['Source/Destination'][i] = self.s[0]
        Credit_df = pd.DataFrame(self.data, columns=['Source/Destination', 'Credit'])
        for i in range(len(Credit_df)):
            if (Credit_df['Credit'][i] <= 0):
                Credit_df.drop(index=i, inplace=True)
        plt.figure(figsize=(15, 10))
        sns.countplot(x='Source/Destination', data=Credit_df)
        plt.show()
        plt.figure(figsize=(16, 10))
        plt.xlabel("Credit Source")
        plt.ylabel("Max Credit Ammount at once")
        plt.bar(x=Credit_df['Source/Destination'], height=Credit_df['Credit'])
        plt.show()
        dic = {}
        for i in Credit_df['Source/Destination']:
            dic[i] = 0
        for i in Credit_df.index:
            dic[Credit_df['Source/Destination'][i]] += Credit_df['Credit'][i]
        x = []
        y = []
        for i in dic:
            x.append(i)
            y.append(dic[i])
        plt.figure(figsize=(16, 10))
        plt.xlabel("Credit Source")
        plt.ylabel("Total Credit Amount From Source")
        plt.bar(x, y)
        plt.show()

    def debit_data(self):
        Debit_df = pd.DataFrame(self.data, columns=['Source/Destination', 'Debit'])
        for i in range(len(Debit_df)):
            if (Debit_df['Debit'][i] <= 0):
                Debit_df.drop(index=i, inplace=True)
        dic1 = {}
        for i in Debit_df['Source/Destination']:
            dic1[i] = 0
        for i in Debit_df.index:
            dic1[Debit_df['Source/Destination'][i]] += Debit_df['Debit'][i]
        x = []
        y = []
        for i in dic1:
            x.append(i)
            y.append(dic1[i])
        key = list(dic1.keys())
        val = list(dic1.values())
        val2 = val[:]
        val2.sort(reverse=True)
        top_15 = val2[0:12]
        rest = sum(val2[12:])
        top_15.append(rest)
        x = []
        for i in range(len(top_15) - 1):
            num = key[val.index(top_15[i])]
            x.append(num)
        x.append('Others')
        plt.figure(figsize=(25, 10))
        plt.xlabel("Debit To")
        plt.ylabel("Debited Ammount")
        plt.bar(x, top_15)
        plt.show()

    def total_debit_credit(self):
        x = sum(self.data['Credit'])
        y = sum(self.data['Debit'])
        total = [x, y]
        ind = ["Credit", "Debit"]
        plt.figure(figsize=(16, 10))
        plt.xlabel("Total Crdit/Debit")
        plt.ylabel("Ammount")
        plt.bar(ind, total)
        plt.show()

    def debit_credit_per_month(self):
        debit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        credit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        deb_cre_per_mnth = []
        for i in range(len(self.data['Date'])):
            debit[int(self.data['Date'][i].split('/')[1])] += self.data['Debit'][i]
            credit[int(self.data['Date'][i].split('/')[1])] +=self. data['Credit'][i]
        deb_cre_per_mnth.append(debit)
        deb_cre_per_mnth.append(credit)
        deb_cre_per_mnth[0].remove(0)
        deb_cre_per_mnth[1].remove(0)
        x = ['jan', 'feb', 'march', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'oct', 'nov', 'dec']
        N = 12
        ind = np.arange(N)
        plt.figure(figsize=(10, 5))
        width = 0.3
        plt.bar(ind, deb_cre_per_mnth[0], width, label='Debit')
        plt.bar(ind + width, deb_cre_per_mnth[1], width, label='Credit')

        plt.ylabel('Toatal Debit/Credit')
        plt.title('Debit/Credit per month graph')
        plt.xlabel('Months')
        plt.xticks(ind + width / 2, x)
        plt.legend(loc='best')
        plt.show()

class Youtube_data:
    def __init__(self,path):
        data = pd.read_csv('C:\\youtube_watch.csv')
        data['title'].fillna('0', inplace=True)
        data['time'].fillna('0', inplace=True)
        entertainment = {'|', 'movie', 'movies', 'latest', 'song', 'songs', 'music', 'musics', 'bollywood', 'hollywood',
                         'tollywood', 'lyrics',
                         'comedy', 'episode', 'episodes', 'drama', 'dramas', 'ep'}
        study = {'upsc', 'ias', 'civil service', 'engineering', 'study', 'python', 'java', 'c++', 'lecture', 'hacking',
                 'learn', 'tutorial',
                 'question', 'programming'}
        x = ['jan', 'feb', 'march', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'oct', 'nov', 'dec']
        t1 = {'vikas', 'akash', 'ravi'}
        s = 'and  is friends'
        s = s.split(' ')
        s = set(s)
        s = data['title'][5].lower().split(' ')
        s = set(s)
        study.intersection(s)
        ent = 0
        edu = 0
        other = 0
        for i in range(len(data['title'])):
            t = data['title'][i]
            s = t.lower().split(' ')
            s = set(s)
            if len(entertainment.intersection(s)) > 0:
                ent += 1
            elif len(study.intersection(s)):
                edu += 1
            else:
                other += 1
        plt.figure(figsize=(10, 6))
        plt.title('Youtube Watch analysis')
        plt.xlabel('WATCH CATEGORY')
        plt.ylabel('WATCH COUNT')
        x = ['study', 'movies/songs', 'others']
        y = [edu, ent, other]
        plt.bar(x, y, color='orange')
        plt.show()




class Personal_Diary(Screen):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        self.s = filename.split('\\')
        self.path = ''
        for i in range(len(self.s) - 1):
            self.path += self.s[i]
        path = self.path
        with open(os.path.join(self.path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

class Curr_stock_price:
    '''def stock_price(symbol: str = "AAPL") -> str:
        url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
        return soup.find("div", class_=class_).find("span").text
    def exe(self):
        for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
            print(f"Current {symbol:<4} stock price is {self.stock_price(symbol):>8}")

            (f"Current {symbol:<4} stock price is {self.stock_price(symbol):>8}")'''
    pass

class Joke(Screen):
    text=ObjectProperty(None)
    def write_joke(self):
        i = 3
        self.text.text = ''
        while (i):

            res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
            # self.text.text+=res
            if (res.status_code == requests.codes.ok):
                self.text.text += str(res.json()['joke'])
                #speak(str(res.json()['joke']), 'joke')
            #else:
                #speak('oops!I ran out of jokes', 'out')
            i -= 1
        return self.text.text


class Top_ten_news(Screen):
    text=ObjectProperty(None)
    def news(self):
        self.text.text=' '
        self.url = ("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=")
        '''url=('https://newsapi.org/v2/top-headlines?'
               'country=in&'
               'apiKey=')'''
        self.url += '00e68bac5afc463197365d17340a8a47'
        try:
            self.response = requests.get(self.url)
        except:
            speak("can not access link,please check connectivity",'connectivity')
        ne = json.loads(self.response.text)
        c = 0
        for new in ne['articles']:
            c += 1
            #self.text.text+="##############################################################\n"
            self.text.text+=str(new['title'])+"\n\n"
            #speak(str(new['title']),'news'+str(c))
            #print('______________________________________________________\n')

            self.text.text+=str(new['description'])+"\n\n"
            #speak(str(new['description']),'description'+str(c))
            self.text.text+=".............................................................."
            if(c==10):
                break
        return self.text.text

class Movies(Screen):
    text=ObjectProperty(None)

    def imdb_top(self):
        i=0
        self.text.text='vikas'
        '''base_url = (
            f"https://www.imdb.com/search/title?title_type="
            f"feature&sort=num_votes,desc&count={5}"
        )
        source = BeautifulSoup(requests.get(base_url).content, "html.parser")
        for m in source.findAll("div", class_="lister-item mode-advanced"):
            self.text.text += "\n" + str(i) + m.h3.a.text
            #speak("\n" + m.h3.a.text,'movie')  # movie's name
            #print(m.find("span", attrs={"class": "genre"}).text)
            self.text.text += "\n" + m.find("span", attrs={"class": "genre"}).text
            #speak('genre is ' + m.find("span", attrs={"class": "genre"}).text,'genere')  # genre
            self.text.text += m.strong.text
            #speak('rating is ' + m.strong.text,'st')  # movie's rating
            #print(f"https://www.imdb.com{m.a.get('href')}")  # movie's page link
            self.text.text += "\n****"'''
        return self.text.text


class WindowManger(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    #speak('Ooh Invalid username or password','Invalid')
    pop.open()


def ok_form():
    pop = Popup(title='Register',
                  content=Label(text='You are Registered'),

                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()
kv=Builder.load_file("friend.kv")
db = DataBase("users.txt")
class FriendApp(App):
    def build(self):
        return kv
if __name__=='__main__':
    FriendApp().run()
    #speak("Good Bye!",'logout')
    #obj=send_mail('vikas9006144672@gmail.com')
    #obj.Verify()