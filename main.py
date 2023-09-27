from fastapi import FastAPI
from sqladmin import Admin
from router import base_router



def get_application(test: bool = False):
    application = FastAPI()
    application.include_router(base_router)
    setup_di(application)
    return application
    
def setup_di(application):    
    admin = Admin(
        application,
    )
    


app = get_application()




