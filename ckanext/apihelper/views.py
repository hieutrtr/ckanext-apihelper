import logging
from flask import Blueprint
import ckan.plugins as p

log = logging.getLogger(__name__)
apihelper = Blueprint("apihelper", __name__)

def get_blueprints():
    return [apihelper]

@apihelper.route("/get")
def get():
    return p.toolkit.render('apihelper/index.html')
@apihelper.route("/create")
def create():
    return p.toolkit.render('apihelper/index.html')
@apihelper.route("/update")
def update():
    return p.toolkit.render('apihelper/index.html')
@apihelper.route("/delete")
def delete():
    return p.toolkit.render('apihelper/index.html')