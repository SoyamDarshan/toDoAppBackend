from app.authentication import bp
#
# @bp.route('/login', methods=['GET'])
# def login():
#     try:
#         user_id = request.form['user_id']
#         result = core.get_to_do_list(user_id)
#         return jsonify({"data": result, "success": 1})
#     except Exception as e:
#         return jsonify({"message": "Invalid Request: request could not be processsed"})
#
#
# @bp.route('/logout', methods=['GET'])
# def logout():
#     try:
#         user_id = request.args['user_id']
#         result = core.get_to_do_list(user_id)
#         return jsonify({"data": result, "success": 1})
#     except Exception as e:
#         return jsonify({"message": "Invalid Request: request could not be processsed"})
#
#
# @bp.route('/registration', methods=['GET'])
# def registration():
#     try:
#         user_id = request.args['user_id']
#         result = core.get_to_do_list(user_id)
#         return jsonify({"data": result, "success": 1})
#     except Exception as e:
#         return jsonify({"message": "Invalid Request: request could not be processsed"})
