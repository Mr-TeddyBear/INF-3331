import pandas as pd
from bokeh.plotting import figure, show, output_file



def assert_input(dataframe,month,start_year,end_year):
    assert month in list(dataframe), (f"Invalid month, valid month is and month of the year and starts with a capitol letter")

    assert start_year in list(dataframe.Year) and end_year in list(dataframe.Year), (
            f"Not valid year({start_year},{end_year}), valid years span from {dataframe.Year[0]} to {dataframe.Year.values[-1]}, {end_year & start_year in list(dataframe.Year.values)}")



def plot_temperature(month,dataframe,y_min=None,y_max=None,start_year=1816,end_year=2012):
    dataframe = pd.read_csv(dataframe, sep=',')
    return _plot(month,dataframe,y_min,y_max,start_year,end_year,'Temperature')


def plot_CO2(dataframe,month='Carbon',y_min=None,y_max=None,start_year=1816,end_year=2012):
    dataframe = pd.read_csv(dataframe, sep=',')
    return _plot(month,dataframe,y_min,y_max,start_year,end_year,'CO2')

def plot_CO2_country(dataframe,upper_thres,lower_thres,start_year='1990',end_year='2010'):
    dataframe = pd.read_csv(dataframe, sep=',')
    dataframe = (dataframe[dataframe.columns[:-4]].dropna())
    dataframe = dataframe.drop('Country Name',1)
    dataframe = dataframe.drop('Indicator Code',1)
    dataframe = dataframe.drop('Indicator Name',1)
    print(dataframe.values)
    dataframe = dataframe.loc[
        (dataframe.values > lower_thres) & (dataframe.values < upper_thres)
    ]

    plot = figure(plot_width=1000,plot_height=400,title='CO2 by country')
    plot.bar(dataframe['Country Code'],)


def _plot(month,dataframe,y_min,y_max,start_year,end_year,head):
    assert_input(dataframe,month,start_year,end_year)
    dataframe_slice = dataframe.loc[
        (dataframe.Year >= start_year) & (dataframe.Year <= end_year)]
    #dataframe_slice.plot(x=('Year'),y=(month))
    plot = figure(plot_width=600, plot_height=400,title=head)

    plot.line(dataframe_slice['Year'],dataframe_slice[month],line_width=2,legend=month)
    output_file('plot.html')

    if None not in (y_min, y_max):
        plot.yaxis.bound = (y_min,y_max)
    show(plot)
    return plot

if __name__ == "__main__":
    """
    data = pd.read_csv("co2.csv", sep = ',')
    plot_CO2('co2.csv',start_year=1850,end_year=1950)
    input('pause')
    plot_temperature('March','temperature.csv')
    """
    plot_CO2_country('CO2_by_country.csv',2,100)

