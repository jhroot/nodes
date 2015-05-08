import os
from flask import Flask, request
from flask.ext import restful
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = restful.Api(app)

# This is a dummy REST service and not intended for deployment
# It should track the API For the node builder

class BuildNodes(restful.Resource):
    def post(self):
        files = request.files
        if len(files) > 0:
            upload = files.items()[0][1]
            filename = secure_filename(upload.filename)
            upload.save(os.path.join('files', filename))
        return {'result': 'file uploaded'}

api.add_resource(BuildNodes, '/nodes')

if __name__ == '__main__':
    app.run(debug=True)