# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#


from bottle import run, post, request
# Resto de importaciones
from pymongo import MongoClient
import hashlib
import utils
##############
# APARTADO 1 #
##############

# 
# Explicación detallada del mecanismo escogido para el almacenamiento de c
# contraseñas, explicando razonadamente por qué es seguro
#


@post('/signup')
def signup():
    nickname = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    if password != password2:
        return "<b>Las contraseñas no coinciden</b>"
    elif utils.getUser(nickname) != None:
        print utils.getUser(nickname)
        return "<b>El alias del usuario ya existe</b>"
    salt = utils.saltGenerator(len(password))
    m = hashlib.sha256()
    m.update(password)
    m.update(salt)
    m.update("123456789")
    password = m.hexdigest()
    print password
    utils.insertUser(nickname,name,email,country,password,salt)
    
@post('/change_password')
def change_password():
    pass
            

@post('/login')
def login():
    pass


##############
# APARTADO 2 #
##############


def gen_secret():
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    pass
    
    
def gen_gauth_url(app_name, username, secret):
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    pass
        

def gen_qrcode_url(gauth_url):  
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    pass
    


@post('/signup_totp')
def signup_totp():
    pass
        
        
@post('/login_totp')        
def login_totp():
    pass

    
if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
signup()