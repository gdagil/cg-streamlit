import streamlit as st
import streamlit.components.v1 as components
import numpy as np

from utils import Plotter, PickerFunc
from labs import Scoords


st.title('Лабораторные работы по КГ')

activation_function = st.selectbox(
    'Выбор рабораторных работ:', 
    ['ЛР1 - (вариант 11) функция в полярных координатах'], 
    label_visibility='hidden')

## Logistic Function
if activation_function == 'ЛР1 - (вариант 11) функция в полярных координатах':
    a_varible, b_varible, a_lower_case_varible = Scoords.st_text_menu(st)
    params = PickerFunc.color_linetype_width_picker(st)
    st.subheader('График функции')
    logistic_fig  = Plotter.polar_plot(
        Scoords.logistic_func, 
        width=params.width, 
        phi=np.linspace(a_varible,b_varible), 
        a=a_lower_case_varible, 
        color=params.color,
        dash=params.dash
        )
    st.plotly_chart(logistic_fig)