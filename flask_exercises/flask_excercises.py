from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        db = {}

        # POST /user - создание пользователя
        def create_user():
            json_data = request.get_json(force=True)
            name = json_data.get("name", "")
            if not name:
                return {"errors": {"name": "This field is required"}}, 422
            db[name] = {}
            return {"data": f"User {name} is created!"}, 201

        # GET /user/<name> - чтение пользователя
        def get_user(name):
            if name not in db:
                return {}, 404
            return {"data": f"My name is {name}"}, 200

        # PATCH /user/<name> - обновление пользователя
        def update_user(name):
            if name not in db:
                return {}, 404
            json_data = request.get_json(force=True)
            new_name = json_data.get("name")
            if new_name:
                db[new_name] = db.pop(name)
                return {"data": f"My name is {new_name}"}, 200
            return {"errors": {"name": "This field is required"}}, 422

        # DELETE /user/<name> - удаление пользователя
        def delete_user(name):
            if name not in db:
                return "", 404
            db.pop(name)
            return "", 204

        # Добавление URL маршрутов для каждого метода
        app.add_url_rule("/user", view_func=create_user, methods=["POST"])
        app.add_url_rule("/user/<name>", view_func=get_user, methods=["GET"])
        app.add_url_rule("/user/<name>", view_func=update_user, methods=["PATCH"])
        app.add_url_rule("/user/<name>", view_func=delete_user, methods=["DELETE"])
