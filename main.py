import tkinter as tk
from tkinter import ttk
from datetime import *
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8})

dateIsNow = datetime.date(datetime.today())

dateWeek = []

temp = dateIsNow.strftime('%d.%m.%Y')
temp2 = dateIsNow - timedelta(days = 6)
dateWeek.append(temp2.strftime('%d.%m.%Y') + " - " + dateIsNow.strftime('%d.%m.%Y'))
for i in range(3):
    temp = temp2
    temp2 = temp2 - timedelta(days = 6)
    dateWeek.append(temp2.strftime('%d.%m.%Y') + " - " + temp.strftime('%d.%m.%Y'))

dateMonth = []

temp = dateIsNow.strftime('%b %Y')
temp2 = dateIsNow
dateMonth.append(temp)

for i in range(3):
    temp2 = temp2 - timedelta(weeks= 4)
    dateMonth.append(temp2.strftime('%b %Y'))

dateQuarter = []

temp = dateIsNow.strftime('%d.%m.%Y')
temp2 = dateIsNow - timedelta(weeks = 11)
dateQuarter.append(temp2.strftime('%d.%m.%Y') + " - " + dateIsNow.strftime('%d.%m.%Y'))
for i in range(3):
    temp = temp2
    temp2 = temp2 - timedelta(weeks = 11)
    dateQuarter.append(temp2.strftime('%d.%m.%Y') + " - " + temp.strftime('%d.%m.%Y'))

dateYear = []

temp = dateIsNow.strftime('%Y')
temp2 = dateIsNow
dateYear.append(temp)

for i in range(3):
    temp2 = temp2 - timedelta(weeks = 52)
    dateYear.append(temp2.strftime('%Y'))


def clicked():
    name = txt.get()
    txt.delete(0, 'end')
    nameKey1 = combo1.get() 
    nameKey2 = combo2.get()
    i = 0
    for i in range(len(key)):
        if(nameKey1 == key[i]):
            break
    j = 0
    for j in range(len(key)):
        if(nameKey2 == key[j]):
            break
    answer = float(name) * value[i]
    answer = answer / value[j] 

    label.config(text = answer)

def graph():
    val = date.get()
    dateOfDay = []
    data = []
    if(val == 1):#Неделя
        nameDate = combo4.get()
        tempDate = nameDate.split()
        secondDate = tempDate[0].split('.')
        secondDate = datetime(int(secondDate[2]),int(secondDate[1]) ,int(secondDate[0]))
        for i in range(7):
            temp = secondDate.strftime('%d.%m.%Y')
            temp = temp.split(".")
            dateOfDay.append(temp[0])
            url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={temp[0]}/{temp[1]}/{temp[2]}"
            data.append(database(url)) 
            secondDate = secondDate + timedelta(days = 1)
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master = tab2)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        plt.plot(dateOfDay, data)
    elif(val == 2):# Месяц
        nameDate = combo4.get()
        nameOfMonth = nameDate.split()
        numberOfMonth = countMonth(nameOfMonth[0])
        firstDate = datetime(year = int(nameOfMonth[1]),month = numberOfMonth ,day = 1)
        temp = firstDate.strftime('%d.%m')
        temp = temp.split(".")
        temp2 = firstDate.strftime('%d.%m.%Y')
        temp2 = temp2.split(".")
        i = 1
        if(nameOfMonth[0] != dateIsNow.strftime('%b')):
            while(temp[1] == firstDate.strftime('%m')):
                dateOfDay.append(i)
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={temp2[0]}/{temp2[1]}/{temp2[2]}"
                data.append(database(url)) 
                firstDate = firstDate + timedelta(days = 1)
                temp2 = firstDate.strftime('%d.%m.%Y')
                temp2 = temp2.split(".")
                i += 1
        else:
            while(i != int(dateIsNow.strftime('%d'))):
                dateOfDay.append(i)
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={temp2[0]}/{temp2[1]}/{temp2[2]}"
                data.append(database(url)) 
                firstDate = firstDate + timedelta(days = 1)
                temp2 = firstDate.strftime('%d.%m.%Y')
                temp2 = temp2.split(".")
                i += 1
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master = tab2)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        plt.plot(dateOfDay, data)
    elif(val == 3):# Квартал
        nameDate = combo4.get()
        tempDate = nameDate.split()
        secondDate = tempDate[0].split('.')
        secondDate = datetime(int(secondDate[2]),int(secondDate[1]) ,int(secondDate[0]))
        for i in range(12):
            temp = secondDate.strftime('%d.%m.%Y')
            temp = temp.split(".")
            dateOfDay.append(secondDate.strftime('%d.%m'))
            url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={temp[0]}/{temp[1]}/{temp[2]}"
            data.append(database(url)) 
            secondDate = secondDate + timedelta(weeks = 1)
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master = tab2)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        plt.plot(dateOfDay, data)
    elif(val == 4):# Год
        nameDate = combo4.get()
        size = int(nameDate) - int(dateIsNow.strftime('%Y'))
        if(size == 0):
            m2 = int(dateIsNow.strftime('%m'))
        else:
            m2 = 12
        for i in range(m2):
            dateOfDay.append(countMonth(i+1))
            if(i < 9):
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/0{i+1}/{nameDate}"
            else:
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{i+1}/{nameDate}"
            data.append(database(url)) 
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master = tab2)
        plot_widget = canvas.get_tk_widget()
        fig.clear()  
        plt.plot(dateOfDay, data)
    plt.grid()
    plot_widget.grid(row = 10, column = 10)
    
