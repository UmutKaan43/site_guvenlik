from flask import Flask,request,render_template
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    yeni = request.args.get("giris")
    if yeni=="AxTe43TT12Ex":
        c = sqlite3.connect("QaRrrs12b.db")
        x = c.cursor()
        x.execute("SELECT * FROM giris")
        veri = x.fetchall()
        c.commit()
        c.close()
        return render_template("index.html",veriler = veri)
    else:
        return render_template("index.html")


@app.route("/reg",methods=["GET","POST"])
def reg():
    if request.method=="POST":
        ip = str(request.form.get("ip"))
        ulke = str(request.form.get("ulke"))
        region = str(request.form.get("region"))
        city = str(request.form.get("city"))
        saat = str(request.form.get("saat"))
        print("yyazi",ip,ulke,region,city)
        c = sqlite3.connect("QaRrrs12b.db")
        x = c.cursor()
        x.execute("INSERT INTO giris (ip, ulke, region, city, saat) VALUES ('"+ip+"','"+ulke+"','"+region+"','"+city+"','"+saat+"')")
        c.commit()
        c.close()
        return "True"     
    else:
        return "Siteye Get işlemi yaptınız"
        # veri tabanını yazsın

if __name__=="__main__":
    #c = sqlite3.connect("QaRrrs12b.db")
    #x = c.cursor()
    #x.execute("Create Table giris (ip TEXT, ulke TEXT, region TEXT, city TEXT, saat TEXT)")
    #c.commit()
    #c.close()    
    app.run(debug=True)