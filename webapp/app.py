from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    page = """
    <h2>Home</h2>
    <p>Hello World!</p>
    <a href ="/sub">Subtract</a>
    <a href ="/mult">Multiply</a>
    <a href ="/add">Add</a>
    """

    return page

@app.route("/sub")
def sub():
    page = """
    <h2>Subtract</h2>
    <form action=/sub method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    <a href ="/">Home</a>
    <a href ="/mult">Multiply</a>
    <a href ="/add">Add</a>
    </form>
    """
    
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The result is {a-b}</p>"
    except:
        page += "<p>Invalid Inputs</p>"
    
    return page

@app.route("/mult")
def mult():
    page = """
    <h2>Multiply</h2>
    <form action=/mult method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    <a href ="/">Home</a>
    <a href ="/sub">Subtract</a>
    <a href ="/add">Add</a>
    </form>
    """
    
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The result is {a*b}</p>"
    except:
        page += "<p>Invalid Inputs</p>"
    
    return page

@app.route("/add")
def add():
    page = """
    <h2>Add</h2>
    <form action=/add method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    <a href ="/">Home</a>
    <a href ="/sub">Subtract</a>
    <a href ="/mult">Multiply</a>
    </form>
    """
    
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The result is {a+b}</p>"
    except:
        page += "<p>Invalid Inputs</p>"
    
    return page