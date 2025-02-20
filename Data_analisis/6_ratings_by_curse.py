import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc  #pytz es una biblioteca para trabajar con fechas y horas en Python y utc es la zona horaria universal

data = pd.read_csv("C:/Users/Juanf/OneDrive/Documentos/Programación/Curso_python/Data_analisis/reviews.csv", parse_dates= ["Timestamp"])  #Parse_dates es para que pandas reconozca la fecha en la columna
share = data.groupby(["Course Name"])["Rating"].count()

char_def = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Egg Yolk Composition'
    },
    tooltip: {
        valueSuffix: '%'
    },
    subtitle: {
        text:
        'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" target="_default">MDPI</a>'
    },
    plotOptions: {
        series: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text= "Analisys of course Reviews", 
                 classes= "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a= wp, text= "These graphs represent course review analysis")

    hc = jp.HighCharts(a = wp, options= char_def)
    hc_data = [{"name": v1, "y": v2} for v1, v2 in zip(share.index, share) ]
    hc.options.series[0].data = hc_data
    return wp

jp.justpy(app)


