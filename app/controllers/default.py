from flask import render_template, request
from app import app
from app.controllers.alt_title import alt_title
from app.controllers.all_pages import all_pages
from app.controllers.w3c import w3c


@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/validacao', methods=["POST"])
def validacao():
	if request.method == 'POST':				
		# alt_title_results = alt_title(request.form['url'])
		todas_paginas = all_pages(request.form['url'])
		erros = w3c(todas_paginas)

	return render_template('validacao.html', erros=erros)
