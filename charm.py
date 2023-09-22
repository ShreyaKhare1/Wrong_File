import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc 
import plotly.express as px 
a=pd.read_csv(r'C:\Users\lenovo\Downloads\500_Patient_Sample.csv')
def abc( id):
    c=a[a['Patient ID']==inp][['Age','Weight',"BP DISYS",'BP SYS']]
    print(c)
    d=a[a["Patient ID"]==inp].head()
    print(d)
inp=int(input("Enter Id"))
abc(inp)
app= dash.Dash(__name__)
app.layout=html.Div([html.H1("Timelime")])

print(app)
if __name__=='__main':
    app.run_server(debug=True)
#b=a[a['Patient ID']==2][['Age','Weight']]
#print(b)
#print(a[['Age','Weight']][4:16])
