from flask import jsonify, request

from app.to_do import bp, core


@bp.route('/home', methods=['GET'])
def get_list():
    return jsonify({"data": "WORKING", "success": 1})


@bp.route('/gettodolist', methods=['GET'])
def get_todo_list():
    try:
        user_id = request.args['user_id']
        result = core.get_to_do_list(user_id)
        return jsonify({"data": result, "success": 1})
    except Exception as e:
        return jsonify({"message": "Invalid Request: request could not be processsed"})


@bp.route('/createtodotask', methods=['POST'])
def create_todo_task():
    try:
        user_id = request.args['user_id']
        task_subject = request.form['task_subject']
        task_description = request.form['task_description']
        task_due_date = request.form['task_due_date']
        task_status = request.form['task_status']
        task_labels = request.form['task_labels']
        result = core.create_todo_task(user_id, task_subject,
                                       task_description,
                                       task_due_date,
                                       task_status,
                                       task_labels)
        return jsonify({"data": result, "success": 1})
    except Exception as e:
        return jsonify({"message": "Invalid Request: request could not be processsed"})


@bp.route('/updatetodotask', methods=['POST'])
def update_todo_task():
    try:
        user_id = request.args['user_id']
        task_id = request.form['task_id']
        task_subject = request.form['task_subject']
        task_description = request.form['task_description']
        task_due_date = request.form['task_due_date']
        task_status = request.form['task_status']
        task_labels = request.form['task_labels']
        result = core.update_todo_task(user_id, task_id,
                                       task_subject,
                                       task_description,
                                       task_due_date,
                                       task_status,
                                       task_labels)
        return jsonify({"data": result, "success": 1})
    except Exception as e:
        return jsonify({"message": "Invalid Request: request could not be processsed"})


@bp.route('/deletetodotask', methods=['POST'])
def delete_todo_list():
    try:
        user_id = request.args['user_id']
        task_id = request.form['task_id']
        result = core.delete_todo_list(user_id, task_id)
        return jsonify({"data": result, "success": 1})
    except Exception as e:
        return jsonify({"message": "Invalid Request: request could not be processsed"})
