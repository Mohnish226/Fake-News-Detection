from flask import Flask, request, jsonify, render_template
import pred
import json

app = Flask(__name__)
main_url = 'http://127.0.0.1:5000/'


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found_404(e):
    return f"404 PAGE NOT FOUND<br><br>You will be redirected in 3 seconds</p><script>var timer = setTimeout(function() {{window.location='{main_url}'}}, 3000);</script></body></html>"


@app.errorhandler(Exception)
def page_not_found(e):
    return f"Something went Wrong <br> You will be redirected in 3 seconds</p><script>var timer = setTimeout(function() {{window.location='{main_url}'}}, 3000);</script></body></html>"


@app.route('/api/text', methods=['GET'])
def api_id():
    text = request.args.get('txt', None)
    save = request.args.get('sav', None)
    print(eval(str(save).title()))
    if text:
        if len(text) < 30:
            return jsonify({'error': 'text too small to predict, are you using the provided data ?'})
        return jsonify({str(round(pred.predict(text) * 100, 2)): ' ' + str(round(pred.predict(text) * 100, 2)) + ' % Fake'})#,
                        #'save': "Do you want to save ? " + str(save)})
    else:
        return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
