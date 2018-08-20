import baker


@baker.command
def run(host='0.0.0.0', port=None):
    """Runs the application on the local development server.
    """
    from webapp.app import app
    try:
        port = int(port) if port else None
    except (ValueError, TypeError):
        port = None
    app.run(host, port)


if __name__ == "__main__":
    baker.run()
