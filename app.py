from flask import Flask, request, render_template
from preprocess import preprocessing
from main import processImage
from pprint import pprint
import shutil
import google.generativeai as genai
genai.configure(api_key='AIzaSyAg6UtggTP8rYwWQ-oBhJQf7xDa7SyyhpE')
gemini_model = genai.GenerativeModel('gemini-pro')
chat = gemini_model.start_chat(history=[])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    if request.method == 'POST':
        img = request.form['File']
        print(img)
        path = 'new_test_imgs\\'+img
        pprint(path)

        shutil.copy(path, 'static')
        processed_image=preprocessing(path)
        processImage(processed_image)

        input_image = 'http://127.0.0.1:5000/static/'+img
        output_image = 'http://127.0.0.1:5000/static/output.jpg'
        html_page = 'http://127.0.0.1:5000/static/generated_code.html'
        css_page = 'http://127.0.0.1:5000/static/generated_final_code.html'
        
        with open('static/generated_code.html', 'r') as file:  # r to open file in READ mode
            html_as_string = file.read()
            file.close()

        gemini_response = chat.send_message(html_as_string+' write style.css code for this html')
        data = gemini_response.text
        data = data.replace('```', '')
        data = data.replace('css', '')

        css = '<style>'
        css += data
        css += '</style>'

        html_as_string = html_as_string.replace('<link rel="stylesheet" type="text/css" href="http://127.0.0.1:5000/static/stylesheet.css">', css)
        print(html_as_string)
        with open('static/generated_final_code.html', 'w') as file:  # r to open file in READ mode
            file.write(html_as_string)
        file.close()
        
        return render_template('index1.html', input_image=input_image, output_image=output_image, html_page=html_page, css_page=css_page)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
