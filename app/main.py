import os

import streamlit as st
import numpy as np

from utils import Plotter, Figure, PickerFunc
from labs import Scoords, Wframe_3d, BSpline


st.set_page_config(
    page_title="ЛР по КГ",
    layout="wide", 
    )


with st.sidebar:
    st.title('Лабораторные работы по КГ - Гудынин Данила (вариант 11)')
    activation_function = st.selectbox(
        'Выбор рабораторных работ:',
        [
            'ЛР1 - функция в полярных координатах',
            'ЛР2 - гранная прямая правильная призма',
            'ЛР3 - Основы построения фотореалистичных изображений',
            'ЛР7 - Построение плоских полиномиальных кривых',
        ],
        label_visibility='hidden')


if activation_function == 'ЛР1 - функция в полярных координатах':
    with st.sidebar:
        a_varible, b_varible, a_lower_case_varible = Scoords.st_text_menu(st)
        params = PickerFunc.color_linetype_width_picker(st)
    st.subheader('График функции')
    logistic_fig = Plotter.polar_plot(
        Scoords.logistic_func,
        width=params.width,
        phi=np.linspace(a_varible, b_varible),
        a=a_lower_case_varible,
        color=params.color,
        dash=params.dash
        )
    st.plotly_chart(logistic_fig, use_container_width=True)


if activation_function == 'ЛР2 - гранная прямая правильная призма':
    with st.sidebar:
        radius, delta_z, num_of_slices, cyl_op, bord_op = Wframe_3d.st_text_menu_1(st)
    base = Figure(num_of_slices, height=delta_z)
    list_of_figures = [
        base.cylinder(delta_z, radius, opacity=cyl_op),
        base.circle(0, radius, opacity=bord_op),
        base.circle(delta_z, radius, opacity=bord_op),
    ]
    prism = Plotter.wireframe_plot_4_scenes(list_of_figures)

    st.plotly_chart(prism, use_container_width=True)


if activation_function == 'ЛР3 - Основы построения фотореалистичных изображений':
    with st.sidebar:
        radius_1, radius_2, delta_z, num_of_slices, cyl_op, bord_op = Wframe_3d.st_text_menu_2(st)
    base = Figure(num_of_slices, height=delta_z)
    cone = base.cone(delta_z, radius_1, radius_2, opacity=cyl_op)
    circle_1 = base.circle(0, radius_1, opacity=bord_op)
    circle_2 = base.circle(delta_z, radius_2, opacity=bord_op)
    fig = Plotter.wireframe_plot_1_scene(cone, [circle_1, circle_2])
    st.plotly_chart(fig, use_container_width=True)



if activation_function == 'ЛР7 - Построение плоских полиномиальных кривых':
    with st.sidebar:
        BSpline.st_text_menu(st)

    source_dots = Plotter.get_bokeh_column_data_source(dict(x=[1, 2.5, 4, 8, 9], y=[2, 5, 8, 2, 7]))
    source_b_spline = Plotter.get_bokeh_column_data_source(dict(x=[], y=[]))
    source_b_k = Plotter.get_bokeh_column_data_source(dict(x=[2], y=[2]))

    fig = Plotter.get_bakeh_dotes_drag(source_dots)
    slider = Plotter.get_bokeh_slider()

    callback = Plotter.get_bokeh_custom_js_callback(
        path=f"{os.path.dirname(__file__)}/utils/src/b_s_callback.js",
        sourses=dict(s_b=source_b_spline, s_d=source_dots, dim_b_s=source_b_k)
    )
    Plotter.add_bokeh_line(fig, x='x', y='y', line_width=3, source=source_b_spline, color="red", hover_alpha=1.0)

    Plotter.bokeh_js_on_change(slider, 'value', callback)
    Plotter.bokeh_js_on_change(source_dots, 'data', callback)

    col = Plotter.bokeh_column(slider, fig)

    st.bokeh_chart(col, use_container_width=True)