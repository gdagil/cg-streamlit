class BSpline:
    @staticmethod
    def st_text_menu(st):
        st.header('Построение плоских полиномиальных кривых.')

        st.subheader('Задание:')
        st.write('''
            Написать программу, строящую полиномиальную кривую по заданным точкам. Обеспечить возможность
            изменения позиции точек и, при необходимости, значений касательных векторов и натяжения.
            ''') 
        st.markdown(
            r"""
                Общая формула для расчета коэффициентов:

                $$N_{i,k}(x)=\frac{x-t_i}{t_{i+k-1}-t_i}N_{i,k-1}(x)+\frac{t_{i+k}-x}{t_{i+k}-t_{i+1}}N_{i+1,k-1}(x)$$

                Формула рекурсивная и заканчивается наkравном единице:

                $$N_{i,1}(x)=\left\{\begin{array}{cr}1&\quad\text{if }t_i\leq x\leq t_{i+1}\\0&\quad\mathrm{otherwise}\quad\end{array}\right.$$

                Вычисление элементов массива:

                $$t=\left\{\begin{array}{ll}0,&\mathrm{if}\ i<k\\i-k+1,&\mathrm{if}\ k\leq{i}\leq{n}\\n-k+2,&\mathrm{if}\ i>n\end{array}\right.$$
            """
        )