from flask import Flask, request, redirect, session
import datetime

app = Flask(__name__)
app.secret_key = "None"

@app.route("/successful")
def successful_request():
    user_name = session.get('user_name',None)
    return "successfully updated" + " " + str(user_name)

@app.route("/main",methods = ['POST'])
def getForm():
    session['user_name'] = request.form['sender_id']
    session['reciever_name'] = request.form['recipient_id']
    session['user_message'] = request.form['sender_message']
    
    #writing to file
    log_file = open('/home/yash/Projects/Python CRUD/log.txt','a')
    log_file.writelines(str(datetime.datetime.now()) + "\n")
    log_file.writelines("from : " + session['user_name'] + "\n")
    log_file.writelines("to : " + session['reciever_name'] + "\n")
    log_file.writelines(session['user_message'] + "\n\n")
    log_file.close()

    if request.method == 'POST':
        return redirect("successful")
    return "Error"


if __name__ == '__main__':
    app.run(debug=True)