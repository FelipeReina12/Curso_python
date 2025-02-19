import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc  #pytz es una biblioteca para trabajar con fechas y horas en Python y utc es la zona horaria universal

data = pd.read_csv("C:/Users/102/Documents/FelipeReina12/Curso_python/Data_analisis/reviews.csv", parse_dates= ["Timestamp"])  #Leemos el archivo csv y convertimos la columna Timestamp a fecha y hora
data["Month"] = data["Timestamp"].dt.strftime("%y %u")
month_average_crs = round(data.groupby(["Month", "Course Name"])["Rating"]. mean(numeric_only=True).unstack(), 2)  #unstack se usa para transformar una columna en filas

char_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2024'
    },
    subtitle: {
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 30,
        y: 50,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        // Highlight the last years where moose hunting quickly deminishes
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766,
                29278,
                27487,
                26007
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048,
                52804,
                49317,
                52490
            ]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text= "Analisys of course Reviews", 
                 classes= "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a= wp, text= "These graphs represent course review analysis")

    hc =jp.HighCharts(a= wp, options=char_def)
    hc.options.xAxis.categories = list(month_average_crs.index)
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series = hc_data
    return wp

jp.justpy(app)


