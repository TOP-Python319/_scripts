class Car:

    def set_values(self, model, engine, color):
        self.model = model
        self.engine = engine
        self.color = color

    
nissan = Car()
print(nissan.__dict__)
nissan.set_values("Juke", "1.6", "black")
print(nissan.__dict__)