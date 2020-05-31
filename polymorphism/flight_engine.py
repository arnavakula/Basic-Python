class Flight:
    def __init__(self, engine):
        self.engine = engine
    
    def start_engine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")

class BoingEngine:
    def start(self):
        print("Starting Boing Engine")
ae = AirbusEngine()
be = BoingEngine()
f_ae = Flight(ae)
f_be = Flight(be)

f_ae.start_engine()
f_be.start_engine() 

#+ is polymorphic as it works with different data types