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
        print(riasec)
        result=findJob(riasec)
        jobs=[]
        for i in range(3):
            jobs.append(result[i].name)            
        print(jsonify({"jobs": jobs}))
        return jsonify({"jobs": jobs})
    except Exception as e:
        print(str(e))
        return((str(e)),500)

if __name__=='__main__':
    port = int(os.environ.get("PORT",8080))
    app.run(host='0.0.0.0',port=port,debug=True)
