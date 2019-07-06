"""
main project function
"""
import os.path

from flask import Flask, render_template
from flaskr.lib import settings, global_variables
from flaskr.models import model_gh
from flaskr.controllers.controller_gh_webapp import CONTROLLER_GH_WEBAPP
# you can also import specific functions from a Blueprint module:
# from flaskr.controllers.common_functions import session_getter, branch_lister, file_lister
from flaskr.controllers.controller_gh_api import CONTROLLER_GH_API

# flask app starts here
APP = Flask(__name__)
APP.secret_key = os.environ['flask_secret_key']
APP.register_blueprint(CONTROLLER_GH_WEBAPP)
APP.register_blueprint(CONTROLLER_GH_API)


# github related variables
TOKEN = os.environ['github_token']

# init the github class
global_variables.OBJ = model_gh.Model(init_token=TOKEN,
                                      init_repo=settings.REPO)


@APP.route('/')
def index():
    """
    index route render template function
    :return:
    """
    return render_template('index.html',
                           template_current_branch=settings.INITIAL_BRANCH_NAME)


if __name__ == '__main__':
    APP.run(debug=True, host='127.0.0.1', threaded=True)
