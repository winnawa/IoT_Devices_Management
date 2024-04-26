from app.devices import bp

@bp.route('/')
def index():
    return 'This is The Devices Blueprint'