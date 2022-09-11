import matplotlib.pyplot as plt
import numpy as np

CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'

color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
              CB91_Purple, CB91_Violet]

key_colors = [x for x in plt.rcParams.keys()]
for k in key_colors:
    if 'color' in k:
        print(k)

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
plt.rcParams['axes.facecolor'] = '#120B27'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'

plt.rcParams['figure.facecolor'] = '#120B27'
plt.rcParams['figure.edgecolor'] = 'white'

plt.rcParams['xtick.color'] = 'darkgray'
plt.rcParams['xtick.labelcolor'] = 'darkgray'

plt.rcParams['ytick.color'] = 'lightgray'
plt.rcParams['ytick.labelcolor'] = 'lightgray'

plt.rcParams['legend.labelcolor'] = 'white'
plt.rcParams['grid.color'] = 'darkgray'


# plt.style.use('_mpl-gallery')

# make data
x1 = np.linspace(0, 10, 100)
y1 = 4 + 2 * np.sin(2 * x1)

x2 = np.linspace(0, 10, 100)
y2 = 8 + 2 * np.sin(2 * x2)

x3 = np.linspace(0, 10, 100)
y3 = 12 + 2 * np.sin(2 * x3)

x4 = np.linspace(0, 10, 100)
y4 = 6 + 2 * np.cos(2 * x4)

x5 = np.linspace(0, 10, 100)
y5 = 9 + 2 * np.cos(2 * x4)

data_dict = {
    'title': "TEST GRAPH 1234567890",
    'row_num': 2,
    'col_num': 2,
    'data': {
        '00': {
            'title': 'plot title 00',
            'label_x': 'XXXXX',
            'label_y': 'YYYYY',
            'data': {
                'line name 1': {
                    'x': x1,
                    'y': y1,
                    'linewidth': 0.1
                },
                'line name 2': {
                    'x': x2,
                    'y': y2,
                    'linewidth': 0.2
                },
                'line name 3': {
                    'x': x3,
                    'y': y3,
                    'linewidth': 0.3
                },
                'line name 4': {
                    'x': x4,
                    'y': y4,
                    'linewidth': 0.4
                },
                'line name 5': {
                    'x': x5,
                    'y': y5,
                    'linewidth': 0.5
                }
            }
        },
        '01': {
            'title': 'plot title 01',
            'label_x': 'XXXXX',
            'label_y': 'YYYYY',
            'data': {
                'line name 1': {
                    'x': x1,
                    'y': y1,
                    'linewidth': 0.1
                },
                'line name 2': {
                    'x': x2,
                    'y': y2,
                    'linewidth': 0.2
                },
                'line name 3': {
                    'x': x3,
                    'y': y3,
                    'linewidth': 0.3
                },
                'line name 4': {
                    'x': x4,
                    'y': y4,
                    'linewidth': 0.4
                },
                'line name 5': {
                    'x': x5,
                    'y': y5,
                    'linewidth': 0.5
                }
            }
        },
        '10': {
            'title': 'plot title 10',
            'label_x': 'XXXXX',
            'label_y': 'YYYYY',
            'data': {
                'line name 1': {
                    'x': x1,
                    'y': y1,
                    'linewidth': 0.1
                },
                'line name 2': {
                    'x': x2,
                    'y': y2,
                    'linewidth': 0.2
                },
                'line name 3': {
                    'x': x3,
                    'y': y3,
                    'linewidth': 0.3
                },
                'line name 4': {
                    'x': x4,
                    'y': y4,
                    'linewidth': 0.4
                },
                'line name 5': {
                    'x': x5,
                    'y': y5,
                    'linewidth': 0.5
                }
            }
        },
        '11': {
            'title': 'plot title 11',
            'label_x': 'XXXXX',
            'label_y': 'YYYYY',
            'data': {
                'line name 1': {
                    'x': x1,
                    'y': y1,
                    'linewidth': 0.1
                },
                'line name 2': {
                    'x': x2,
                    'y': y2,
                    'linewidth': 0.2
                },
                'line name 3': {
                    'x': x3,
                    'y': y3,
                    'linewidth': 0.3
                },
                'line name 4': {
                    'x': x4,
                    'y': y4,
                    'linewidth': 0.4
                },
                'line name 5': {
                    'x': x5,
                    'y': y5,
                    'linewidth': 0.5
                }
            }
        }
    }
}


def show_graph(graph_dict, fig_width=19.2, fig_height=10.8):

    row_num = graph_dict['row_num']
    col_num = graph_dict['col_num']

    fig, axes = plt.subplots(nrows=row_num, ncols=col_num, figsize=(fig_width, fig_height), tight_layout=True)

    if 'title' in graph_dict:
        title = graph_dict['title']
        fig.suptitle(title, color='yellow', fontsize=20)

    if 'data' in graph_dict:

        graph_data = graph_dict['data']
        for row in range(row_num):
            for col in range(col_num):
                ax = axes[row, col]
                plot_loc = f"{row}{col}"
                plot_dict = graph_data[plot_loc]

                if 'title' in plot_dict:
                    plot_title = plot_dict['title']
                    ax.set_title(f"{plot_title}", color='white', fontsize=18)
                if 'label_x' in plot_dict:
                    plot_label_x = plot_dict['label_x']
                    ax.set_xlabel(f"{plot_label_x}", color='white', fontsize=12)
                if 'label_y' in plot_dict:
                    plot_label_y = plot_dict['label_y']
                    ax.set_ylabel(f"{plot_label_y}", color='white', fontsize=12)

                ax.tick_params('x', direction='in')
                ax.tick_params('y', direction='in')
                # ax.grid(True)


                if 'data' in plot_dict:
                    plot_data = plot_dict['data']
                    for line_name, line_data_dict in plot_data.items():
                        x = line_data_dict['x']
                        y = line_data_dict['y']
                        linewidth = line_data_dict['linewidth']
                        ax.plot(x, y, linewidth=linewidth, label=line_name)
                ax.legend(loc='upper right')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['bottom'].set_visible(True)
                ax.spines['left'].set_visible(True)

                # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                #        ylim=(0, 8), yticks=np.arange(1, 8))

    # plt.legend(frameon=False)

    plt.tight_layout()
    plt.show()

show_graph(graph_dict=data_dict)
