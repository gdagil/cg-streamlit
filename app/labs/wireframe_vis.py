from typing import Literal

import numpy as np
# from numpy.typing import NDArray
from pydantic import BaseModel


class LEffect(BaseModel):
    ambient: float|list[float]
    diffuse: float|list[float]
    fresnel: float|list[float]
    roughness: float|list[float]
    specular: float|list[float]


class LEffectRCSteps(LEffect):
    r_c_steps: int|None = None  # Range controle steps


class Wframe_3d:
    ambient_range = (0.0, 1.0)
    diffuse_range = (0.0, 1.0)
    fresnel_range = (0.0, 5.0)
    roughness_range = (0.0, 1.0)
    specular_range = (0.0, 1.0)


    @staticmethod
    def st_text_menu_prizm(st):
        st.header('Каркасная визуализация выпуклого многогранника. Удаление невидимых линий')

        st.subheader('Задание:')
        st.write('''
            Разработать формат представления многогранника и процедуру его каркасной 
            отрисовки в ортографической и изометрической проекциях. Обеспечить удаление невидимых 
            линий и возможность пространственных поворотов и масштабирования многогранника. 
            Обеспечить автоматическое центрирование и изменение размеров изображения при изменении 
            размеров окна
            \n
            Гранная прямая правильная призма
        ''') 
        radius = st.slider('Радиус призмы', 0.1, 10.0, step=0.1, value=5.0)
        delta_z = st.slider('Высота призмы', 0.1, 30.0, step=0.1, value=5.0)
        num_of_slices = st.slider('Количество граней', 3, 30, step=1, value=5)
        cyl_op = st.slider('Прозрачность цилиндра', 0.0, 1.0, step=0.1, value=0.9)
        bord_op = st.slider('Прозрачность верхней и нижней грани', 0.0, 1.0, step=0.1, value=1.0)
        return radius, delta_z, num_of_slices, cyl_op, bord_op


    @staticmethod
    def st_text_menu_cone(st, lab:Literal["3", "6"]="3"):
        if lab == "3":
            st.header('Основы построения фотореалистичных изображений')
            st.subheader('Задание:')
            st.write('''
                Используя результаты Л.Р.№2, аппроксимировать заданное тело выпуклым многогранником. Точность
                аппроксимации задается пользователем. Обеспечить возможность вращения и масштабирования многогранника и
                удаление невидимых линий и поверхностей. Реализовать простую модель закраски для случая одного источника света.
                \n
                Прямой усеченный круговой конус
            ''') 
        elif lab == "6":
            st.header('Создание анимационных эффектов')
            st.subheader('Задание:')
            st.write('''Для поверхности, созданной в прощлой ЛР, обеспечить выполнение эффекта изменения 
                интенсивности источника рассеянного света
            ''') 
        radius_1 = st.slider('Нижний радиус конуса', 0.1, 10.0, step=0.1, value=8.1)
        radius_2 = st.slider('Верхний радиус конуса', 0.1, 10.0, step=0.1, value=2.8)
        delta_z = st.slider('Высота конуса', 0.1, 30.0, step=0.1, value=11.4)
        num_of_slices = st.slider('Количество граней', 3, 30, step=1, value=30)
        cyl_op = st.slider('Прозрачность цилиндра', 0.0, 1.0, step=0.1, value=1.0)
        bord_op = st.slider('Прозрачность нижней и верхней грани', 0.0, 1.0, step=0.1, value=1.0)
        return radius_1, radius_2, delta_z, num_of_slices, cyl_op, bord_op


    @staticmethod
    def st_lighting_effects(st, range_control:bool=False) -> LEffectRCSteps:
        st.subheader('Освещение объекта')

        if range_control:
            r_c_steps = st.slider(
                "Определите количество кадров анимации", 
                1,
                100,
                step=1,
                value=30
            )
        else:
            r_c_steps=None

        st.write('''ambient - рассеянный свет увеличивает общую видимость 
            цвета, но может размыть изображение
        ''')
        if range_control:
            a_r = st.slider("Определите интервал ambient", value=Wframe_3d.ambient_range)
            ambient = np.linspace(a_r[0], a_r[1], r_c_steps).tolist()
        else:
            ambient = st.slider("Выберите ambient", Wframe_3d.ambient_range[0], Wframe_3d.ambient_range[1], step=0.01, value=0.8)


        st.write('''diffuse - степень отражения падающих лучей
            в различных ракурсах
        ''')
        if range_control:
            d_r = st.slider("Определите интервал diffuse", value=Wframe_3d.diffuse_range)
            diffuse = np.linspace(d_r[0], d_r[1], r_c_steps).tolist()
        else:
            diffuse = st.slider("Выберите diffuse", Wframe_3d.diffuse_range[0], Wframe_3d.diffuse_range[1], step=0.01, value=0.8)


        st.write('''fresnel - коэффициент отражения в зависимости от
            угла обзора; например, бумага отражает при просмотре ее
            от края бумаги (почти на 90 градусов), возникает сияние
        ''')
        if range_control:
            f_r = st.slider("Определите интервал fresnel", value=Wframe_3d.fresnel_range)
            fresnel = np.linspace(f_r[0], f_r[1], r_c_steps).tolist()
        else:
            fresnel = st.slider("Выберите fresnel", Wframe_3d.fresnel_range[0], Wframe_3d.fresnel_range[1], step=0.01, value=0.2)


        st.write('''roughness - изменяет зеркальное отражение; 
            чем грубее поверхность, чем шире и менее контрастен блеск
        ''')
        if range_control:
            r_r = st.slider("Определите интервал roughness", value=Wframe_3d.roughness_range)
            roughness = np.linspace(r_r[0], r_r[1], r_c_steps).tolist()
        else:
            roughness = st.slider("Выберите roughness", Wframe_3d.roughness_range[0], Wframe_3d.roughness_range[1], 
                step=0.01, value=0.5
            )


        st.write('''specular - уровень отражения падающих лучей
            в одном направлении, вызывающий блеск
        ''')
        if range_control:
            s_r = st.slider("Определите интервал specular", value=Wframe_3d.specular_range)
            specular = np.linspace(s_r[0], s_r[1], r_c_steps).tolist()
        else:
            specular = st.slider("Выберите specular", Wframe_3d.specular_range[0], Wframe_3d.specular_range[1], step=0.01, value=0.05)


        return LEffectRCSteps(
            ambient=ambient,
            diffuse=diffuse,
            fresnel=fresnel,
            roughness=roughness,
            specular=specular,
            r_c_steps=r_c_steps if r_c_steps else 1
        )

    @staticmethod
    def st_lighting_effects_checkboxes(st) -> dict[str,bool]:
        st.write("Выбор эффектов анимации")
        ambient = st.checkbox('ambient', value=True)
        diffuse = st.checkbox('diffuse')
        fresnel = st.checkbox('fresnel')
        roughness = st.checkbox('roughness')
        specular = st.checkbox('specular')
        return dict(
            ambient=ambient,
            diffuse=diffuse,
            fresnel=fresnel,
            roughness=roughness,
            specular=specular
        )
    