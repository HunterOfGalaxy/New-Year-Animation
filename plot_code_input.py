import plotly.graph_objects as go

# Input Characteristics Data (VBE vs IB)
vbe = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
ib = [0, 0, 0, 0, 0, 0.1, 0.25, 0.5, 0.75, 1.5]

# Output Characteristics Data (VCE vs IC)
vce = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
ic = [0, 0.25, 0.75, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

# Input Characteristics Plot
input_fig = go.Figure()
input_fig.add_trace(go.Scatter(
    x=vbe, y=ib, mode='lines+markers', name='Input (VCE=0.4V)',
    marker=dict(size=8, color='blue'),
    line=dict(width=2)
))
input_fig.update_layout(
    title="Input Characteristics (VBE vs IB)",
    xaxis_title="VBE (V)",
    yaxis_title="IB (μA)",
    template="plotly_white",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)

# Output Characteristics Plot
output_fig = go.Figure()
output_fig.add_trace(go.Scatter(
    x=vce, y=ic, mode='lines+markers', name='Output (IB=50μA)',
    marker=dict(size=8, color='green'),
    line=dict(width=2)
))
output_fig.update_layout(
    title="Output Characteristics (VCE vs IC)",
    xaxis_title="VCE (V)",
    yaxis_title="IC (mA)",
    template="plotly_white",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)

# Show the plots
input_fig.show()
output_fig.show()
