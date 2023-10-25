from flask import Flask, render_template, request
import psutil

app = Flask(__name__)
online_users = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    username = request.form.get('username')
    #if username is not unique, return back to home page with some alert message
    if username in  online_users:
        return render_template("home.html",message = "username is not unique")
    #get ip address, mac address and maybe hostname of the user
    client_ip = request.remote_addr
    #add this in database
    online_users[username] = client_ip
    #return to a page where all online users are shown
    #return render_template("/online_users",users = online_users)
    return client_ip

@app.route("/online_users")
def online(users):
    return render_template("online_users.html",users = users)

'''host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)'''
net_ifs = psutil.net_if_addrs()
desired_interface = 'Wi-Fi'
if desired_interface in net_ifs:
    host_ip = net_ifs[desired_interface][1].address
else:
    host_ip = "127.0.0.1"

if __name__ == "__main__":
    app.run(host=host_ip,port=5555,debug=True)
