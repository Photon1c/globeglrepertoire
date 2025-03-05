from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI API Key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ai_response', methods=['POST'])
def get_ai_response():
    data = request.get_json()
    prompt = data['prompt']

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    ai_response = response['choices'][0]['message']['content']
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)