#!/usr/bin/python3
#!/usr/bin/python3
"""
Flask application to generate a complete HTML page containing location 
and amenity dropdown menus and rental listings.
"""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/3-hbnb')
def display_hbnb():
    """Generate page with dropdown menu of states and cities"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('3-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)