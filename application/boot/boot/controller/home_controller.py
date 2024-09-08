from pweb import Blueprint
from pweb_form_rest import ssr_ui_render

url_prefix = "/"
home_controller = Blueprint(
    "home_controller",
    __name__,
    url_prefix=url_prefix
)


@home_controller.route("/", methods=['GET'])
def index():
    return ssr_ui_render(view_name="home/index")

@home_controller.route("/table", methods=['GET'])
def table():
    return ssr_ui_render(view_name="home/html-table")


@home_controller.route("/allInput", methods=['GET'])
def allInput():
    return ssr_ui_render(view_name="home/html-from-all-input")

@home_controller.route("/aboutMe", methods=['GET'])
def aboutMe():
    return ssr_ui_render(view_name="home/aboutMe")
