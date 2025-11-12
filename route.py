from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


@app.route('/')
@app.route('/helper')
def action_helper(info= None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/pagina', methods=['GET'])
def action_pagina():
    return ctl.render('pagina')

#-----------------------------------------------------------------------------


@app.route('/home', method= 'GET')
def home():
    return ctl.render('home')

@app.route('/registers', method= 'GET')
def registers():
    return ctl.render('registers')

@app.route('/login', method= 'GET')
def login():
    return ctl.render('login')

@app.route('/relatorios', method= 'GET')
def relatorios():
    return ctl.render('relatorios')

@app.route('/cadastro', method= 'GET')
def cadastro():
    return ctl.render('cadastro')

if __name__ == '__main__':

    run(app, host='127.0.0.1', port=8080, debug=True)
