import zipfile 
import os
import sys
  
from flask import Flask, render_template, request
#from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)

      # importing ZipFile class from zipfile module
      from zipfile import ZipFile

      # more fine-grained control over ZIP files
      with ZipFile("zip_return.zip", "w") as newzip:
          newzip.write(f.filename)
          newzip.close()

      return (
          """\
            <html>
            <body>
                <h1> TADA </h1>
                <p> <a href=\"""" + os.getcwd() + """\"zip_return.zip\" download> Download </a> </p>
            </body>
            </html>
          """
      )
		
if __name__ == '__main__':
   app.run(host='localhost', port=5000, debug=True)