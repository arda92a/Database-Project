import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import FuncFormatter
from PyQt6 import QtWidgets, QtCore
import warnings
import numpy as np

class GraphHelper:
    def __init__(self, graphics_view):
        self.graphics_view = graphics_view
        self.graph_methods = {
            'Bar Graph': self.draw_bar_graph,
            'Pie Chart': self.draw_pie_chart,
            'Line Graph': self.draw_line_graph
        }

    def setup_graph(self, graph_name=None):
        width = self.graphics_view.frameGeometry().width()
        height = self.graphics_view.frameGeometry().height()

        dpi = 100
        width_in_inches = width / dpi
        height_in_inches = height / dpi

        figure, ax = plt.subplots(figsize=(width_in_inches, height_in_inches))

        figure.patch.set_facecolor('#111010')
        ax.set_facecolor('#111010')

        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(colors='white')

        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        # Apply FuncFormatter only for specific graphs
        if graph_name in ['monthlyEnergyConsumptionStatistics', 'totalEnergyConsumptionStatistics']:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0f}'.format(x)))

        return figure, ax

    def draw_bar_graph(self, labels, values, graph_name):
        figure, ax = self.setup_graph(graph_name)

        if graph_name in ['dailyDeviceUsage', 'historicalDeviceUsage']:
            ax.barh(labels, values, color='#facc10')
        else:
            ax.bar(labels, values, color='#facc10')
            plt.xticks(rotation=15)

        self.adjust_layout_and_draw(figure, ax)

    def draw_pie_chart(self, labels, values, graph_name):
        figure, ax = self.setup_graph(graph_name)
        ax.pie(values, labels=labels, colors=['#facc10', '#a3acff', '#ffb3ff', '#90d595', '#e48381', '#aafbff'], textprops={'color':'white'})
        self.adjust_layout_and_draw(figure, ax)

    def draw_line_graph(self, labels, values, graph_name):
        figure, ax = self.setup_graph()
        ax.plot(labels, values, color='#facc10')
        plt.xticks(rotation=15)
        self.adjust_layout_and_draw(figure, ax)

    def adjust_layout_and_draw(self, figure, ax):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error", UserWarning)
                plt.tight_layout()
        except UserWarning:
            pass
    
        canvas = FigureCanvas(figure)
        scene = QtWidgets.QGraphicsScene()
        scene.addWidget(canvas)
        rect = self.graphics_view.viewport().rect()
        scene.setSceneRect(QtCore.QRectF(rect))
        self.graphics_view.setScene(scene)

        plt.close(figure)

    def draw_graph(self, labels, values, graph_type, graph_name=None):
        if not labels or not values:
            return
        if not np.any(values) or np.any(np.isnan(values)) or np.any(np.isinf(values)):
            return
        if not graph_type:
            return
        if graph_type in self.graph_methods:
            self.graph_methods[graph_type](labels, values, graph_name)
            plt.close('all')
        else:
            raise ValueError(f"Unsupported graph type: {graph_type}")