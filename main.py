from flask import Flask, request, jsonify
from argostranslate import package, translate

app = Flask(__name__)

translator = None

@app.route('/translate', methods=['POST'])
def translate_text():
    global translator
    if not translator:
        package.install_from_path("path/to/your/argos/package")
        translator = translate.Translator.default()
        
    data = request.json
    source_lang = data.get('source_lang', 'en')
    target_lang = data.get('target_lang', 'es')
    text = data.get('text', '')

    try:
        translated_text = translator.translate(text, source_lang, target_lang)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
