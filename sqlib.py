
from re import X
import mysql.connector
import json

from mysql.connector import cursor

def sql_koneksi(): 
    db =  mysql.connector.connect(host="localhost",user="root",password="",database="db_monitor")
    return db

def input_data(t,h,c,r,s):
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("INSERT INTO `tb_data`(`Suhu`, `Kelembapan_udara`, `Intensitas_cahaya`, `Curah_hujan`, `Kelembapan_tanah`,`Time`) VALUES (%s,%s,%s,%s,%s,now())", (t,h,c,r,s))
    db.commit()

def input_dataa(a,b,d,e,f):
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("INSERT INTO `tb_data2`(`Suhu`, `Kelembapan_udara`, `Intensitas_cahaya`, `Curah_hujan`, `Kelembapan_tanah`,`Time`) VALUES (%s,%s,%s,%s,%s,now())", (a,b,d,e,f))
    db.commit()

def show_data() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`, `Suhu`, `Kelembapan_udara` , `Intensitas_cahaya`, `Curah_hujan`, `Kelembapan_tanah` FROM `tb_data` ")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)  
    dataJson = json.dumps(datas)  #data yang diambil dari sql ke json objek
    return dataJson  #data yang diambil dari sql ke json objek

def node1_suhu() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Suhu` FROM `tb_data` ORDER by Id DESC LIMIT 5 ")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node1_kelembapanudara() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Kelembapan_udara` FROM `tb_data` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node1_kelembapantanah() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Kelembapan_tanah` FROM `tb_data` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node1_keltanah_konversi():
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT `Kelembapan_tanah` FROM `tb_data`")
    c = cursor.fetchall()
    data = None
    hasil = float(c[-1][0])
    if hasil>4.8 :
        data = "Kering"
    else :
        if hasil<4.8 and hasil>3.5:
         data = "Normal"
        else :
            data = "Basah"
    return data

def node1_intensitascahaya() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Intensitas_cahaya` FROM `tb_data` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node1_curahhujan() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Curah_hujan` FROM `tb_data` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node1_curahhujan_konversi():
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT `Curah_hujan` FROM `tb_data`")
    c = cursor.fetchall()
    data = None
    hasil = int(c[-1][0])
    if hasil>500 :
        data = "Tidak Hujan"
    else:
        data = "Hujan"
    return data
    
def show_dataa() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`, `Suhu`, `Kelembapan_udara` , `Intensitas_cahaya`, `Curah_hujan`, `Kelembapan_tanah` FROM `tb_data2`")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    dataJson = json.dumps(datas)  #data yang diambil dari sql ke json objek
    return dataJson  #data yang diambil dari sql ke json objek

def node2_suhu() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Suhu` FROM `tb_data2` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node2_kelembapanudara() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Kelembapan_udara` FROM `tb_data2` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node2_kelembapantanah() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Kelembapan_tanah` FROM `tb_data2` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node2_keltanah_konversi():
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT `Kelembapan_tanah` FROM `tb_data2`")
    c = cursor.fetchall()
    data = None
    hasil = float(c[-1][0])
    if hasil>4.8 :
        data = "Kering"
    else :
        if hasil<4.8 and hasil>3.5:
         data = "Normal"
        else :
            data = "Basah"
    return data

def node2_intensitascahaya() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Intensitas_cahaya` FROM `tb_data2` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node2_curahhujan() :
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute ("SELECT `Time`,`Curah_hujan` FROM `tb_data2` ORDER by Id DESC LIMIT 5")
    rows = [x for x in cursor]  #data yang diambil dari sql ke json objek
    cols = [x[0] for x in cursor.description]  #data yang diambil dari sql ke json objek
    datas = []  #data yang diambil dari sql ke json objek
    for row in rows:  #data yang diambil dari sql ke json objek
        data = {}  #data yang diambil dari sql ke json objek
        for prop, val in zip(cols, row):  #data yang diambil dari sql ke json objek
            data[prop] = val  #data yang diambil dari sql ke json objek
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['Time'] = str(datas[i]['Time'])

    dataJson = json.dumps(datas)  
    return dataJson  #data yang diambil dari sql ke json objek

def node2_curahhujan_konversi():
    db = sql_koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT `Curah_hujan` FROM `tb_data2`")
    c = cursor.fetchall()
    data = None
    hasil = int(c[-1][0])
    if hasil>500 :
        data = "Tidak Hujan"
    else:
        data = "Hujan"
    return data
    
def input_user(Username,Password,IP_Adress):
    db = sql_koneksi()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO `tb_user`(`Username`, `Password`, `IP_Address`) VALUES (%s,%s,%s)",(Username,Password,IP_Adress))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

def cek_data_user(Username,Password):
    db = sql_koneksi()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `Username`, `Password` FROM `tb_user` WHERE `Username`=%s AND `Password`=%s",(Username,Password))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        return True

def update_ip(IP_Address,Username,Password):
    db = sql_koneksi()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE `tb_user` SET `IP_Address`=%s WHERE `Username`=%s AND `Password`= %s",(IP_Address,Username,Password))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

def cek_username(Username):
    db = sql_koneksi()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `Username` FROM `tb_user` WHERE `Username`=%s",(Username,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c==None:
        return True
    else:
        return False
