import plotly.express as px
import pandas as pd

# Data
data = pd.DataFrame({
    "Season": ["Kharif", "Rabi", "Summer", "Autumn", "Winter"],
    "Production": [303, 444, 507, 300, 600]
})

# Bubble Plot
fig = px.scatter( data, x="Season", y="Production", size="Production", color="Season", title="Crop Production in India (2020)", 
                labels={"Production": "Production (in Tons)", "Season": "Season"}, template="plotly_white"
)

fig.update_layout(
    title_font=dict(size=24, family='Arial, sans-serif', color='black'),
    xaxis_title_font=dict(size=18, family='Arial, sans-serif', color='black'), yaxis_title_font=dict(size=18, family='Arial, sans-serif', color='black'),
    legend_title_font=dict(size=16, family='Arial, sans-serif', color='black'), font=dict(size=14, family='Arial, sans-serif', color='black'),
    margin=dict(l=40, r=40, t=80, b=40),
    paper_bgcolor='white', plot_bgcolor='white'
)

# Customizing the markers
fig.update_traces(marker=dict(line=dict(color='DarkSlateGrey', width=2)))

# Adding annotations
for i, row in data.iterrows():
    fig.add_annotation(
        x=row['Season'], y=row['Production'],
        text=str(row['Production']),
        showarrow=True, arrowhead=2,
        ax=0, ay=-30,
        font=dict(size=12, color='black', family='Arial, sans-serif')
    )

fig.show()
