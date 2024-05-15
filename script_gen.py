import os

def textbox_code():
    l = '<input type=\"text\"> '
    return l


def label_code():
    l = 'Label '
    return l


def radiobutton_code():
    l = '<input type=\"radio\" name=\"n\" value=\"v\"> '
    return l


def checkbox_code():
    l = '<input type=\"checkbox\"> '
    return l


def button_code():
    l = '<input type=\"submit\" value=\"Button\"> '
    return l


def image_code():
    #specify the path where the dummy image is persent, if not in the same dir
    l = '<img src="http://127.0.0.1:5000/static/dummy_image.png" height=50px alt=\"Image\"> '
    return l


def break_code():
    l = '\n<br><br>\n'
    return l

def generate_html():
    #path for storing the html file
##    path='Automatic-HTML-Code-Generation\\'
    #define the opening tags of html 
    html=open('static/generated_code.html','w')
    html.write('<HTML>\n<HEAD>\n')
    #link the css file
    #specify the full path in href if css not present in the same dir
    html.write('<link rel="stylesheet" type="text/css" href="http://127.0.0.1:5000/static/stylesheet.css">\n')
    html.write('<TITLE>Generated HTML Code</TITLE>\n')
    html.write('</HEAD>\n<BODY>\n')
    with open('temp.txt', 'r') as line:
        print("hiiiiiiiiiiiiii")
        lines=line.readlines()
        for line in lines:
            #split the line to obtain element_name, x and y
            l=line.split(',')
            #l=['element_name', x, y]
            #generate code for the specific element
            if(l[0]=='TextBox'):
                c=textbox_code()
            elif(l[0]=='Label'):
                c=label_code()
            elif(l[0]=='RadioButton'):
                c=radiobutton_code()
            elif(l[0]=='CheckBox'):
                c=checkbox_code()
            elif(l[0]=='Button'):
                c=button_code()
            elif(l[0]=='Image'):
                c=image_code()
            elif(l[0]=='BREAK\n'):
                c=break_code()
            else:
                print('printing else code', l)
            html.write(c)
        
    html.write('\n</BODY>\n</HTML>')
    
    #html script is generated
    #destroy the temp file now
    #change the path to temp file, if not in the same dir
    os.remove('temp.txt')
def generate_css():
    css = open('static/generated_style.css', 'w')
    css.write('/* Generated CSS Code */\n\n')
    
    # CSS for TextBox
    css.write('input[type="text"] {\n')
    css.write('\t/* Add your styling for TextBox here */\n')
    css.write('}\n\n')

    # CSS for Label
    css.write('.label {\n')
    css.write('\t/* Add your styling for Label here */\n')
    css.write('}\n\n')

    # CSS for RadioButton
    css.write('input[type="radio"] {\n')
    css.write('\t/* Add your styling for RadioButton here */\n')
    css.write('}\n\n')

    # CSS for CheckBox
    css.write('input[type="checkbox"] {\n')
    css.write('\t/* Add your styling for CheckBox here */\n')
    css.write('}\n\n')

    # CSS for Button
    css.write('input[type="submit"] {\n')
    css.write('\t/* Add your styling for Button here */\n')
    css.write('}\n\n')

    # CSS for Image
    css.write('img {\n')
    css.write('\t/* Add your styling for Image here */\n')
    css.write('}\n\n')

    css.close()
#generate_css()
#generate_html()
