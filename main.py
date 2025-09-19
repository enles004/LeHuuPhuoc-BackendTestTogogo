from src.api.app import create_app
import uvicorn

if "__main__" == __name__:
    app = create_app()
    uvicorn.run(app, log_level="info")
