import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
df = pd.read_csv("data/world_population.csv")

# Reshape the dataframe: Convert year-based columns into rows
df_melted = df.melt(id_vars=["Country/Territory", "Continent"], 
                     value_vars=["2022 Population", "2020 Population", "2015 Population", 
                                 "2010 Population", "2000 Population", "1990 Population", 
                                 "1980 Population", "1970 Population"],
                     var_name="Year", value_name="Population")

# Convert "Year" column to proper format (extract numbers)
df_melted["Year"] = df_melted["Year"].str.extract(r'(\d+)').astype(int)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("World Population Analysis", style={'text-align': 'center'}),
    
    html.Label("Select a Continent:"),
    dcc.Dropdown(
        id="continent-dropdown",
        options=[{"label": c, "value": c} for c in df_melted["Continent"].unique()],
        value="Asia",  # Default selection
        clearable=False
    ),

    html.Label("Select a Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(y), "value": y} for y in sorted(df_melted["Year"].unique())],
        value=2022,  # Default selection
        clearable=False
    ),
    
    dcc.Graph(id="population-bar-chart"),
    dcc.Graph(id="population-trend-chart"),
])

# Define the callback function
@app.callback(
    [Output("population-bar-chart", "figure"),
     Output("population-trend-chart", "figure")],
    [Input("continent-dropdown", "value"),
     Input("year-dropdown", "value")]
)
def update_charts(selected_continent, selected_year):
    # Filter data for the selected year and continent
    filtered_df = df_melted[(df_melted["Year"] == selected_year) & 
                            (df_melted["Continent"] == selected_continent)]

    # Create bar chart (Population by Country)
    bar_fig = px.bar(
        filtered_df, 
        x="Country/Territory", 
        y="Population", 
        title=f"Population by Country in {selected_year} ({selected_continent})",
        labels={"Population": "Population", "Country/Territory": "Country"},
        height=500,
        color="Country/Territory"
    )

    # Filter data for population trends
    trend_df = df_melted[df_melted["Continent"] == selected_continent]

    # Create line chart (Population Trends Over Time)
    line_fig = px.line(
        trend_df, 
        x="Year", 
        y="Population", 
        color="Country/Territory",
        title=f"Population Trends in {selected_continent}",
        labels={"Population": "Population", "Year": "Year"},
        height=500
    )

    return bar_fig, line_fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
