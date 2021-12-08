from config import AppConfig
from main import create_app

app = create_app(AppConfig)

if __name__ == '__main__':
    app.run()