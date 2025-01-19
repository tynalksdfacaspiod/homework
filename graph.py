import numpy
import pylab
from matplotlib.widgets import Slider, RadioButtons, CheckButtons, Button
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

def gauss(sigma, mu, x):
    ''' Отображаемая функция '''
    return (1.0 / (sigma * numpy.sqrt(2.0 * numpy.pi)) *
            numpy.exp(-((x - mu) ** 2) / (2 * sigma ** 2)))

def derivative(sigma, mu, x):
    ''' Производная функции в точке '''
    return -( (x-mu)/(sigma**3 * numpy.sqrt(2 * numpy.pi)) *
             numpy.exp(-((x - mu) ** 2) / (2 * sigma**2)))

def tangent(sigma, mu, edge, x, dot):
    return gauss(sigma, mu, dot) + edge*(x - dot)

if __name__ == "__main__":
    def update_graph():
        ''' Функция для обновления графика '''
        # Будем использовать sigma и mu, установленные с помощью слайдеров
        global slider_sigma
        global slider_mu
        global slider_dot
        global graph_axes
        global radiobutton_color
        global grid_visible
        global tangent_visible

        types = {'Красный': 'r', 'Синий': 'b', 'Зелёный': 'g', 
                 'Пунктир': ':', 'Тире-точка': '-.'}

        # Используем атрибут val, чтобы получить значение слайдеров
        sigma = slider_sigma.val
        mu = slider_mu.val
        dot = slider_dot.val

        x = numpy.arange(-5.0, 5.0, 0.01) 
        y = gauss(sigma, mu, x)
        
        y2 = gauss(sigma, mu, dot)
        
        x3 = numpy.arange(dot - 1.0, dot + 1.0, 0.1)

        edge = derivative(sigma, mu, dot)
        y3 = tangent(sigma, mu, edge, x3, dot) 

        style = types[radiobuttons_color.value_selected]
        graph_axes.clear()
        if tangent_visible:
            graph_axes.plot(x3, y3, style)

        graph_axes.plot(x, y, style)
        graph_axes.plot(dot, y2, marker="o", markersize=10, markerfacecolor="green")
        

        if grid_visible:
            graph_axes.grid()
        pylab.draw()

    def on_change_graph(value):
        ''' Обработчик события изменения значений слайдеров '''
        update_graph()

    def on_radio_buttons_clicked(label):
        ''' Обработчик события при клике по RadioButton '''
        update_graph()

    def on_check_clicked(label):
        ''' !!! Обработчик события при клике по CheckButtonsоо '''
        global grid_visible
        global tangent_visible
        if label == 'Сетка':
            # Если щёлкнули на флажке "Сетка", 
            # то инвертируем значение переменной grid_visible
            grid_visible = not grid_visible
        if label == 'Касательная':
            tangent_visible = not tangent_visible
        update_graph()

    def on_clicked_button(val):
        slider_dot.reset()
        update_graph()

    # Создадим окно с графиком
    fig, graph_axes = pylab.subplots()
    graph_axes.grid()

    # !!! Состояние флажка и видимость сетки
    grid_visible = True
    tangent_visible = False

    # Оставим снизу от графика место для виджетов
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.55)

    # Создание слайдера для задания точки
    axes_slider_dot = pylab.axes([0.05, 0.43, 0.85, 0.04])
    slider_dot = Slider(axes_slider_dot,
                        label='dot',
                        valmin=-5.0,
                        valmax=5.0,
                        valinit=0.0,
                        valfmt='%1.2f')

    # Подпишемся на событие при изменении слайдера
    slider_dot.on_changed(on_change_graph)

    # Создание слайдера для задания sigma
    axes_slider_sigma = pylab.axes([0.05, 0.35, 0.85, 0.04])
    slider_sigma = Slider(axes_slider_sigma,
                          label='sigma',
                          valmin=0.1,
                          valmax=1.0,
                          valinit=0.5,
                          valfmt='%1.2f')

    # Подпишемся на событие при изменении значения слайдера
    slider_sigma.on_changed(on_change_graph)

    # Создание слайдера для задания mu
    axes_slider_mu = pylab.axes([0.05, 0.27, 0.85, 0.04])
    slider_mu = Slider(axes_slider_mu,
                       label='mu',
                       valmin=-4.0,
                       valmax=4.0,
                       valinit=0.0,
                       valfmt='%1.2f')
    
    # Подпишемся на событие при изменении значения слайдера
    slider_mu.on_changed(on_change_graph)

    # Создание осей для переключателей
    axes_radiobuttons = pylab.axes([0.05, 0.05, 0.2, 0.2])
    
    # Создание переключателя
    radiobuttons_color = RadioButtons(axes_radiobuttons, 
                                      ['Красный','Синий','Зелёный', 
                                       'Пунктир','Тире-точка'])
    radiobuttons_color.on_clicked(on_radio_buttons_clicked)

    # !!! Создание осей флажка
    axes_checkbuttons = pylab.axes([0.35, 0.15, 0.2, 0.1])
    
    axes_checkbutton_tangent = pylab.axes([0.35, 0.05, 0.2, 0.1])
    
    # !!! Создание флажка
    checkbutton_grid = CheckButtons(axes_checkbuttons,
                                    ['Сетка'],
                                    [True])
    checkbutton_grid.on_clicked(on_check_clicked)

    checkbutton_tangent = CheckButtons(axes_checkbutton_tangent,
                                       ['Касательная'],
                                       [False])

    checkbutton_tangent.on_clicked(on_check_clicked)
    
    axes_reset_button = pylab.axes([0.55, 0.15, 0.2, 0.1])
    reset_button = Button(axes_reset_button,
                          'Reset',
                          color="red")
    reset_button.on_clicked(on_clicked_button)
    


    update_graph()
    pylab.show()
