from bottle import route, request, run

import os

@route('/fileselect')
def fileselect():
        return '''
    <form action="/upload" method="post" enctype="multipart/form-data">
      Category:      <input type="text" name="category" />
      Select a file: <input type="file" name="upload" multiple />
      <input type="submit" value="Start upload" />
    </form>
        '''

@route('/upload', method='POST')
def do_upload():
        category   = request.forms.getall('category')
        upload     = request.files.getall('upload')
        print dir(upload)
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png','.jpg','.jpeg'):
            return 'File extension not allowed.'

        #save_path = get_save_path_for_category(category)
        save_path = "/Users/joannsmac/bottle/static/images"
        upload.save(save_path) # appends upload.filename automatically
        return 'OK'

run(host='localhost', port=8080)