from flask import Flask
from textblob import TextBlob
from markupsafe import escape
from flask import request
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/sentiment*": {"origins": "*"}})


@app.route('/sentiment' , methods=['POST'])
def sentiment():
    try:
        content = request.json
    except:
        return json.dumps({})

    if not content or 'body' not in content:
        return json.dumps({})

    body = content["body"]
    escaped = escape(body)
    textBlob = TextBlob(escaped)

    data = {}
    data['polarity'] = textBlob.polarity
    data['subjectivity'] = textBlob.subjectivity
    json_data = json.dumps(data)

    print(json_data)

    return json_data