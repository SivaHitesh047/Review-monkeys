from flask import Flask,render_template,request,url_for,redirect
from flaskext.mysql import MySQL


mysql = MySQL() 
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'formdb'
mysql.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/showRegister')
def register():
    return render_template('register.html')

@app.route('/showLogin')
def login():
    return render_template('login.html')

@app.route('/showLoginx',methods=['POST','GET'])
def validate():
    details = request.form
    uname = details['uname']
    pword = details['pword']
    
    print("",uname,pword)
    sql = '''select uname,pword FROM register'''
    
    con = mysql.connect()
    cur = con.cursor()

    cur.execute(sql)
   
    records = cur.fetchall()
    #count = cur.rowcount

    for row in records:
        
        unamex = row[0]
        pwordx = row[1]
            
        print("",unamex,pwordx)

        if uname==unamex and pword==pwordx:
            print("",unamex,pwordx)
            return render_template("post.html")

    return render_template("login.html")

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    #form = SignUpform()

    #if form.validate_on_submit():
    details = request.form
    uname = details['uname']
    email = details['email']
    pword = details['pword']

    print("",uname,email,pword)
    con = mysql.connect()
    cur = con.cursor()
    sql = """INSERT INTO register(uname,email,pword)VALUES(%s,%s,%s)"""

    try:
        cur.execute(sql,(uname,email,pword))
        con.commit()

    except:
        con.rollback()

    finally:
        cur.close()
        con.close()
    
    return render_template("success.html")

#return render_template("register.html",form=form)

@app.route('/showCreate')
def create():
    return render_template("create.html") 

@app.route('/showRestaurant')
def contact():
    con = mysql.connect()
    cur = con.cursor()
    otype = "Restaurant"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)

    return render_template("restaurant.html",orgnames=orgnames)

@app.route('/showHospital')
def showhospital():
    con = mysql.connect()
    cur = con.cursor()
    otype = "Hospital"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)

    return render_template("hospital.html",orgnames=orgnames)

@app.route('/revHospitalshow')
def showrevhospital():
    con = mysql.connect()
    cur = con.cursor()
    otype = "Hospital"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)

    return render_template("revhospital.html",orgnames=orgnames)

@app.route('/revHospital',methods=['POST','GET'])
def revhospital():
   
    details = request.form
    hname = details['hname']
    dname = details['dname']
    print(hname,dname)
    con = mysql.connect()
    cur = con.cursor()
    
    otype = "Hospital"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)

    if hname == 'none':
        return render_template("revhospital.html",orgnames=orgnames)
    else:
        if dname == 'none':
            sql = """ select name,age,dis,rate,most,cmnts from hospital where hname = %s """
            cur.execute(sql,(hname,))
            
            
        else:
            sql = """ select name,age,dis,rate,most,cmnts from hospital where hname = %s && dname = %s"""
            cur.execute(sql,(hname,dname))
            
        data = cur.fetchall()
        size = len(data)
        #print("The size of the .....:",size)
        cols = 6
        datalist = ["Name:","Age:","Opinion about treatment:","Unhealthiness:","How recommandable it is:","Comments:"]
        #print(data)
        for item in data:
            print(item)
        
        if size==0:
            return render_template("revhospital.html",orgnames=orgnames)
        
        else:
            return render_template("revhospitaly.html",data=data,size=size,cols=cols,datalist=datalist,orgnames=orgnames)
    
@app.route('/revrestaurantshow')
def showrevrest():
    con = mysql.connect()
    cur = con.cursor()
    otype = "Restaurant"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)
    return render_template("revrestaurant.html",orgnames=orgnames)    

@app.route('/revrestaurant',methods=['POST','GET'])
def revrestaurant():
    details = request.form
    rname = details['rname']
    print(rname)
    con = mysql.connect()
    cur = con.cursor()
    otype = "Restaurant"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)
    if rname == 'none':
        return render_template("revrestaurant.html",orgnames=orgnames)
    
    else:
        sql = """ select name,rate,most,comments from restaurant where rname = %s """
        cur.execute(sql,(rname,))
            
        data = cur.fetchall()
        size = len(data)
        cols = len(data[0])
        datalist = ["Name:","Rating:","Most liked:","Comments:"]
        #print(data)
        
        for item in data:
            print(item)
        
        return render_template("revrestaurantx.html",data=data,size=size,cols=cols,datalist=datalist,orgnames=orgnames)

@app.route('/showrevInstitute')
def showrevinst():
    con = mysql.connect()
    cur = con.cursor()
    otype = "Institute"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)
    return render_template("revinstitute.html",orgnames=orgnames)

@app.route('/revinstitute',methods=['POST','GET'])
def revinstitute():
    details = request.form
    iname = details['iname']
    print(iname)
    con = mysql.connect()
    cur = con.cursor()
    otype = "Institute"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)
    if iname == 'none':
        return render_template("revinstitute.html",orgnames=orgnames)
    
    else:
        sql = """ select name,course,rate1,rate2,rate3,cmnts from institute where iname = %s """
        cur.execute(sql,(iname,))
            
        data = cur.fetchall()
        size = len(data)
        cols = len(data[0])
        datalist = ["Name:","Department:","Acadamics Rating:","Extra and Co curricular activities Rating:","How recommandable it is:","Comments:"]
        #print(data)
        
        for item in data:
            print(item)
        
        return render_template("revinstitutex.html",data=data,size=size,cols=cols,datalist=datalist,orgnames=orgnames)

@app.route('/showInstitute')
def Institute():
    con = mysql.connect()
    cur = con.cursor()
    otype = "Institute"
    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)

    return render_template("institute.html",orgnames=orgnames)

@app.route('/showResponses')
def review():
    return render_template("review.html")

