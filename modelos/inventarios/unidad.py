"""
Modelo de unidad de medida.
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
from .magnitud import Magnitud

class Unidad (django.db.models.Model):

  nombre = django.db.models.CharField(
      verbose_name = 'Nombre de la unidad',
      unique = True)

  simbolo = django.db.models.CharField(
      verbose_name = 'Símbolo de la unidad',
      unique = True)

  magnitud = django.db.models.ForeignKey(
      'Magnitud',
      django.db.models.PROTECT,
      verbose_name = 'Magnitud de la unidad')

  def __str__ (ego):
    return "%s (%s)" % (ego.nombre, ego.simbolo)

