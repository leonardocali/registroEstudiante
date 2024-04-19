class Singleton:
    instancias = {}
    
    def __new__(cls, *args,**kwargs):

        if cls not in cls.instancias:
            cls.instancias[cls] = super().__new__(cls)
        
        return cls.instancias[cls]