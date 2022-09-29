import plotly.graph_objects as go
import pandas as pd
import numpy as np


Z = np.linspace(0,np.pi/2)

class Plotter:
    @staticmethod
    def polar_plot(func, phi:float, a:int, width:int, color:str="red", dash:str="dash") -> go.Figure:
        fig = go.Figure()
        fig.add_trace(go.Scatterpolargl(
            r=func(a, phi), 
            mode='lines', 
            line=dict(color=color, width=width, dash=dash)))
        fig.update_layout(width=700, height=700)
        return fig