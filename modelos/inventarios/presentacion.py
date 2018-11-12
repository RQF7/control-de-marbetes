"""
Modelo de presentación.
Control de marbetes.
Copyright (C) 2018 Ricardo Quezada.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import django
from .envase import Envase
from .producto import Producto
from .unidad import Unidad

class Presentacion (django.db.models.Model):

  envase = django.db.models.ForeignKey(
      'Envase',
      django.db.models.PROTECT,
      verbose_name = 'Envase de la presentación')

  unidad = django.db.models.ForeignKey(
      'Unidad',
      django.db.models.PROTECT,
      verbose_name = 'Unidad de medida para la capacidad de la presentación')

  capacidad = django.db.models.FloatField(
      verbose_name = 'Capacidad de la presentación',
      validators = [
        django.core.validators.MinValueValidator(0)])

  producto = django.db.models.ForeignKey(
      'Producto',
      django.db.models.PROTECT,
      verbose_name = 'Producto de la presentación')

  class Meta:
    unique_together = ('envase', 'unidad', 'capacidad', 'producto')

  def __str__ (ego):
    return "%s, %s, %s %d %s" % (ego.producto.marca,
        ego.producto,
        ego.envase,
        ego.capacidad,
        ego.unidad)

