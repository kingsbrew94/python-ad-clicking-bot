from components.structure import Struct 

class Timedouts(Struct):
    
    def __init__(self):
        super(Timedouts, self).__init__()
    
    def _set_fields(self, field_name: str):
        props = self.search_mdt(self.errors(), field_name)
        return self.get_element(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props
    
    def timeout(self):
        return self._set_fields('Timedout')