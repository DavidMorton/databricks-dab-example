# import reflex as rx
import subprocess

# class Spline(rx.Component):
#     library = "@splinetool/react-spline"
#     lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
#     tag = "Spline"
#     is_default = True
#     scene: rx.Var[str]

# spline = Spline.create

# scene = "https://prod.spline.design/1eapv4LnOygEqB66/scene.splinecode"

# def spline_demo():
#     return spline(scene=scene)

subprocess.run([
    "reflex", 
    "run",
    "--env",
    "prod"
    ], check=True)

# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.express as px
# import dash_bootstrap_components as dbc

# # Initialize the Dash app with Bootstrap styling
# dash_app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# chart_data = pd.DataFrame({'x': [x for x in range(30)],
#                            'y': [2 ** x for x in range(30)]})

# # Define the app layout
# dash_app.layout = dbc.Container([
#     dbc.Row([dbc.Col(html.H1('Hello world!!!'), width=12)]),
#     dcc.Graph(
#         id='fare-scatter',
#         figure=px.scatter(chart_data, x='x', y='y',
#             labels={'x': 'Apps', 'y': 'Fun with data'},
#             template='simple_white'),
#         style={'height': '500px', 'width': f'{min(100 + 50 * 30, 1000)}px'}
#     )
# ], fluid=True)

# if __name__ == '__main__':
#     dash_app.run_server(debug=True)
