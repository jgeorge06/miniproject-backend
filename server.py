from flask import Flask,request,jsonify
from jobfind import *
import os
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/job_finder',methods=['POST'])
def job_finder():
    try:
        data=request.json
        riasec=data.get("riasecscore",[])
        for i in range(6):
            riasec[i]=riasec[i]/8
        result=PC(riasec)
        jobs=[]
        links=[]
        for i in range(3):
            jobs.append(result[i].name)  
            links.append(result[i].link)
        return jsonify({
            "jobs": jobs,
            "links":links
            })
    except Exception as e:
        return((str(e)),500)

if __name__=='__main__':
    port = int(os.environ.get("PORT",8080))
    app.run(host='0.0.0.0',port=port,debug=True)
