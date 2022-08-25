from flask import Flask, request
app = Flask(__name__)

# http://127.0.0.1:5000/add?a=10&b=20
@app.route('/add')
def add():
    """A + B = result"""
    a = request.args['a']
    b = request.args['b']
    result = int(a) + int(b)
    return f'<h2> {a} + {b} = {result}</h2>'

# http://127.0.0.1:5000/subtract?a=10&b=20
@app.route('/subtract')
def subtract():
    """A - B = result"""
    a = request.args['a']
    b = request.args['b']
    result = int(a) - int(b)
    return f'<h2> {a} - {b} = {result}</h2>'

# http://127.0.0.1:5000/multiply?a=10&b=20
@app.route('/multiply')
def multiply():
    """A * B = result"""
    a = request.args['a']
    b = request.args['b']
    result = int(a) * int(b)
    return f'<h2> {a} * {b} = {result}</h2>'

# http://127.0.0.1:5000/divide?a=10&b=20
@app.route('/divide')
def divide():
    """A / B = result"""
    a = request.args['a']
    b = request.args['b']
    result = int(a) / int(b)
    return f'<h2> {a} / {b} = {result}</h2>'





# # Springboard's solution

# from flask import Flask, request
# from operations import add, sub, mult, div

# app = Flask(__name__)

# @app.route("/add")
# def do_add():
#     """Add a and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = add(a, b)

#     return str(result)

# @app.route("/sub")
# def do_sub():
#     """Subtract and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = sub(a, b)

#     return str(result)

# @app.route("/mult")
# def do_mult():
#     """Multiply a and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = mult(a, b)

#     return str(result)

# @app.route("/div")
# def do_div():
#     """Divide a and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = div(a, b)

#     return str(result)

# ## PART TWO

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)