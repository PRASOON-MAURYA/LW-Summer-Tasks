from flask import Flask
app = Flask(__name__)
@app.route('/')

def home_page():
    # write your pyhon code here to detect car number and give its details
    # let details of the car be saved in variables x1, x2, x2, x4
    
    x1 = "UP 29 PM 2001"
    x2 = "Prasoon Maurya"
    x3 = "18 Oct 2002"
    x4 = "Petrol"
    
    txt = '<h1 style="font-family:Georgia; color:rgb(0, 0, 230); font-size: 55px;">CAR DETAILS</h1>' + '<h1 style="font-family:Georgia; color:hsl(0, 100%, 50%); font-size: 45px;">'+"Car number is :"+' <h2 style="font-family:Courier; color:Fuchsia; font-size: 40px;">'"{t1}".format(t1 = x1)+'</h2>'+'</h1>' + '<h1 style="font-family:Georgia; color:hsl(0, 100%, 50%); font-size: 45px;">'+"Owner name is :"+' <h2 style="font-family:Courier; color:Fuchsia; font-size: 40px;">'"{t2}".format(t2 = x2)+'</h2>'+'</h1>'+'</h1>' + '<h1 style="font-family:Georgia; color:hsl(0, 100%, 50%); font-size: 45px;">'+"Registration Date :"+' <h2 style="font-family:Courier; color:Fuchsia; font-size: 40px;">'"{t3}".format(t3 = x3)+'</h2>'+'</h1>'+'</h1>' + '<h1 style="font-family:Georgia; color:hsl(0, 100%, 50%); font-size: 45px;">'+"Engine Type :"+' <h2 style="font-family:Courier; color:Fuchsia; font-size: 40px;">'"{t4}".format(t4 = x4)+'</h2>'+'</h1>'
    return  txt
  
if __name__ == "__main__":
    app.run(debug=True, port=2019)
