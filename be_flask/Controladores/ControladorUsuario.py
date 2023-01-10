from Repositorios.RepositorioUsuario import RepositorioUsuario
from Modelos.Usuario import Usuario
class ControladorUsuario():
  def __init__(self):
      self.repositorioUsuario = RepositorioUsuario()

  def index(self):
      return self.repositorioUsuario.findAll()

  def create(self,infoUsuario):
      nuevoUsuario=Usuario(infoUsuario)
      return self.repositorioUsuario.save(nuevoUsuario)

  def show(self,id):
      elUsuario=Usuario(self.repositorioUsuario.findById(id))
      return elUsuario.__dict__

  def update(self,id,infoUsuario):
      usuarioActual=Usuario(self.repositorioUsuario.findById(id))
      usuarioActual.cedula=infoUsuario["cedula"]
      usuarioActual.nombre=infoUsuario["nombre"]
      usuarioActual.apellido=infoUsuario["apellido"]
      usuarioActual.hobbie=infoUsuario["hobbie"]
      return self.repositorioUsuario.save(usuarioActual)

  def delete(self,id):
      return self.repositorioUsuario.delete(id)