def countMonth(nameOfMonth):
    if(nameOfMonth == "Jan"):
        return 1
    if(nameOfMonth == "Feb"):
        return 2
    if(nameOfMonth == "Mar"):
        return 3
    if(nameOfMonth == "Apr"):
        return 4
    if(nameOfMonth == "May"):
        return 5
    if(nameOfMonth == "Jun"):
        return 6
    if(nameOfMonth == "Jul"):
        return 7
    if(nameOfMonth == "Aug"):
        return 8
    if(nameOfMonth == "Sep"):
        return 9
    if(nameOfMonth == "Oct"):
        return 10
    if(nameOfMonth == "Nov"):
        return 11   
    if(nameOfMonth == "Dec"):
        return 12
    if(nameOfMonth == 1):
        return "Jan"
    if(nameOfMonth == 2):
        return "Feb"
    if(nameOfMonth == 3):
        return "Mar"
    if(nameOfMonth == 4):
        return "Apr"
    if(nameOfMonth == 5):
        return "May"
    if(nameOfMonth == 6):
        return "Jun"
    if(nameOfMonth == 7):
        return "Jul"
    if(nameOfMonth == 8):
        return "Aug"
    if(nameOfMonth == 9):
        return "Sep"
    if(nameOfMonth == 10):
        return "Oct"
    if(nameOfMonth == 11):
        return "Nov" 
    if(nameOfMonth == 12):
        return "Dec"

def combobox():
    val = date.get()
    if(val == 1):
        combo4.config(values = dateWeek)
        combo4.current(0)
    elif(val == 2):
        combo4.config(values = dateMonth)
        combo4.current(0)
    elif(val == 3):
            combo4.config(values = dateQuarter)
            combo4.current(0)
    elif(val == 4):
        combo4.config(values = dateYear)
        combo4.current(0)
    combo4.grid(column=2, row = val)


import urllib.request
import xml.dom.minidom

# отправляем запрос на сайт и получаем ответ в формате xml
url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={dateIsNow.strftime('%d/%m/%Y')}"
response = urllib.request.urlopen(url)
xml_string = response.read().decode('windows-1251')

# создаем объект DOM из xml строки
dom = xml.dom.minidom.parseString(xml_string)

# создаем словарь для хранения данных
data = {}

