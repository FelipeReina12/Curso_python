import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text= "Analisys of course Reviews", 
                 classes= "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a= wp, text= "These graphs represent course review analysis")
    return wp

jp.justpy(app)


