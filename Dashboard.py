# import pymongo
# import pandas as pd
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.graph_objects as go

# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
# db = client["Dashboard"]  # Replace with your database name
# collection = db["Schools"]  # Replace with your collection name

# # Fetch data from MongoDB
# data = list(collection.find())
# df = pd.DataFrame(data)

# # Convert categorical variables (1/2) into "Yes"/"No"
# categorical_vars = [
#     "Boundary Wall",
#     "Library Available",
#     "Separate Room for HM",
#     "Drinking Water Available",
#     "Playground Available",
#     "Electricity Availability",
#     "CWSN"
# ]

# df[categorical_vars] = df[categorical_vars].replace({1: "Yes", 2: "No"})

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Layout
# app.layout = html.Div(
#     style={"backgroundColor": "#f9f9f9", "padding": "20px"},
#     children=[
#         html.H1("School Infrastructure Dashboard", style={"textAlign": "center", "color": "#333"}),

#         # Dropdown for state filter
#         html.Label("Select State:", style={"color": "#333", "fontSize": "18px"}),
#         dcc.Dropdown(
#             id="state-dropdown",
#             options=[{"label": state, "value": state} for state in df["State"].unique()],
#             value=None,  # Default: All states
#             placeholder="Select a state to filter...",
#             style={"width": "50%", "marginBottom": "20px"}
#         ),

#         # Graph for categorical variables
#         dcc.Graph(id="categorical-bar-chart", style={"height": "80vh"})
#     ]
# )

# # Callback to update the bar chart based on the selected state
# @app.callback(
#     Output("categorical-bar-chart", "figure"),
#     [Input("state-dropdown", "value")]
# )
# def update_bar_chart(selected_state):
#     # Filter data based on state
#     filtered_df = df if not selected_state else df[df["State"] == selected_state]

#     # Ensure all categories ("Yes" and "No") exist for each variable
#     counts = {}
#     for var in categorical_vars:
#         value_counts = filtered_df[var].value_counts().to_dict()
#         counts[var] = {"Yes": value_counts.get("Yes", 0), "No": value_counts.get("No", 0)}

#     # Convert counts dictionary to a DataFrame
#     counts_df = pd.DataFrame(counts).T

#     # Create traces for "Yes" and "No"
#     yes_counts = counts_df["Yes"]
#     no_counts = counts_df["No"]

#     bar_chart = go.Figure()

#     bar_chart.add_trace(
#         go.Bar(
#             x=categorical_vars,
#             y=yes_counts,
#             name="Yes",
#             marker=dict(color="green"),
#             text=yes_counts,
#             textposition="auto"
#         )
#     )

#     bar_chart.add_trace(
#         go.Bar(
#             x=categorical_vars,
#             y=no_counts,
#             name="No",
#             marker=dict(color="red"),
#             text=no_counts,
#             textposition="auto"
#         )
#     )

#     # Update layout
#     bar_chart.update_layout(
#         title={
#             "text": f"Categorical Features {'for ' + selected_state if selected_state else ''}",
#             "x": 0.5,
#             "xanchor": "center"
#         },
#         barmode="group",
#         xaxis=dict(title="Features", tickangle=45, tickfont=dict(size=12)),
#         yaxis=dict(title="Number of Schools"),
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(255,255,255,0.9)",
#         font=dict(color="#333"),
#         legend=dict(title="Responses", orientation="h", x=0.5, xanchor="center", y=-0.2)
#     )

#     return bar_chart


# if __name__ == "__main__":
#     app.run_server(debug=True)

# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import pymongo
# import pandas as pd
# import plotly.express as px

# # MongoDB connection
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["Dashboard"]  # Replace with your database name
# collection = db["Schools"]  # Replace with your collection name

# # Fetch data from MongoDB
# data = list(collection.find({}, {"Grade Configuration": 1, "_id": 0}))

# # Preprocess the data: Group by grade configurations and count occurrences
# grade_configurations = [tuple(item["Grade Configuration"]) for item in data]
# df = pd.DataFrame(grade_configurations, columns=["Lower Class", "Upper Class"])
# df["Configuration"] = df.apply(lambda row: f"[{row['Lower Class']}, {row['Upper Class']}]", axis=1)
# config_counts = df["Configuration"].value_counts().reset_index()
# config_counts.columns = ["Configuration", "Count"]

