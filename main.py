from routers import solicitudesRouter, usuariosRouter
import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.include_router(solicitudesRouter.router)
app.include_router(usuariosRouter.router)
@app.get("/")
async def home():
    salida = {"Bienvenido de vuelta señor Stark"}
    return salida

@app.on_event("startup")
async def startup():
    print("Conectandose teóricamente con una base de datos que no existe")

@app.on_event("shutdown")
async def shutdown():
    print("Cerrando")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", reload=True)