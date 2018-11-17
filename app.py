from bottle import Bottle, run, template
import io

app = Bottle()


def build_template(region, title):
    # NEED TO CREATE BUILD DIRECTORY IF IT DOESN'T EXIST!!!
    print("Building template for DNN")
    template_data = template('chart.html', region=region, title=title)
    # using Jinja2 string was fun, but let's get back to includes and other good stuff
    # html = Environment().from_string(tmpl.core_template).render(data=template_data)
    # html_minified = minify_html(html)
    file_name = f"opioid_mortality_{region}_pho.html"
    save_file_overwrite(template_data, file_name)
    pass


def save_file_overwrite(s_contents, s_name):
    print("Now in save file module")
    build_directory = 'build'
    with io.open(f"{build_directory}/{s_name}", "w+", encoding='utf8') as file:
        file.write(s_contents)
    print(f"File saved in {build_directory}: {s_name}")
    return


@app.route('/')
def index():
        region = "Hamilton"
        title = "City of Hamilton Public Health"
        return template('chart.html', region=region, title=title)


build_template("Hamilton", "City of Hamilton Public Health")
run(app, host='localhost', port=8081, debug=True)