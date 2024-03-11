from . import app
from flask import render_template
import my_app.calculations
import my_app.visualization

csv_file = 'concentration.timeseries.csv'

@app.route('/')
def home():
    routes = [
        ('/get-mean', 'Returns the mean of the concentration'),
        ('/get-std-deviation', 'Returns the standard deviation of the concentration'),
        ('/get-sum', 'Returns the sum of the concentration'),
        ('/get-image', 'Returns PNG visualization of concentration')
    ]
    return render_template('index.html', routes=routes)

@app.route("/get-image")
def getImage():
    plot_image_encoded = my_app.visualization.getImage(csv_file)
    return render_template('get_image.html', plot_image_encoded=plot_image_encoded)

@app.route('/get-mean', methods=['GET'])
def concentration_mean():
    mean = my_app.calculations.get_mean(csv_file)
    
    if isinstance(mean, (float, int)):
        mean_str = str(mean)
        return render_template(
            "get_mean.html",
            mean_str=mean_str,
        )
    else:
        return render_template(
            "get_mean.html",
            error_message=mean,
        )

@app.route('/get-std-deviation', methods=['GET'])
def concentration_std_deviation():
    try:
        std_deviation_sample = my_app.calculations.get_std_deviation_sample(csv_file)
        std_deviation_pop = my_app.calculations.get_std_deviation_pop(csv_file)

        std_deviation_sample_str = str(std_deviation_sample) if isinstance(std_deviation_sample, (float, int)) else None
        std_deviation_pop_str = str(std_deviation_pop) if isinstance(std_deviation_pop, (float, int)) else None

        return render_template(
            "get_std_deviation.html",
            std_deviation_sample_str=std_deviation_sample_str,
            std_deviation_pop_str=std_deviation_pop_str,
            error_message=None
        )

    except (FileNotFoundError, ValueError) as e:
        return render_template(
            "get_std_deviation.html",
            std_deviation_sample_str=None,
            std_deviation_pop_str=None,
            error_message=str(e)
        )

    except Exception as e:
        return render_template(
            "get_std_deviation.html",
            std_deviation_sample_str=None,
            std_deviation_pop_str=None,
            error_message=f"An unexpected error occurred: {str(e)}"
        )

@app.route('/get-sum', methods=['GET'])
def concentration_sum():
    sum = my_app.calculations.get_sum(csv_file)
    
    if isinstance(sum, (float, int)):
        sum_str = str(sum)
        return render_template(
            "get_sum.html",
            sum_str=sum_str,
        )
    else:
        return render_template(
            "get_sum.html",
            error_message=sum_str,
        )
