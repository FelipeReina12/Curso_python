import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc  #pytz es una biblioteca para trabajar con fechas y horas en Python y utc es la zona horaria universal

data = pd.read_csv("C:/Users/Juanf/OneDrive/Documentos/Programación/Curso_python/Data_analisis/reviews.csv", parse_dates= ["Timestamp"]) 

data["Timestamp"] = pd.to_datetime(data["Timestamp"])
data["Week"] = data["Timestamp"].dt.strftime("%y %u")  #Aqui lo que hacemos es darle formato a la fecha para que nos muestre el año y las semanas
week_average = round(data.groupby(["Week"]).mean(numeric_only=True), 2)

char_def = """
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
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text= "Analisys of course Reviews", 
                 classes= "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a= wp, text= "These graphs represent course review analysis")

    hc = jp.HighCharts(a= wp, options = char_def)
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average["Rating"])
    return wp

jp.justpy(app)