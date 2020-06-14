class Profesor():
    def __init__(self, materia,id, dia, horaI,horaF):
        self.materia = materia
        self.id = id
        self.dia = dia
        self.horaI = horaI
        self.horaF = horaF
    
    def getMateria(self):
        return self.materia
    
    def getId(self):
        return self.id
    
    def getDia(self):
        return self.dia
    
    def getHoraI(self):
        return self.horaI
    
    def getHoraF(self):
        return self.horaF
    
        