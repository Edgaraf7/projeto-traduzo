from asyncio import start_server
from datetime import datetime
from flask import Flask, request, render_template
from controllers.admin_controller import admin_controller
from controllers.history_controller import history_controller
from models.history_model import HistoryModel
from src.models.language_model import LanguageModel
from deep_translator import GoogleTranslator


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")
app.register_blueprint(history_controller, url_prefix='/history')


@app.route("/", methods=['GET'])
def home():
    languages = LanguageModel.list_dicts()
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?"
    )


@app.route("/", methods=['POST'])
def translate_text():
    # Verifica se o parâmetro 'reverse' está presente na solicitação POST
    if 'reverse' in request.form:
        # Se estiver presente, trata-se de uma solicitação de reversão
        return reverse_translation()

    # Caso contrário, trata-se de uma solicitação normal de tradução
    text_to_translate = request.form['text-to-translate']
    translate_from = request.form['translate-from']
    translate_to = request.form['translate-to']

    translator = GoogleTranslator(source=translate_from, target=translate_to)
    translated_text = translator.translate(text_to_translate)

    # Salva o histórico da tradução
    history_record = HistoryModel({
        "text": text_to_translate,
        "translated_text": translated_text,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "timestamp": datetime.now()
    })
    history_record.save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text
    )


@app.route("/reverse", methods=['POST'])
def reverse_translation():
    text_to_translate = request.form['text-to-translate']
    translate_from = request.form['translate-from']
    translate_to = request.form['translate-to']

    translator = GoogleTranslator(source=translate_from, target=translate_to)
    translated_text = translator.translate(text_to_translate)

    original_text = text_to_translate
    text_to_translate = translated_text
    translated_text = original_text

    translate_from, translate_to = translate_to, translate_from

    # Salva o histórico da tradução
    history_record = HistoryModel({
        "text": text_to_translate,
        "translated_text": translated_text,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "timestamp": datetime.now()
    })
    history_record.save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text
    )


if __name__ == "__main__":
    start_server()