# # Ensure the DataFrame is not empty
# if config_counts.empty:
#     raise ValueError("No grade configuration data found in the database!")

# # Dash App
# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("Grade Configuration Grouping", style={'textAlign': 'center'}),
#     dcc.Graph(id="grade-config-bar"),
#     html.Div("Filter by Minimum Count:", style={'textAlign': 'center'}),
#     dcc.Slider(
#         id="count-slider",
#         min=int(config_counts["Count"].min()),
#         max=int(config_counts["Count"].max()),
#         value=int(config_counts["Count"].min()),
#         marks={i: str(i) for i in range(int(config_counts["Count"].min()), int(config_counts["Count"].max()) + 1)},
#         step=1
#     )
# ])

# @app.callback(
#     Output("grade-config-bar", "figure"),
#     Input("count-slider", "value")
# )
# def update_bar_chart(min_count):
#     # Filter data based on the minimum count selected in the slider
#     filtered_df = config_counts[config_counts["Count"] >= min_count]

#     # Create the bar chart
#     fig = px.bar(
#         filtered_df,
#         x="Configuration",
#         y="Count",
#         title="Number of Schools by Grade Configuration",
#         labels={"Configuration": "Grade Configuration", "Count": "Number of Schools"},
#         color_discrete_sequence=["#636EFA"]
#     )

#     # Update layout for better visualization
#     fig.update_layout(
#         xaxis_title="Grade Configuration",
#         yaxis_title="Number of Schools",
#         template="plotly_white",
#         xaxis_tickangle=-45
#     )

#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)

import pymongo
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client["Dashboard"]  # Replace with your database name
collection = db["Schools"]  # Replace with your collection name

# Fetch data from MongoDB
data = list(collection.find())

# Prepare DataFrames
df = pd.DataFrame(data)

# Preprocessing Categorical Variables
categorical_vars = [
    "Boundary Wall",
    "Library Available",
    "Separate Room for HM",
    "Drinking Water Available",
    "Playground Available",
    "Electricity Availability",
    "CWSN"
]
if not df.empty:
    df[categorical_vars] = df[categorical_vars].replace({1: "Yes", 2: "No"})

# Grade Configurations
grade_configurations = [tuple(item["Grade Configuration"]) for item in data]
grade_df = pd.DataFrame(grade_configurations, columns=["Lower Class", "Upper Class"])
grade_df["Configuration"] = grade_df.apply(lambda row: f"[{row['Lower Class']}, {row['Upper Class']}]", axis=1)
config_counts = grade_df["Configuration"].value_counts().reset_index()
config_counts.columns = ["Configuration", "Count"]

# School Classification
classification_df = pd.DataFrame(list(collection.find({}, {"State": 1, "classification": 1, "_id": 0})))

# Student-to-Teacher Ratios
teacher_student_data = pd.DataFrame(
    list(collection.find({}, {"Total Teachers": 1, "Total Students": 1, "_id": 0}))
)
teacher_student_data["Student:Teacher Ratio"] = (
    teacher_student_data["Total Students"] / teacher_student_data["Total Teachers"]
).round(2)
bins = [0, 20, 30, 40, 50, 60, float('inf')]
labels = ["<20", "20-30", "30-40", "40-50", "50-60", ">60"]
teacher_student_data["Ratio Group"] = pd.cut(teacher_student_data["Student:Teacher Ratio"], bins=bins, labels=labels)
ratio_counts = teacher_student_data["Ratio Group"].value_counts().reset_index()
ratio_counts.columns = ["Ratio Group", "Count"]
ratio_counts = ratio_counts.sort_values("Ratio Group")

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "School Dashboard"

