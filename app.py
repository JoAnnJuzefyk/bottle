import os
from bottle import route, run, template, static_file
from os.path import dirname, abspath, join


# added these 2 lines an update the def serve_static
CURDIR = dirname(abspath(__file__))
static_root = os.path.join(CURDIR, 'static', 'images')
TEMPLATE_DIR = os.path.join(CURDIR, 'templates')
index_html = '''My first web app! By <strong>{{ author }}</strong>.'''


@route('/')
def index():
    return template(index_html, author='Real Python')


@route('/adder')
def adder():
    return template(adder_html)


@route('/name/<name>')
def name(name):
    image_filename = f"{name}.jpg"  # Assuming the image format is JPG
    return static_file(image_filename, root=static_root)


@route('/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root=static_root)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
