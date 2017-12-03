from .dataunits import compatible, convert_to_desired, within_espilon, IncompatibleUnitsError
    
class Input(object):
    self.__init__(self, value, unit):
        self.value = value
        self.unit = unit

class IntputReceivable(object):
    def __init__(self, receivable_unit):
        self.input_buffer = []
        self.receivable_units = receivable_unit

    def add_input(self, input):
        if not compatible(input.get_unit(), receivable_unit):
            raise IncompatibleUnitsError("Invalid input units: {} needed {}".format(input.get_unit(), receivable_unit))
        self.input_buffer.append(convert_to_desired(input, receivable_unit))

    def consume_input():
        self.input_buffer.pop(0)