# Layout: All graphs in one tab
app.layout = html.Div([
    html.H1("School Dashboard", style={"textAlign": "center", "color": "#333"}),
    html.Div([
        # Dropdown for Categorical Bar Chart
        html.Label("Select State (Categorical Bar Chart):", style={"color": "#333", "fontSize": "18px"}),
        dcc.Dropdown(
            id="state-dropdown",
            options=[{"label": state, "value": state} for state in df["State"].unique()],
            value=None,
            placeholder="Select a state to filter...",
            style={"width": "50%", "marginBottom": "20px"}
        ),
        dcc.Graph(id="categorical-bar-chart", style={"height": "60vh"}),

        # Grade Configurations Heatmap
        html.H2("Grade Configurations Heatmap", style={"textAlign": "center", "marginTop": "40px"}),
        dcc.Graph(id="grade-config-heatmap", style={"height": "60vh"}),

        # Dropdown for School Classification Pie Chart
        html.Label("Select State (School Classification):", style={"color": "#333", "fontSize": "18px"}),
        dcc.Dropdown(
            id="state-filter",
            options=[{"label": state, "value": state} for state in classification_df["State"].unique()],
            placeholder="Select a state",
            multi=True,
            style={"width": "50%", "marginBottom": "20px"}
        ),
        dcc.Graph(id="classification-pie-chart", style={"height": "60vh"}),

        # Dropdown for Student-to-Teacher Ratios
        html.Label("Filter by Ratio Group:", style={"color": "#333", "fontSize": "18px"}),
        dcc.Dropdown(
            id="ratio-group-filter",
            options=[{"label": group, "value": group} for group in ratio_counts["Ratio Group"]],
            placeholder="Select a ratio group",
            style={"width": "50%", "marginBottom": "20px"}
        ),
        dcc.Graph(id="student-teacher-ratio-bar", style={"height": "60vh"})
    ])
])

# Callbacks
@app.callback(
    Output("categorical-bar-chart", "figure"),
    [Input("state-dropdown", "value")]
)
def update_bar_chart(selected_state):
    filtered_df = df if not selected_state else df[df["State"] == selected_state]
    counts = {}
    for var in categorical_vars:
        value_counts = filtered_df[var].value_counts().to_dict()
        counts[var] = {"Yes": value_counts.get("Yes", 0), "No": value_counts.get("No", 0)}
    counts_df = pd.DataFrame(counts).T
    yes_counts = counts_df["Yes"]
    no_counts = counts_df["No"]
    bar_chart = go.Figure()
    bar_chart.add_trace(go.Bar(x=categorical_vars, y=yes_counts, name="Yes", marker=dict(color="green"), text=yes_counts, textposition="auto"))
    bar_chart.add_trace(go.Bar(x=categorical_vars, y=no_counts, name="No", marker=dict(color="red"), text=no_counts, textposition="auto"))
    bar_chart.update_layout(
        title="Categorical Features",
        barmode="group",
        xaxis=dict(title="Features", tickangle=45),
        yaxis=dict(title="Number of Schools"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.9)"
    )
    return bar_chart

@app.callback(
    Output("grade-config-heatmap", "figure"),
    Input("grade-config-heatmap", "id")
)
def update_grade_heatmap(_):
    heatmap_df = grade_df.pivot_table(index="Lower Class", columns="Upper Class", aggfunc="size", fill_value=0)
    fig = px.imshow(
        heatmap_df,
        text_auto=True,
        labels={"color": "Count"},
        title="Grade Configurations Heatmap"
    )
    return fig

@app.callback(
    Output("classification-pie-chart", "figure"),
    Input("state-filter", "value")
)
def update_classification_pie_chart(selected_states):
    filtered_df = classification_df if not selected_states else classification_df[classification_df["State"].isin(selected_states)]
    classification_counts = filtered_df["classification"].value_counts().reset_index()
    classification_counts.columns = ["Classification", "Count"]
    fig = px.pie(classification_counts, names="Classification", values="Count", title="Odd vs Standard School Classification", color_discrete_sequence=px.colors.qualitative.Set2)
    return fig

@app.callback(
    Output("student-teacher-ratio-bar", "figure"),
    Input("ratio-group-filter", "value")
)
def update_ratio_horizontal_bar(selected_groups):
    filtered_data = ratio_counts if not selected_groups else ratio_counts[ratio_counts["Ratio Group"] == selected_groups]
    fig = px.bar(
        filtered_data,
        y="Ratio Group",
        x="Count",
        orientation="h",
        title="Horizontal Bar Plot: Student to Teacher Ratios",
        labels={"Ratio Group": "Student:Teacher Ratio", "Count": "Number of Schools"}
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)



