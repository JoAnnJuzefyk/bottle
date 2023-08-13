import os
from bottle import route, run, template, static_file

index_html = '''My first web app! By <strong>{{ author }}</strong>.'''


@route('/')
def index():
    return template(index_html, author='Real Python')


@route('/name/<name>')
def name(name):
    return template('templates/max_image.html', name=name)

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='/Users/joannsmac/bottle/static/images')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
