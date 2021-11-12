from tkinter import font
import requests
import bs4
import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data=""

    for i in info_div:
        text = i.find("h1", class_=None).get_text()
        count = i.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"
    return all_data


def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data=""
    
    j=0

    for i in info_div:
        if j<=2:
            text = i.find("h1", class_=None).get_text()
            count = i.find("span", class_=None).get_text()
            all_data = all_data + text + " " + count + "\n"
        j=j+1
    mainlabel['text']=all_data
 
def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data



get_covid_data()

root = tk.Tk()
root.geometry("900x700")
root.title("Covid-19 Tracker")
f = ("poppins", 25, "bold")

country =tk.Label(root,text="Enter country name",font=f)
country.pack() 

textfield = tk.Entry(root, width = 50)
textfield.pack()



mainlabel = tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()

gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()

root.mainloop()