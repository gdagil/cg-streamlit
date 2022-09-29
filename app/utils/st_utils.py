from pydantic import BaseModel


class Picker(BaseModel):
    dash: str
    color: str
    width: int


class PickerFunc:
    @staticmethod
    def color_linetype_width_picker(st) -> Picker:
        col1, col2, col3 = st.columns(3)
        with col1:
            dash=st.radio(
                "Вид линии: ",
                options=['dash', 'dashdot', 'dot', 'longdash', 'longdashdot', 'solid'],
            )
        with col2:
            color = st.color_picker(label="Цвет линии", value='#FF0000')
        with col3:
            width = st.slider('Толщина линии', 1, 10, step=1, value=3)
        return Picker(width=width, dash=dash, color=color)