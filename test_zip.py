import zipfile 
import os
import sys
  
from flask import Flask, render_template, request, current_app, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/form')
def form():
    return render_template('form.html')
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files.getlist("file")
      for p in f: 
        p.save('uploads/' + p.filename)

      # importing ZipFile class from zipfile module
      from zipfile import ZipFile

      # more fine-grained control over ZIP files
      with ZipFile("uploads/zip_return.zip", "w") as newzip:
          for p in f:
            newzip.write('uploads/' + p.filename)
          newzip.close()

      return (
        render_template('uploads.html')
      )

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, path=filename)
    
		
if __name__ == '__main__':
   app.run(host='localhost', port=5000, debug=True)