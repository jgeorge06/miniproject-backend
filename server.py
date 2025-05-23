from flask import Flask,request,jsonify
from jobfind import *
from userdb import *
import os
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


def calculate(answers):
    j=0
    fullriasec=[0,0,0,0,0,0]
    riasec=[0,0,0,0,0,0]
    for i in answers:
        fullriasec[j//8]+=i
        j+=1
    for i in range(6):
        riasec[i]=float(fullriasec[i]/8)
    result=CR(riasec)
    jobs=[]
    links=[]
    for i in range(3):
        jobs.append(result[i].name)  
        links.append(result[i].link)
    return (fullriasec,jobs,links)

@app.route('/job_finder',methods=['POST'])
def job_finder():
    try:
        data=request.json
        answers=data.get("answers",[])
        uid=data.get("uid","")
        store(uid,answers)
        riasec,jobs,links = calculate(answers)
        return(jsonify({
            "riasec": riasec,
            "jobs": jobs,
            "links": links
        }))
    except Exception as e:
        return((str(e)),500)

@app.route('/data_retriever',methods=['POST'])
def data_retriver():
    try:
        data=request.json
        uid=data.get("uid","")
        answers = retrieve(uid)
        if answers:          
            riasec,jobs,links = calculate(answers[1:])
            return(jsonify({
                "flag": True,
                "riasec": riasec,
                "jobs": jobs,
                "links": links,
                "answers": answers[1:]
            }))
        return(jsonify({
            "flag": False
        }))
    except Exception as e:
        return((str(e)),500)
    
if __name__=='__main__':
    port = int(os.environ.get("PORT",8080))
    app.run(host='0.0.0.0',port=port,debug=True)
