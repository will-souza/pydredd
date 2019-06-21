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
		todas_paginas = all_pages(request.form['url'])
		alt_title_results = alt_title(todas_paginas)
		if 'w3c' in request.form:
			erros = w3c(todas_paginas)
		else:
			erros = 'pokemon'
		if 'alt-title-img' in request.form:
			alt_title_img = request.form['alt-title-img']
		else:
			alt_title_img = 'naruto'


	return render_template('validacao.html', erros=erros, alt_title_img=alt_title_img, alt_title_results=alt_title_results)
