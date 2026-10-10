import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db, AdminUser
from routes.auth_routes import auth_bp
from routes.registration_routes import registration_bp
from routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS for local frontend
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(registration_bp)
    app.register_blueprint(admin_bp)

    # Health Check API
    @app.route('/api/health', methods=['GET'])
    def health_check():
        try:
            db.session.execute(db.text('SELECT 1'))
            db_status = "connected"
        except Exception as e:
            db_status = f"disconnected: {str(e)}"

        return jsonify({
            'status': 'ok',
            'message': 'Smart Registration Portal Backend API is running.',
            'database': db_status
        }), 200

    # Error Handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Endpoint not found.'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal server error occurred.'
        }), 500

    # Auto Create Tables & Initial Admin on Startup
    with app.app_context():
        try:
            db.create_all()
            admin_user = db.session.get(AdminUser, 1) or AdminUser.query.filter_by(username=app.config['ADMIN_USERNAME']).first()
            if not admin_user:
                admin_user = AdminUser(username=app.config['ADMIN_USERNAME'])
                admin_user.set_password(app.config['ADMIN_PASSWORD'])
                db.session.add(admin_user)
                db.session.commit()
                print(f"[INIT] Created default admin account: {app.config['ADMIN_USERNAME']}")
        except Exception as e:
            print(f"[INIT ERROR] Failed to initialize database tables: {e}")

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[SERVER] Smart Registration Portal Backend running on http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
