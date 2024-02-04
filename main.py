import json
import numpy as np
from engine import Engine
from body import Body
import plotly.graph_objects as go


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def main():
    engine = Engine()
    body = Body()
    engine.add_body(body)
    engine.add_body(Body({'position': [0, 50, 0]}))

    fig = go.Figure(data=go.Scatter(x=[0], y=[0], mode='markers'))
    fig.update_layout(title='Random Data Scatter Plot',
                      xaxis_title='time',
                      yaxis_title='position')

    for i in range(50):
        engine.simulate(0.1)

        for body in engine.bodies:
            fig.add_scatter(
                x=[i], y=[body.position[1]], mode='markers', marker_color='rgba(152, 0, 0, .8)')
            fig.add_scatter(
                x=[i], y=[body.velocity[1]], mode='markers', marker_color='rgba(255, 182, 193, .9)')

    fig.show()


if __name__ == "__main__":
    main()
