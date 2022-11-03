import streamlit as st
import numpy as np

from utils import Plotter, Figure, PickerFunc
from labs import Scoords, Wframe_3d


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
            'ЛР2 - гранная прямая правильная призма'
        ],
        label_visibility='hidden')


# Logistic Function
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
        radius, delta_z, num_of_slices, cyl_op, bord_op = Wframe_3d.st_text_menu(st)
    base = Figure(num_of_slices, height=delta_z)
    list_of_figures = [
        base.cylinder(delta_z, radius, opacity=cyl_op),
        base.circle(0, radius, opacity=bord_op),
        base.circle(delta_z, radius, opacity=bord_op),
    ]
    prism = Plotter.wireframe_plot_4_scenes(list_of_figures)

    st.plotly_chart(prism, use_container_width=True)

