import plotly.express as px

def main():
    fig = px.scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13],
             labels={'x': 'X Axis', 'y': 'Y Axis'})
    fig.show()

if __name__ == "__main__":
    main()

# EOF
