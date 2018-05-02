from flask import Flask, make_response, request, render_template
from temperature_CO2_plotter import *
from bokeh.embed import components
app = Flask(__name__)


@app.route("/", methods=['GET'])
def input():
    #response = r
    """
    <!DOCTYPE = html>
   <html>
    <body>
        <center>
        <h1>Temperature</h1>
        <p1>
        Temperature plot options<br/>
        <select>
            <option value="January">January</option>
            <option value="Febuary">Febuary</option>
            <option value="March">March</option>
            <option value="April">April</option>
            <option value="May">May</option>
            <option value="June">June</option>
            <option value="July">July</option>
            <option value="August">August</option>
            <option value="September">September</option>
            <option value="Oktober">Oktober</option>
            <option value="November">November</option>
            <option value="December">December</option>
        </select>
        <form>
            <input type="text" name="start_year_temp" placeholder="First year(eks. 1820)"><br>
            <input type="text" name="end_year_temp" placeholder="Last year(eks. 1900)"><br>
        </form>
        <img src="static/temp.png">

        </p1>

        <h2>CO2</h2>
        <p2>
        CO2 plot options
        <form>
            <input type="text" name="start_year_co2" placeholder="First year"><br>
            <input type="text" name="end_year_co2" placeholder="Last year"><br>
        </form>

        <img src="static/co2.png">

        </p2>

        <from>
            <input type="submit" name="Redraw plots" value="Redraw plots">
        </from>
        </center>
    </body>
    <html>
    """
#    print (request.form)
    start_year,end_year = (request.args.get('start_year')),(request.args.get('end_year'))
    print ("stuff is happeing",start_year,type(end_year))
    if start_year == None or len(start_year) == 0:
        start_year = 1816
    else:
        start_year = eval(start_year)
    if end_year == None or len(end_year) == 0:
        end_year = 2012
    else:
        end_year = eval(end_year)

    current_month = request.args.get('feature_name')
    if current_month == None:
        current_month = 'January'
    all_months = [
            'January','Febuary','March','April','May','June','July','August','September','October','November','December']

    temp_plot = plot_temperature(current_month,'temperature.csv',start_year=start_year,end_year=end_year)

    temp_script, temp_div = components(temp_plot)
    print (temp_div)
    temp_rendr = render_template('plot_template.html',script=temp_script,div=temp_div,current_feature=current_month,feature_names=all_months)

    co2_plot = plot_CO2('co2.csv','Carbon',start_year=start_year,end_year=end_year)

    co2_script, co2_div = components(co2_plot)

    co2_rendr = render_template('plot_co2_template.html',script=co2_script,div=co2_div,current_feature='Carbon')

    #plotting(month,start_yearco2,start_year_temp,end_year_co2,end_year_temp,y_min,y_max)
    return co2_rendr,temp_rendr
def plotting(month,start_year_co2,start_year_temp,end_year_co2,end_year_temp,y_min,y_max):

    plot_temperature(month,'temperature.csv',)
    plt.savefig('static/temp.png')
    plot_CO2('co2.csv',month)
    plt.savefig('static/co2.png')







if __name__ == "__main__":
    app.run(debug=True)
