from flask import Flask, request, render_template
from mira_sdk import MiraClient, Flow



client = MiraClient(config={"API_KEY": "sb-6d186ff04b4291932737f850d329bdd7"})

app = Flask(__name__)


def convert_to_normal_text(text):
    
    text = text.replace("**", "")  # Remove bold
    text = text.replace("*", "")  # Remove italics
    
    # Print the plain text
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-recommendation', methods=['POST'])
def get_recommendation():
     # Get the user input (drama genre)
    genre = request.form.get("genre")
    type = request.form.get("type")

    version = "1.0.0"
    input_data = {
    "type": type,
    "genre": genre
    }

    

    if version:
      flow_name = f"@harshal/drama-suggestion/{version}"
    else:
      flow_name = "@harshal/drama-suggestion"

    result = client.flow.execute(flow_name, input_data)
    
    return render_template('response.html', genre=genre, result=result['result'])

if __name__ == '__main__':
    app.run(debug=True,port=9000)






