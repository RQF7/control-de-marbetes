"""
Modelo de una conversión entre unidades.
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
from .unidad import Unidad

class Conversion (django.db.models.Model):

  unidadUno = django.db.models.ForeignKey(
      'Unidad',
      django.db.models.PROTECT,
      verbose_name = 'Unidad de dominio')

  unidadDos = django.db.models.ForeignKey(
      'Unidad',
      django.db.models.PROTECT,
      verbose_name = 'Unidad de contradominio')

  def __str__ (ego):
    return "%s a %s" % (ego.unidadUno, ego.unidadDos)

