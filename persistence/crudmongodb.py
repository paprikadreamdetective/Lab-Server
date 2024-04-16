from .crud import Crud
from pymongo import MongoClient, database
from pymongo.errors import ServerSelectionTimeoutError

class crudMongoDB(Crud):
  def __init__(self, host: str, port: int) -> None:
    self.host = host
    self.port = port
    self.db = self.init_connection_db()

  def init_connection_db(self) -> (database.Database | None):
    try:
        client = MongoClient(self.host, self.port, ServerSelectionTimeoutError=5000) 
        print("Conexión a la base de datos establecida correctamente.")
        db = client['test']
        return db
    except ServerSelectionTimeoutError: 
        print("Error: No se pudo conectar a la base de datos.")
        return None
    
  def create_experiment(self, nombre, descripcion, fecha_inicio, fecha_fin) -> dict:
    experimento = {
      "nombre": nombre,
      "descripcion": descripcion,
      "fechaInicio": fecha_inicio,
      "fechaFin": fecha_fin
    }
    self.db.experimentos.insert_one(experimento)
    return experimento["_id"]

  def get_experiment(self, id):
    experimento = self.db.experimentos.find_one({"_id": id})
    return experimento
  
  def update_experiment(self, id, nombre, descripcion, fecha_inicio, fecha_fin):
    self.db.experimentos.update_one({"_id": id}, {"$set": {"nombre": nombre, "descripcion": descripcion, "fechaInicio": fecha_inicio, "fechaFin": fecha_fin}})

  def remove_experiment(self, id):
    self.db.experimentos.delete_one({"_id": id})

