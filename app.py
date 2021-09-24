import pandas as pd
import datetime as dt
from jupyter_dash import JupyterDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

daily_trip = pd.read_csv("daily_trip2020.csv")


# TODO: rename test_df
test_df = pd.read_csv("Monthly_stats2020.csv")

# TODO: consider making 2020-03-07 a global variable to make logic more clear
# Build App(Displaying both graphs, include Dropdown menu for second graph)
app = JupyterDash(__name__)
fig1 = px.line(daily_trip, x='Date', y='Counts', title='Daily Trips for Yellow Cabs in 2020').update_layout(
    shapes=[dict(type= 'line', yref= 'paper', y0= 0, y1= 1,xref= 'x', x0= "2020-03-07", x1= "2020-03-07")]).add_annotation(
        x="2020-03-07",text='State of emergency declared')

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children="Effect of COVID-19 on NYC's Yellow Cabs in 2020"),
        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.Label(["Options", dcc.Dropdown(id='amount-dropdown',value='Total Distance Travelled(miles)',
                  clearable=False, options=[{'label': c, 'value': c} for c in test_df.columns])]), 
              dcc.Graph(id='graph2')  
    ])
])


# Define callback to update graph
@app.callback(
    Output('graph2','figure'),
    [Input("amount-dropdown", "value")]
)
def update_figure(selected_amount):
  return px.line(x=test_df.index,y=test_df[selected_amount], title=f"Monthly {selected_amount} for Yellow Cabs in 2020",labels={
              "x": "Month","y": f"{selected_amount}"}).update_layout(shapes=
              [dict(type= 'line', yref= 'paper', y0= 0, y1= 1,xref= 'x', x0= 2.1, x1= 2.1)]).add_annotation(
                  x=2.1,text='State of emergency declared')

# Run app and display url result inline in the notebook so you can click url
if __name__=='__main__':
  app.run_server(debug=True)