import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np


class Plotter:
    scenes_4 = {
        "1_1": dict(eye=dict(x=0, y=2, z=0)),
        "1_2": dict(eye=dict(x=2, y=0, z=0)),
        "2_1": dict(eye=dict(x=0, y=0, z=2)),
        "2_2": dict(eye=dict(x=2, y=2, z=2)),
    }   


    @staticmethod
    def polar_plot(func, phi:float, a:int, width:int, color:str="red", dash:str="dash") -> go.Figure:
        fig = go.Figure()
        fig.add_trace(go.Scatterpolargl(
            r=func(a, phi), 
            mode='lines', 
            line=dict(color=color, width=width, dash=dash)))
        fig.update_layout(width=1000, height=900)
        return fig

    @staticmethod
    def wireframe_plot_4_scenes(figs_list:list) -> go.Figure:
        rows = 2
        cols = 2
        ultra_plot = make_subplots(rows=rows, cols=cols,
            specs=[[{"type": "scene"}, {"type": "scene"}],
                [{"type": "scene"}, {"type": "scene"}]],
                row_heights=[5, 5]
            )
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                for fig in figs_list: 
                    ultra_plot.add_trace(fig, row=row, col=col)
        
        ultra_plot.update_layout(scene1_camera=Plotter.scenes_4["1_1"])
        ultra_plot.update_layout(scene2_camera=Plotter.scenes_4["1_2"])
        ultra_plot.update_layout(scene3_camera=Plotter.scenes_4["2_1"])
        ultra_plot.update_layout(scene4_camera=Plotter.scenes_4["2_2"])
        
        ultra_plot.update_layout(height=1000, width=900)
        return ultra_plot


class Figure:
    number_of_slices = 3
    height = 8
    slice_weight = 2

    def __init__(
        self, 
        number_of_slices:int=3,
        slice_weight:float=2.0,
        height:float=8.0
        ):

        self.number_of_slices = number_of_slices + 1
        slice_weight = slice_weight
        self.height = height

    def circle(self, z_coordinate:float, radius:float=5.0, opacity:float=1.0) -> go.Surface:
        """Create a circular mesh located at 0, 0, z with radius"""
        r_discr = np.linspace(0, radius, 2)
        theta_discr = np.linspace(0, 2*np.pi, self.number_of_slices)
        r_grid, theta_grid = np.meshgrid(r_discr, theta_discr)
        x_circle = r_grid * np.cos(theta_grid)
        return go.Surface(
            x=x_circle, 
            y=r_grid * np.sin(theta_grid), 
            z=np.zeros_like(x_circle) + z_coordinate, 
            showscale=False,
            opacity=opacity
            )

    def cylinder(self, delta_z:float=5, radius:float=5.0, opacity:float=0.9) -> go.Surface:
        """Create a cylindrical mesh located at 0, 0, 0, with radius and height delta_z"""
        center_z = np.linspace(0, delta_z, 15)
        theta = np.linspace(0, 2*np.pi, self.number_of_slices)
        theta_grid, z_grid = np.meshgrid(theta, center_z)
        return go.Surface(
            x=radius * np.cos(theta_grid), 
            y=radius * np.sin(theta_grid), 
            z=z_grid, 
            colorscale=[[0, '#530b96'],[1, '#530b96']], 
            showscale=False, 
            opacity=opacity
            )