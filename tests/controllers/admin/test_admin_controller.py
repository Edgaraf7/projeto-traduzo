# tests/controllers/admin/test_admin_controller.py

import json
from bson import ObjectId
from models.user_model import UserModel
from models.history_model import HistoryModel
from datetime import datetime

def test_history_delete(app_test):
    # Criação de um usuário admin para autenticação
    admin_user = UserModel({"name": "admin", "token": "valid_token"})
    admin_user.save()

    # Criação de um registro de histórico
    history_record = HistoryModel({
        "text": "Hello",
        "translated_text": "Olá",
        "translate_from": "en",
        "translate_to": "pt",
        "timestamp": datetime.now()
    })
    history_record.save()

    # Pegando o ID do registro criado
    history_id = str(history_record.data["_id"])

    # Fazendo a requisição DELETE
    response = app_test.delete(f"/admin/history/{history_id}", headers={
        "Authorization": "valid_token",
        "User": "admin",
    })

    # Verificando a resposta da exclusão
    assert response.status_code == 204

    # Verificando se o histórico foi realmente deletado
    assert HistoryModel.find_one({"_id": ObjectId(history_id)}) is None
