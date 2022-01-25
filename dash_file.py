#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from flask import Flask


#define dataframe
df = px.data.iris()

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    #url_base_pathname='/yourpath'
)

# dash app layout
option = [
    {'label': 'Patal width', 'value': 'petal_width'},
    {'label': 'Petal length', 'value': 'petal_length'},
    {'label': 'Sepal width', 'value': 'sepal_width'},
    {'label': 'Sepal length', 'value': 'sepal_length'}
]

app.layout = html.Div(
    [
    dcc.Graph(id="scatter-plot"),
    html.Div(
        children=[
        html.Label('Select X'),
        dcc.Dropdown(
            id='select_x',
            options=option,
            value='petal_width'
        ),
        html.Br(),
        html.Label('Select Y'),
        dcc.Dropdown(
            id='select_y',
            options=option,
            value='petal_length'
        ),
        html.Br(),
        html.Label('Size'),
        dcc.Dropdown(
            id='size',
            options=option,
            value='sepal_length'
        )
    ], style={'padding': 10, 'flex': 1})  # end of children
    
], style={'display': 'flex', 'flex-direction': 'row'})  # end of Div

# callback - feed data
@app.callback( Output("scatter-plot", "figure"),
               [Input("select_x", "value"), Input("select_y", "value"), Input("size", "value")])

def update_scatter_chart(select_x, select_y, size):
    fig = px.scatter(df,
                     x=select_x, y=select_y,
                     color="species", size=size)
    fig.update_layout(width=600, height=400)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
