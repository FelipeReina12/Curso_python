import justpy as jp
#Pagina para ver las funciones de juspy "Highcharts Documentation"
#Para buscar los tipos de lines vamos a Chart and series types
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from pytz import utc  #pytz es una biblioteca para trabajar con fechas y horas en Python y utc es la zona horaria universal

data = pd.read_csv("reviews.csv", parse_dates= ["Timestamp"]) 

data["Day"] = data["Timestamp"].dt.date  #Crea una nueva columna "Day" que contenga solo la fecha
day_average = data.groupby("Day").mean(numeric_only=True)

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: true
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
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
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
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]

    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text= "Analisys of course Reviews", 
                 classes= "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a= wp, text= "These graphs represent course review analysis")
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.title.text = "Averge Rating by Day"  #Aqui pasamos la key del diccionario para ver la value, la cual es el texto del título y podemos cambiarlo

    hc.options.series[0].data = list(zip(day_average.index, day_average["Rating"]))

    return wp

jp.justpy(app)


