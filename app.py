import yake

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def hello_world():
    kw_extractor = yake.KeywordExtractor()
    request_data = request.get_json()
    text = request_data["text"]
    keywords = kw_extractor.extract_keywords(text)

    return jsonify(keywords)
    
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=5001)