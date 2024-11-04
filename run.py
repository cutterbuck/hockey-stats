from package.app import app
from package.schedules import start_running_schedules


if __name__ == '__main__':
    start_running_schedules()
    # app.run_server(debug = True, dev_tools_ui = True, use_reloader = False, port=8060)

    from waitress import serve
    serve(app.server, host="0.0.0.0", port=8080)

