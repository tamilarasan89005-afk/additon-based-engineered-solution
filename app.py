from flask import Flask, render_template, request

app = Flask(__name__)


class InvalidNumberError(Exception):
    """Custom exception for invalid inputs"""
    pass


def add_numbers(a, b):
    try:
        # Checking None or empty
        if a == "" or b == "":
            raise InvalidNumberError("Inputs cannot be empty")

        # Convert to float
        a = float(a)
        b = float(b)

        return a + b

    except ValueError:
        # User entered characters
        raise InvalidNumberError("Inputs must be valid numbers")

    except Exception as e:
        raise InvalidNumberError(str(e))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")

    try:
        result = add_numbers(num1, num2)
        return render_template("result.html", ans=result)

    except InvalidNumberError as e:
        return render_template("result.html", ans=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
