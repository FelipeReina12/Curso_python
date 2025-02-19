import justpy as jp
#Pagina para ver las funciones de juspy "Highcharts Documentation"
#Para buscar los tipos de lines vamos a Chart and series types
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc  #pytz es una biblioteca para trabajar con fechas y horas en Python y utc es la zona horaria universal

data = pd.read_csv("C:/Users/Juanf/OneDrive/Documentos/Programación/Curso_python/Data_analisis/reviews.csv", parse_dates= ["Timestamp"])  #Leemos el archivo csv y convertimos la columna Timestamp a fecha y hora

data["Day"] = data["Timestamp"].dt.date  #Crea una nueva columna "Day" que contenga solo la fecha
day_average = round(data.groupby("Day").mean(numeric_only=True), 2)  #Aqui agrupamos por la columna "Day" y calculamos el promedio de cada columna numérica

#A continuación creamos la chart_def que contiene la configuración de la gráfica (Esto es un codigo de javaScript)
chart_def = """ 
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]

    }]
}
"""
def app():  #Creamos una función para la aplicación
    wp = jp.QuasarPage()  #Esto es para crear una página web 
    h1 = jp.QDiv(a = wp, text= "Analisys of course Reviews",  #Aqui creamos un título para nuestra página, le damos los parametros de tamaño que deseamos
                 classes= "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a= wp, text= "These graphs represent course review analysis")  #p1 es es donde se muestra el texto de la página, p1 hace referencia a que es un párrafo
    hc = jp.HighCharts(a = wp, options = chart_def)  #Con hc creamos un gráfico de alta definición, a es para especificar el lugar donde se mostrar, wp es la página que creamos al principio
    hc.options.title.text = "Averge Rating by Day"  #Aqui pasamos la key del diccionario para ver la value, la cual es el texto del título y podemos cambiarlo

    hc.options.xAxis.categories = list(day_average.index)  #Aqui pasamos la key del diccionario para ver la value, la cual es la lista de días, categories es para especificar que es una lista de categorías
    hc.options.series[0].data = list(day_average["Rating"])  #Esto es para pasar los datos del dataframe a la gráfica

    return wp

jp.justpy(app)


