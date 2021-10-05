import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from numpy import arange
from numpy import meshgrid
import numpy as np
import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cbook
from matplotlib.colors import LightSource

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

plt.subplots_adjust(left=0.1, bottom=0.5)

# Criando arrays para X e Y
delta = 0.025
xrange = arange(-1.0, 1.0, delta)
yrange = arange(-1.0, 1.0, delta)
X, Y = meshgrid(xrange, yrange)

# Definindo valores iniciais de cada parâmetro
v = 330
L = 10
m0 = 5
n0 = 4
p0 = 7
q0 = 2
a0 = 1
b0 = 0.7071
c0 = 1
d0 = 3
slider_step = 0.2
# Calculando e imprimindo Frequência
f = v*math.sqrt((m0**2/L**2)+(n0**2/L**2))
fig.suptitle('Freq = %f' % f, fontdict=font)
# fig.text(2, 0.65, 'Freq = %f'%f, fontdict=font)

# Como a função original está na forma implícita foi necessário separar para plotar
# F é o lado esquerdo da equação, e G o outro
F = 0
G = c0*np.cos(np.pi*m0*X/a0)*np.cos(np.pi*n0*Y/b0)+d0*np.cos(np.pi*p0*X/a0)*np.cos(np.pi*q0*Y/b0)
#G = c0*np.sin(np.pi*m0*X/a0)*np.sin(np.pi*n0*Y/b0)+d0*np.sin(np.pi*n0*X/a0)*np.sin(np.pi*m0*Y/b0)
Z = F-G


# Func que desenha o gráfico
def draw(x, y, z):
    ax1.cla()  # Limpa o ax
    ax1.contour(x, y, z, [0])  # Plota os valores
    #ax[1].cla()
    #ax[1].contour(x, y, z, [0])
    ax2.cla()
    #ax2.plot_wireframe(x, y, z, rstride=6, cstride=6,alpha=0.5)
    ax2.contour(x, y, z, [0])
    ax2.plot_surface(x, y, z, rstride=5, cstride=5,vmin=-0.1,vmax=0.1,alpha=0.5,
                          linewidth=0.2, antialiased=False,cmap=cm.coolwarm)


draw(X, Y, Z)  # Chama função

plt.axis([-1, 1, -1, 1])  # Amplitude dos eixos

# Parâmetros gerais dos sliders
ax_color = 'lightgoldenrodyellow'
ax_width = 0.45
ax_height = 0.02


# Função que cria novo slider
def create_slider(x, i, x0, x_min, x_max):
    ax_x = plt.axes([0.25, 0.1+i*0.04, ax_width, ax_height], facecolor=ax_color)
    slider_x = Slider(ax_x, '%s' % x, x_min, x_max, valinit=x0, valstep=slider_step)
    return slider_x


slider_m = create_slider('m', 0, m0, 0.0, 10.0)
slider_n = create_slider('n', 1, n0, 0.0, 10.0)
slider_a = create_slider('a', 2, a0, 0.2, 10.0)
slider_b = create_slider('b', 3, b0, 0.2, 10.0)
slider_c = create_slider('c', 4, c0, -10.0, 10.0)
slider_d = create_slider('d', 5, d0, -10.0, 10.0)
slider_p = create_slider('p', 6, p0, 0.0, 10.0)
slider_q = create_slider('q', 7, q0, 0.0, 10.0)

def update(val):
    # Variáveis recebem valores do slider apenas quando este muda
    n = slider_n.val
    m = slider_m.val
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    d = slider_d.val
    p = slider_p.val
    q = slider_q.val
    f = v*math.sqrt((m**2/L**2)+(n**2/L**2))  # Recalculando Frequência
    fig.suptitle('Freq = %f' % f, fontdict=font)
    # fig.text(2, 0.65, 'Freq = %f' % f, fontdict=font)
    Z = -(c * np.cos(np.pi * m * X / a) * np.cos(np.pi * n * Y / b) + d * np.cos(np.pi * p * X / a) * np.cos(
        np.pi * q * Y / b))  # Recalculando Z
    #Z = -(c * np.sin(np.pi * m * X / a) * np.sin(np.pi * n * Y / b) + d * np.sin(np.pi * n * X / a) * np.sin(
    #   np.pi * m * Y / b))
    draw(X, Y, Z)  # Plota com os novos valores


slider_m.on_changed(update)
slider_n.on_changed(update)
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_p.on_changed(update)
slider_q.on_changed(update)

reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(reset_ax, 'Reset', color=ax_color, hovercolor='0.975')


def reset(event):
    slider_m.reset()
    slider_n.reset()
    slider_a.reset()
    slider_b.reset()
    slider_c.reset()
    slider_d.reset()


button.on_clicked(reset)

plt.show()

