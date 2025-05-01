from abc import ABC, abstractmethod

# Interfaz base
class Documento(ABC):
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def editar(self, nuevo_contenido):
        pass

# Documento real con contenido editable
class DocumentoReal(Documento):
    def __init__(self, contenido):  
        self.contenido = contenido

    def mostrar(self):
        print("Contenido del documento:", self.contenido)

    def editar(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        print("El contenido ha sido actualizado correctamente.")

# Proxy que controla el acceso
class DocumentoProxy(Documento):
    def __init__(self, contenido, contraseña_lectura, contraseña_edicion):  
        self.documento_real = DocumentoReal(contenido)
        self.contraseña_lectura = contraseña_lectura
        self.contraseña_edicion = contraseña_edicion
        self.modo = None  # 'lectura' o 'edicion'

    def verificar_acceso(self):
        print("\nIntentando acceder al documento...")  # Mensaje inicial
        intento = input("Ingrese la contraseña: ")
        if intento == self.contraseña_edicion:
            self.modo = 'edicion'
            print("Acceso concedido: modo edición.")
            return True
        elif intento == self.contraseña_lectura:
            self.modo = 'lectura'
            print("Acceso concedido: modo lectura.")
            return True
        else:
            print("Acceso denegado: contraseña incorrecta.")
            return False

    def tiene_permiso_edicion(self):
        return self.modo == 'edicion'

    def mostrar(self):
        # Verificar acceso antes de mostrar el documento
        if self.modo is None and not self.verificar_acceso():
            print("No se puede mostrar el documento sin autenticación.")
            return
        self.documento_real.mostrar()

    def editar(self, nuevo_contenido):
        # Verificar acceso antes de editar
        if self.modo is None and not self.verificar_acceso():
            print("No se puede editar el documento sin autenticación.")
            return
        if self.tiene_permiso_edicion():
            self.documento_real.editar(nuevo_contenido)
        else:
            print("No tienes permiso para editar este documento.")

# Programa principal
if __name__ == "__main__":  
    doc = DocumentoProxy(
        contenido="Este es un documento confidencial.",
        contraseña_lectura="leer123",
        contraseña_edicion="editar123"
    )

    # Intentar mostrar el documento (requiere autenticación)
    doc.mostrar()

    # Solo ofrecer edición si tiene permiso
    if doc.modo is not None:  # Verificar si ya se autenticó
        if doc.tiene_permiso_edicion():
            editar = input("\n¿Deseas editar el documento? (sí/no): ")
            if editar.lower() == "sí":
                nuevo_contenido = input("Ingresa el nuevo contenido: ")
                doc.editar(nuevo_contenido)
        else:
            print("\nNo tienes permiso de edición. Solo puedes leer el documento.")
    else:
        print("\nAcceso denegado. No se puede continuar sin autenticación.")