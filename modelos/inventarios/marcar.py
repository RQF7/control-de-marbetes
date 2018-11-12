"""
Modelo de marca.
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

class Marca (django.db.models.Model):

  nombre = django.db.models.CharField(
      verbose_name = 'Nombre de la marca',
      unique = True)

  def __str__ (ego):
    return ego.nombre
