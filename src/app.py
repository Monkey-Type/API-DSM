from app import create_app, create_database
import os

app = create_app()
db = create_database(app)


if __name__ == "__main__":
    app.run(debug=True)
    db.run()
