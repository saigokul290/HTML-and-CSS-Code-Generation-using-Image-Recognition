import google.generativeai as genai
genai.configure(api_key='AIzaSyAg6UtggTP8rYwWQ-oBhJQf7xDa7SyyhpE')
gemini_model = genai.GenerativeModel('gemini-pro')
chat = gemini_model.start_chat(history=[])

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