# -*- coding: utf-8 -*-

import units.predefined
from units import unit, named_unit, scaled_unit, si_prefixed_unit
from units.quantity import Quantity
from units.compatibility import compatible as strictly_compatible, within_epsilon
from units.exception import IncompatibleUnitsError

def no_converter(_ignored):
    raise IncompatibleUnitsError("No known conversion between classes")

class RelatedUnitConveter(object):
    RELATIONSHIPS = {}

    @staticmethod
    def get_converter(source_unit, target_unit):
        return RelatedUnitConveter.RELATIONSHIPS.get((source_unit.canonical(), target_unit.canonical()))

    def __init__(self, source_unit, target_unit, forward_converter=no_converter, backward_converter=no_converter):
        self.source_unit = source_unit
        self.target_unit = target_unit
        self.key = (source_unit.canonical(), target_unit.canonical())
        self.reverse_key = tuple(reversed(self.key))
        self.forward_converter = forward_converter or no_converter
        self.backward_converter = backward_converter or no_converter
        if self.key not in self.RELATIONSHIPS and forward_converter is not None:
            self.RELATIONSHIPS[self.key] = self
        if self.reverse_key not in self.RELATIONSHIPS and backward_converter is not None:
            self.invert() # Will auto-register

    def translate(self, source_quantity, target_unit=None):
        if not isinstance(source_quantity, Quantity):
            source_quantity = Quantity(source_quantity, self.source_unit)
        target_unit = target_unit or self.target_unit
        converter_source_quantity = strict_convert_to_unit(source_quantity, self.source_unit)
        converter_target_quantity = Quantity(self.forward_converter(converter_source_quantity), self.target_unit)
        target_quantity = strict_convert_to_unit(converter_target_quantity, target_unit)
        return target_quantity

    def invert(self):
        return RelatedUnitConveter(self.target_unit, self.source_unit, self.backward_converter, self.forward_converter)

def related_unit_converter(source_unit, target_unit, forward_converter=None, backward_converter=None):
    converter = RelatedUnitConveter.get_converter(source_unit, target_unit)
    if converter:
        return converter
    if forward_converter is None and backward_converter is None:
        return None
    return RelatedUnitConveter(source_unit, target_unit, forward_converter=forward_converter, backward_converter=no_converter)

units.predefined.define_units()

"""Temperature units."""
celcius = unit(u'°C') # Celsius
ferenheit = unit(u'°F') # Ferenheit
related_unit_converter(ferenheit, celcius, lambda f: (f - 32) * 5.0 / 9.0, lambda c: (c * 9.0 / 5.0) + 32)

def compatible(unit1, unit2):
    if strictly_compatible(unit1, unit2):
        return True
    return related_unit_converter(unit1, unit2) is not None

def strict_convert_to_unit(quantity, target_unit):
    if not isinstance(quantity, Quantity):
        IncompatibleUnitsError("No units defined for conversion")
    return target_unit(quantity / target_unit(1.0))

def convert_to_unit(quantity, target_unit):
    if not isinstance(quantity, Quantity):
        IncompatibleUnitsError("No units defined for conversion")
    try:
        return strict_convert_to_unit(quantity, target_unit)
    except IncompatibleUnitsError as e:
        try:
            converter = related_unit_converter(quantity.unit, target_unit)
            if not converter:
                raise e
            return converter.translate(quantity, target_unit)
        except IncompatibleUnitsError:
            raise e
