from flask import render_template

from app import app


@app.errorhandler(404)
def error_404(e):
    title = '404 Página Não Encontrada'
    
    return render_template('404.html', title=title), 404
