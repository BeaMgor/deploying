from flask import render_template,request, redirect, url_for
from app import app
import psycopg2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevoregistro', methods=['GET', 'POST'])
def nuevoregistro():
    if request.method == 'GET': 
        return render_template('nuevoregistro.html')
    else:
        dbParams = app.config['DATABASE']
        
        conn = psycopg2.connect (host=dbParams ['host'], port=dbParams['port'], dbname=dbParams ['dbname'], user=dbParams['dbuser'], password=dbParams['password'])
        cur = conn.cursor()
        query = """INSERT INTO movimientos (fecha_hora, descripcion, moneda_cimprada, cantida_comprada, moneda_pagada, cantidad_pagada)
                   VALUES ('{}', '{}', '{}', '{}', '{}', '{}');"""
        f = request.form 

        query = query.format(f['fecha'], f['hora'], f['descripcion'], f['moneda_comprada'], f['cantida_comprada'], f['moneda_pagada'], f['cantida_pagada'])

        cur.execute(query)

        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('index'))
