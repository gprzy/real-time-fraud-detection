import os
import pandas as pd

from flask import (
    Flask,
    render_template,
    send_file
)


template_dir = os.path.abspath('./data_source/templates')
app = Flask(__name__, template_folder=template_dir)


data_path = './data_source/raw_data/creditcard.csv'
df = pd.read_csv(data_path)
shape = df.shape

@app.route('/')
def display_csv():
    table = df.sample(30).to_html()

    return render_template(
        template_name_or_list='display_csv.html', 
        table=table,
        shape=shape
    )


@app.route('/download')
def download():
    file_path = 'raw_data/creditcard.csv'
    response = send_file(
        file_path,
        mimetype='text/csv',
        as_attachment=True
    )

    response.headers['Content-Disposition'] = f'attachment; filename={file_path}'
    return response


if __name__ == '__main__':
    app.run(port=5001, debug=True)
