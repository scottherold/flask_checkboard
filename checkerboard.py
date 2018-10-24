from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_colored_blocks():
    return render_template("index.html", block_cols=8, block_rows=8)

@app.route('/<x>/<y>')
def display_colored_blocks(x,y):
    xNum = int(x)
    yNum = int(y)
    return render_template("index.html", block_cols=xNum, block_rows=yNum)

if __name__ == "__main__":
    app.run(debug=True)