# проходим по каждому элементу Valute и добавляем данные в словарь
for valute in dom.getElementsByTagName('Valute'):
    name = valute.getElementsByTagName('Name')[0].childNodes[0].nodeValue
    value = valute.getElementsByTagName('Value')[0].childNodes[0].nodeValue.replace(',', '.')
    nominal = valute.getElementsByTagName('Nominal')[0].childNodes[0].nodeValue
    data[name] = float(value) / int(nominal) 


key = []
for keys in data.keys():
    key.append(keys)
key.append("Российский Рубль")

value = []
for values in data.values():
    value.append(values)
value.append(1)

def database(url):
    response = urllib.request.urlopen(url)
    xml_string = response.read().decode('windows-1251')

    # создаем объект DOM из xml строки
    dom = xml.dom.minidom.parseString(xml_string)

    # создаем словарь для хранения данных
    data = {}

    # проходим по каждому элементу Valute и добавляем данные в словарь
    for valute in dom.getElementsByTagName('Valute'):
        name = valute.getElementsByTagName('Name')[0].childNodes[0].nodeValue
        value = valute.getElementsByTagName('Value')[0].childNodes[0].nodeValue.replace(',', '.')
        nominal = valute.getElementsByTagName('Nominal')[0].childNodes[0].nodeValue
        data[name] = float(value) / int(nominal)


    key = []
    for keys in data.keys():
        key.append(keys)

    value = []
    for values in data.values():
        value.append(values)

    nameKey3 = combo3.get()
    i = 0
    for i in range(len(key)):
        if(nameKey3 == key[i]):
            break
    return value[i]

win = tk.Tk()
win.title("S-I-T-B")
win.geometry("1500x800")

tab_control = ttk.Notebook(win)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text ="Калькулятор валют")
tab_control.add(tab2, text ="Динамика курса")

#Первое окно

tab1.grid_columnconfigure(0, minsize = 200)
tab1.grid_columnconfigure(1, minsize = 150)
tab1.grid_rowconfigure(0, minsize = 100)

combo1 = ttk.Combobox(tab1, values = key)
combo1.current(0)
combo1.grid(column=0, row = 0)

combo2 = ttk.Combobox(tab1, values = key)
combo2.current(0)
combo2.grid(row = 3, column= 0)

label = tk.Label(tab1,text = "")
label.grid(row = 3, column= 1)

txt = tk.Entry(tab1)
btn = tk.Button(tab1, text = "Конвертировать", command = clicked)
txt.grid(column=1, row = 0)
btn.grid(column=2, row = 0)

#Второе окно

tab2.grid_columnconfigure(0, minsize = 200)
tab2.grid_columnconfigure(1, minsize = 200)

label2 = tk.Label(tab2,text = "Валюта")
label2.grid(row = 0, column= 0)
label3 = tk.Label(tab2,text = "Период")
label3.grid(row = 0, column= 1)
label4 = tk.Label(tab2,text = "Выбор периода")
label4.grid(row = 0, column= 2)

combo3 = ttk.Combobox(tab2, values = key)
combo3.current(0)
combo3.grid(column=0, row = 1)

combo4 = ttk.Combobox(tab2)

btn2 = tk.Button(tab2, text = "Построить график", command = graph)
btn2.grid(column=0, row = 4)

date = tk.IntVar()

tk.Radiobutton(tab2,text='Неделя', variable=date, value=1, command=combobox).grid(column=1,row = 1)
tk.Radiobutton(tab2,text='Месяц', variable=date, value=2, command=combobox).grid(column=1,row = 2)
tk.Radiobutton(tab2,text='Квартал', variable=date, value=3, command=combobox).grid(column=1,row = 3)
tk.Radiobutton(tab2,text='Год', variable=date, value=4, command=combobox).grid(column=1,row = 4)


#Запуск программы
tab_control.pack(expand = 1, fill = 'both')
win.mainloop()
