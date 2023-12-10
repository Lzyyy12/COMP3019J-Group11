from apps import app
import logs, logging

if __name__ == "__main__":
    logs.log_config()
    logging.info('Recipe webapp startup')
    
    app.run(debug=True)