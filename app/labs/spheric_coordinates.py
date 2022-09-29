import numpy as np


class Scoords:
    @staticmethod
    def st_text_menu(st):
        st.header('Построение изображений 2D-кривых')

        st.subheader('Задание:')
        st.write('Написать и отладить программу, строящую изображение заданной замечательной кривой.')
        st.latex(r"ρ = {a\overϕ}, \qquad 0 < A \leq ϕ \leq B")
        st.markdown(r'''
            * $ρ,ϕ$- полярные координаты
            * $x,y$ – декартовы координаты t – независимый параметр.
            * $a,b, k,A,B$ - константы, значения которых выбираются пользователем.
        ''')   
        b_default = float("{0:.1f}".format(2*np.pi))
        a_varible = st.slider('Выберите A', 0.01, b_default-0.04, step=0.01, value=0.01)
        b_varible = st.slider('Выберите B', a_varible, b_default, step=0.01, value=b_default)
        a_lower_case_varible = st.slider('Выберите a', -1, 1, step=2, value=1)
        st.latex(f'0 < {a_varible} \leq ϕ \leq {b_varible}')
        return a_varible, b_varible, a_lower_case_varible

    @staticmethod
    def logistic_func(a, p):
        return a*p