@app.route('/restaurantform',methods=['POST','GET'])
def revrest():
    #form = SignUpform()

    #if form.validate_on_submit():
    details = request.form
    uname = details['uname']
    email = details['email']
    phno = details['phno']
    add1 = details['address1']
    add2 = details['address2']
    add3 = details['address3']
    most = details['most']
    rate = details['rate']
    cmnts = details['cmnts']
    rname = details['rname'] 
    print("",uname,email)
    con = mysql.connect()
    cur = con.cursor()
    sql = """INSERT INTO restaurant(name,email,phone,add1,add2,add3,rate,most,comments,rname) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        cur.execute(sql,(uname,email,phno,add1,add2,add3,rate,most,cmnts,rname))
        con.commit()

    except:
        con.rollback()
        return render_template("restaurant.html")
    
    finally:
        cur.close()
        con.close()
    
    return render_template("home.html")

@app.route('/Hospitalform',methods=['POST','GET'])
def revhosp():
    #form = SignUpform()

    #if form.validate_on_submit():
    details = request.form
    uname = details['uname']
    age = details['age']
    email = details['email']
    phno = details['phno']
    add1 = details['add1']
    add2 = details['add2']
    add3 = details['add3']
    rate = details['rate']
    doc = details['doc']
    most = details['most']
    cmnts = details['cmnts']
    hname = details['hname']
    dname = details['dname'] 
    print("",uname,email)
    con = mysql.connect()
    print("",con)
    cur = con.cursor()
    sql = """INSERT INTO hospital(name,age,email,phno,add1,add2,add3,dis,rate,most,cmnts,hname,dname) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        cur.execute(sql,(uname,age,email,phno,add1,add2,add3,doc,rate,most,cmnts,hname,dname))
        con.commit()

    except Exception as e:
        print(e)
        con.rollback()
        return render_template("hospital.html")
    
    finally:
        cur.close()
        con.close()
    
    return render_template("home.html")


@app.route('/Instituteform',methods=['POST','GET'])
def revinst():
    #form = SignUpform()

    #if form.validate_on_submit():
    details = request.form
    uname = details['uname']
    course = details['course']
    email = details['email']
    phno = details['phno']
    add1 = details['add1']
    add2 = details['add2']
    add3 = details['add3']
    rate1 = details['rate1']
    rate2 = details['rate2']
    rate3 = details['rate3']
    cmnts = details['cmnts']
    iname = details['iname'] 
    print("",uname,email)
    con = mysql.connect()
    print("",con)
    cur = con.cursor()
    sql = """INSERT INTO institute(name,course,email,phno,add1,add2,add3,rate1,rate2,rate3,cmnts,iname) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        cur.execute(sql,(uname,course,email,phno,add1,add2,add3,rate1,rate2,rate3,cmnts,iname))
        con.commit()

    except Exception as e:
        print("",e)
        con.rollback()
        return render_template("institute.html")
    
    finally:
        cur.close()
        con.close()
    
    return render_template("home.html")

@app.route("/getPost",methods=["POST","GET"])
def req():
    details = request.form
    ortype = details['ortype']
    orname = details['orname']
    sop = details['sop'] 
    print("",ortype,orname)
    con = mysql.connect()
    cur = con.cursor()
    sql = """INSERT INTO request(ortype,orname,sop) VALUES(%s,%s,%s)"""
    try:
        cur.execute(sql,(ortype,orname,sop))
        con.commit()

    except:
        con.rollback()
        return render_template("post.html")
    
    finally:
        cur.close()
        con.close()
    
    return render_template("successx.html")

@app.route('/showadmin')
def showadmin():
    return render_template("admin.html")

@app.route('/admin',methods=["POST","GET"])
def admin():
    details = request.form
    uname = details['uname']
    pword = details['pword']
    
    print("",uname,pword)
    sql = '''SELECT uname,pword FROM admin'''
    con = mysql.connect()
    cur = con.cursor()
   
    cur.execute(sql)
    records = cur.fetchall()
    #count = cur.rowcount

    for row in records:
        
        unamex = row[0]
        pwordx = row[1]
            
        print("",unamex,pwordx)

        if uname==unamex and pword==pwordx:
            print("",unamex,pwordx)
            return render_template("request.html")

    return render_template("admin.html")


@app.route('/request')
def accept():
    con = mysql.connect()
    cur = con.cursor()
    sql = ''' select ortype,orname,sop FROM request '''
    cur.execute(sql)
    data = cur.fetchall()
    size = len(data)
    cols = 3
    datalist = ["Organisation type:","Organisation name:","Statement of Purpose:"]
    return render_template("requestx.html",data=data,size=size,cols=cols,datalist=datalist)            

@app.route('/acceptdecline/<string:otype>,<string:oname>',methods=["POST","GET"])
def accdec(otype,oname):

    con = mysql.connect()
    cur = con.cursor()

    print("org type : ",otype)
    print("org name: ",oname)
    
    
    sql = """INSERT INTO accept(otype,oname) VALUES(%s,%s)"""
    try:
        cur.execute(sql,(otype,oname))
        con.commit()

    except:
        con.rollback()
        return render_template("request.html")

    sqlx = """ select oname from accept where otype = %s """
    cur.execute(sqlx,(otype,))
    
    orgnames = cur.fetchall()
    #size = len(orgnames)

    if otype.lower()=="restaurant":
        return render_template("restaurant.html",orgnames=orgnames)
    
    if otype.lower()=="hospital":
        return render_template("hospital.html",orgnames=orgnames)

    if otype.lower()=="institute":
        return render_template("institute.html",orgnames=orgnames)
    

if __name__=="__main__":
    app.run(debug=False)
     