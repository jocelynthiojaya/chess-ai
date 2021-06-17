from endpoint.controllers import index

def register_all_blueprints(app):
    app.register_blueprint(index.bp)

    @app.errorhandler(404)  
    def page404(e):
        return "404"