import flask
from flask import Flask,request,jsonify
import json
from sqlib import cek_data_user, input_data,input_dataa, show_data, node1_suhu, node1_kelembapanudara, node1_kelembapantanah, node1_keltanah_konversi, node1_intensitascahaya, node1_curahhujan, node1_curahhujan_konversi, node2_suhu, node2_kelembapanudara, node2_kelembapantanah, node2_keltanah_konversi, node2_curahhujan, node2_curahhujan_konversi ,node2_intensitascahaya, show_dataa,input_user,cek_username,update_ip

app = Flask(__name__)

@app.route('/monitor/node1', methods=['POST'])
def node1():
    json_data = flask.request.json
    if json_data ==None:
        result = {"pesan":"data not found"}
        resp = jsonify(result)
        return resp,404
    else :
        if 'Suhu' not in json_data or 'Kelembapan_udara' not in json_data or 'Intensitas_cahaya' not in json_data or 'Curah_hujan' not in json_data or 'Kelembapan_tanah' not in json_data :
            result = {"pesan": "bad request"}
            resp = jsonify(result)
            return resp,403
        else :
            Suhu = json_data ['Suhu']
            Kelembapan_udara = json_data ['Kelembapan_udara']
            Intensitas_cahaya = json_data ['Intensitas_cahaya']
            Curah_hujan = json_data ['Curah_hujan']
            Kelembapan_tanah = json_data ['Kelembapan_tanah']
            input_data(Suhu,Kelembapan_udara,Intensitas_cahaya,Curah_hujan,Kelembapan_tanah) 
            result = {"pesan" : " input berhasil"}
            resp= jsonify(result)
            return resp, 200

@app.route('/monitor/node2', methods=['POST'])
def node2():
    json_data = flask.request.json
    if json_data ==None:
        result = {"pesan":"data not found"}
        resp = jsonify(result)
        return resp,404
    else :
        if 'Suhu' not in json_data or 'Kelembapan_udara' not in json_data or 'Intensitas_cahaya' not in json_data or 'Curah_hujan' not in json_data or 'Kelembapan_tanah' not in json_data :
            result = {"pesan": "bad request"}
            resp = jsonify(result)
            return resp,403
        else :
            Suhu = json_data ['Suhu']
            Kelembapan_udara = json_data ['Kelembapan_udara']
            Intensitas_cahaya = json_data ['Intensitas_cahaya']
            Curah_hujan = json_data ['Curah_hujan']
            Kelembapan_tanah = json_data ['Kelembapan_tanah']
            input_dataa (Suhu,Kelembapan_udara,Intensitas_cahaya,Curah_hujan,Kelembapan_tanah) 
            result = {"pesan" : " input berhasil"}
            resp= jsonify(result)
            return resp, 200
        
@app.route('/monitor/node1', methods=['GET'])
def monitor_node1() :
    resp = show_data()
    return resp,200

@app.route('/monitor/suhu', methods=['GET'])
def monitor_suhu() :
    resp = node1_suhu()
    return resp,200

@app.route('/monitor/udara', methods=['GET'])
def monitor_udara() :
    resp = node1_kelembapanudara()
    return resp,200

@app.route('/monitor/tanah', methods=['GET'])
def monitor_tanah() :
    resp = node1_kelembapantanah()
    return resp,200

@app.route('/monitor/tanahkonversi', methods=['GET'])
def monitor_tanahkonversi() :
    resp = node1_keltanah_konversi()
    return resp,200

@app.route('/monitor/cahaya', methods=['GET'])
def monitor_cahaya() :
    resp = node1_intensitascahaya()
    return resp,200

@app.route('/monitor/hujan', methods=['GET'])
def monitor_hujan() :
    resp = node1_curahhujan()
    return resp,200

@app.route('/monitor/hujankonversi', methods=['GET'])
def monitor_hujankonversi() :
    resp = node1_curahhujan_konversi()
    return resp,200

@app.route('/monitor/node2', methods=['GET'])
def monitor_node2() :
    resp = show_dataa()
    return resp,200

@app.route('/monitor/suhu2', methods=['GET'])
def monitor_suhu2() :
    resp = node2_suhu()
    return resp,200

@app.route('/monitor/udara2', methods=['GET'])
def monitor_udara2() :
    resp = node2_kelembapanudara()
    return resp,200

@app.route('/monitor/tanah2', methods=['GET'])
def monitor_tanah2() :
    resp = node2_kelembapantanah()
    return resp,200

@app.route('/monitor/tanahkonversi2', methods=['GET'])
def monitor_tanahkonversi2() :
    resp = node2_keltanah_konversi()
    return resp,200

@app.route('/monitor/cahaya2', methods=['GET'])
def monitor_cahaya2() :
    resp = node2_intensitascahaya()
    return resp,200

@app.route('/monitor/hujan2', methods=['GET'])
def monitor_hujan2() :
    resp = node2_curahhujan()
    return resp,200

@app.route('/monitor/hujankonversi2', methods=['GET'])
def monitor_hujankonversi2() :
    resp = node2_curahhujan_konversi()
    return resp,200
    
@app.route('/monitor/register/user',methods=['POST'])
def user_register():
    json_data = request.json
    if json_data==None:
        result = {"pesan":"data not found"}
        resp = jsonify(result)
        return resp,404
    else:
        if 'Username' not in json_data or 'Password' not in json_data or 'IP_Address' not in json_data:
            result = {"pesan": "bad request"}
            resp = jsonify(result)
            return resp,403
        else:
            Username = json_data['Username']
            Password = json_data['Password']
            IP_Address = json_data['IP_Address']
            cek = cek_username(Username)
            if cek == False:
                result = {"pesan" : " User Already Existed"}
                resp= jsonify(result)
                return resp, 208
            else:
                input_user(Username,Password,IP_Address)
                result = {"pesan" : " input berhasil"}
                resp= jsonify(result)
                return resp, 200

@app.route('/monitor/login/user',methods=['POST'])
def user_login():
    json_data = request.json
    if json_data==None:
        result = {"pesan":"data not found"}
        resp = jsonify(result)
        return resp,404
    else:
        if 'Username' not in json_data or 'Password' not in json_data or 'IP_Address' not in json_data:
            result = {"pesan": "bad request"}
            resp = jsonify(result)
            return resp,403
        else:
            Username = json_data['Username']
            Password = json_data['Password']
            IP_Address = json_data['IP_Address']
            cek = cek_data_user(Username,Password)
            if cek==False:
                result = {"pesan": "Forbidden"}
                resp = jsonify(result)
                return resp,203
            else:
                update_ip(IP_Address,Username,Password)
                result = {"pesan" : " Selamat Datang "+Username}
                resp= jsonify(result)
                return resp, 200
                
if __name__ == "__main__" :
    #serve(app, host="0.0.0.0", port=4001)
    app.run(port=4001, debug=True)
