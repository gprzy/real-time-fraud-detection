import os
import pandas as pd

from flask import (
    Flask,
    render_template
)


template_dir = os.path.abspath('./online_payments/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def display_csv():
    return render_template(
        template_name_or_list='page.html'
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True)
