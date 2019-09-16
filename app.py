import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Rainy Days in 2019"
mytitle = "It rains a lot"
x_values = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August']
y1_values = [10, 9, 11, 10, 11, 11]
y2_values = [11, 10, 10, 7, 5, 2]
y3_values = [10, 10, 11, 11, 12, 10]
color1 = '#33AFFF'
color2 = '#15537A'
color3 = '#B3E2FF'
name1 = 'Washington DC'
name2 = 'San Francisco'
name3 = 'Nashville'
tabtitle = 'rainy days'
sourceurl = 'https://www.weather-us.com/en'
githublink = 'https://github.com/austinlasseter/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
