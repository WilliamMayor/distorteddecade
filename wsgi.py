import dd

app = dd.create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')