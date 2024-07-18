from flask import Flask, render_template, request, redirect, url_for, session, flash
import ollama
import paraphraser

app = Flask(__name__)
app.secret_key = '🤠 replace this if you plan to use it comericially - SpectrixDev'

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        models_response = ollama.list()
        models = models_response.get('models', [])
        print("Models fetched:", models)
    except Exception as e:
        flash(f"An error occurred while fetching models: {str(e)}", "danger")
        models = []

    if request.method == 'POST':
        model_name = request.form['model']
        prompt = request.form['prompt']
        query = f"You are a writer. Write only about this: {prompt}"
        print(f"Selected model: {model_name}")
        print(f"Prompt: {prompt}")
        print(f"Query: {query}")
        
        try:
            response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': query}])
            essay = response['message']['content']
            print("Generated essay:", essay)
            session['original_essay'] = essay
            session['sentences'] = paraphraser.split_text_into_sentences(essay)
            session['current_index'] = 0
            session['rephrased_sentences'] = []
            print("Sentences:", session['sentences'])
            return redirect(url_for('confirm_paraphrase'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
            print(f"Error: {str(e)}")
            return redirect(url_for('index'))

    return render_template('index.html', models=models)

@app.route('/confirm_paraphrase', methods=['GET', 'POST'])
def confirm_paraphrase():
    if 'original_essay' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        return redirect(url_for('paraphrase'))

    original_essay = session['original_essay']
    return render_template('confirm_paraphrase.html', original_essay=original_essay)

@app.route('/paraphrase', methods=['GET', 'POST'])
def paraphrase():
    if'sentences' not in session:
        return redirect(url_for('index'))

    current_index = session.get('current_index', 0)
    sentences = session['sentences']
    rephrased_sentences = session.get('rephrased_sentences', [])

    if request.method == 'POST':
        rephrase = request.form['rephrase']
        rephrased_sentences.append(rephrase)
        session['rephrased_sentences'] = rephrased_sentences
        session['current_index'] = current_index + 1

        if current_index + 1 >= len(sentences):
            return redirect(url_for('done'))
        else:
            return redirect(url_for('paraphrase'))  # Redirect to the same route to show the next sentence

    if current_index < len(sentences):
        original_sentence = sentences[current_index]
    else:
        return redirect(url_for('done'))

    sentences_left = len(sentences) - current_index - 1
    return render_template('paraphrase.html', original_sentence=original_sentence, sentences_left=sentences_left)

@app.route('/done')
def done():
    rephrased_sentences = session.get('rephrased_sentences', [])
    rephrased_essay = ' '.join(rephrased_sentences)
    return render_template('done.html', rephrased_essay=rephrased_essay)

if __name__ == '__main__':
    app.run(debug=True)
