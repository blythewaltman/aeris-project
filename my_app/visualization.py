import os
import io
import base64
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def getImage (filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, filename)
    # load csv into data frame
    df = pd.read_csv(csv_file_path)

    # extract csv columns
    z = df['z']
    y = df['y']
    x = df['x']
    concentration = df['concentration']

    # use the Agg backend
    plt.switch_backend('Agg')
    # create 3D scatter plot
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

    # scatter plot
    sc = ax.scatter(x, y, z, c=concentration, cmap='viridis', marker='o')

    # set axis labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Concentration Time Series')

    # color bar
    cbar = fig.colorbar(sc, ax=ax, label='Concentration')

    # save plot as png
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # free up resources
    plt.close(fig)

     # encode image as base64
    plot_image_encoded = base64.b64encode(output.getvalue()).decode('utf-8')

    return plot_image_encoded

