#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Sat May 30 15:31:16 2020
#
#@author: anonymous
#"""

from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
model=pickle.load(open('attrition.pkl','rb'))
sc=pickle.load(open('standard.pkl','rb'))
@app.route('/')
def helloworld():
    return  render_template("index.html")
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/about')
def about():
    return  render_template("about.html")
@app.route('/stats')
def stats():
    return  render_template("stats.html")
@app.route('/login',methods=['POST'])
def admin():
    b1=0
    b2=0
    b3=0
    c1=0
    c2=0
    c3=0
    e1=0
    e2=0
    e3=0
    e4=0
    g1=0
    g2=0
    g3=0
    g4=0
    h1=0
    h2=0
    h3=0
    m1=0
    m2=0
    m3=0
    m4=0
    a=request.form['age']
    b=request.form['bt']
    c=request.form['dept']
    d=request.form['distance']
    e=request.form['es']
    f=request.form['gender']
    g=request.form['js']
    h=request.form['ms']
    i=request.form['income']
    j=request.form['ot']
    k=request.form['percent']
    l=request.form['pr']
    m=request.form['rs']
    n=request.form['totalworkyear']
    o=request.form['promote']
    s=request.form['years']
    if(b=='Non-Travel'):
        b1,b2,b3=1,0,0;
    elif(b=='Travel_Frequently'):
        b1,b2,b3=0,1,0;
    elif(b=='Travel Rarely'):
        b1,b2,b3=0,0,1;  
    if(c=='Human Resources'):
        c1,c2,c3=1,0,0;
    elif(c=='Research & Development'):
        c1,c2,c3=0,1,0;
    elif(c=='Sales'):
        c1,c2,c3=0,0,1; 
    if(e==1):
        e1,e2,e3,e4=1,0,0,0;
    elif(e==2):
        e1,e2,e3,e4=0,1,0,0;
    elif(e==3):
        e1,e2,e3,e4=0,0,1,0;   
    elif(e==4):
        e1,e2,e3,e4=0,0,0,1;
    if(g==1):
        g1,g2,g3,g4=1,0,0,0;
    elif(g==2):
        g1,g2,g3,g4=0,1,0,0;
    elif(g==3):
        g1,g2,g3,g4=0,0,1,0;   
    elif(g==4):
        g1,g2,g3,g4=0,0,0,1;
    if(h=='Divorced'):
        h1,h2,h3=1,0,0;
    elif(h=='Married'):
        h1,h2,h3=0,1,0;
    elif(h=='Single'):
        h1,h2,h3=0,0,1; 
    if(m==1):
        m1,m2,m3,m4=1,0,0,0;
    elif(m==2):
        m1,m2,m3,m4=0,1,0,0;
    elif(m==3):
        m1,m2,m3,m4=0,0,1,0;   
    elif(m==4):
        m1,m2,m3,m4=0,0,0,1;
    if(f=="Female"):
        f=0;
    elif(f=='Male'):
        f=1;
    if(j=='No'):
        j=0;
    elif(j=='Yes'):
        j=1;
    if(l=='3'):
        l=0;
    elif(l=='4'):
        l=1;   
    t=[[int(m1),int(m2),int(m3),int(m4),int(h1),int(h2),int(h3),int(g1),int(g2),int(g3),int(g4),int(e1),int(e2),int(e3),int(e4),int(c1),int(c2),int(c3),int(b1),int(b2),int(b3),int(a),float(d),int(f),float(i),int(j),float(k),int(l),int(n),int(s),int(o)]]#typecasting as the input we receive from the ui is string
    y=model.predict(sc.fit_transform(t))
    y=str(y[0])
    if(y=='0'):
        z="The employee will stay."
    else:
        z="The employee will leave..."
    return render_template("index.html",y=z)#as y is a dataframe lists of lists so we  index to extract the actual string
if(__name__=="__main__"):
    app.run(debug=True)