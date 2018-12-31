"""
Script de Selenium para automatizar la interacción con la página del SAT.

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

import json
import selenium.webdriver
import selenium.webdriver.common.by
import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.ui
import time


def esperar_a_servidor(navegador):
    """"""
    selenium.webdriver.support.ui.WebDriverWait(navegador, 60).until(
        selenium.webdriver.support.expected_conditions
            .invisibility_of_element_located((
                selenium.webdriver.common.by.By.ID,
                'formRegistroGeneral:retroalimentacionView:j_idt11')))
    return


if __name__ == '__main__':

    # Carga inicial desde trámites y servicios
    navegador = selenium.webdriver.Firefox()
    navegador.get('https://www.sat.gob.mx/tramites/67622/' +
                  'registro-de-uso-de-marbetes-obtenidos,' +
                  '-utilizados,-destruidos-e-inutilizados-')
    navegador.find_element_by_link_text('INICIAR').click()

    # Autentificación con firma electrónica
    for manejador in navegador.window_handles:
        navegador.switch_to.window(manejador)
    selenium.webdriver.support.ui.WebDriverWait(navegador, 60).until(
        selenium.webdriver.support.expected_conditions
        .presence_of_element_located(
            (selenium.webdriver.common.by.By.ID, 'privateKeyPassword')))

    # Esperar hasta estar en aplicación de java server faces
    selenium.webdriver.support.ui.WebDriverWait(navegador, 60).until(
        selenium.webdriver.support.expected_conditions.url_to_be(
            'https://agaff.siat.sat.gob.mx' +
            '/PTSC/marbetes/faces/pages/registro/registroUso.jsf'))

    # Referencias a elementos de formulario
    #selector_de_origen = selenium.webdriver.support.ui.Select(
    #    navegador.find_element_by_id(
    #        'formRegistroGeneral:retroalimentacionView:' +
    #        'cmbOrigen_input'))

    # Cargar archivo de datos))
    datos = json.load(open('datos.json'))
    numero_actual = datos['numero_inicial']
    print("Retroalimentación de marbetes")
    print("Serie", datos['serie'])
    print("Número inicial", datos['numero_inicial'])
    print("Fecha", datos['fecha'])
    print("")

    # Introducir rangos de marbetes
    for rango in datos['rangos']:
        print(rango['clave'], rango['lote'], rango['cantidad'], sep='; ')

        #contenedor_de_selector_de_producto = navegador.find_element_by_id(
        #        'formRegistroGeneral:retroalimentacionView:' +
        #        'cmbClaveProducto_input')
        #contenedor_de_selector_de_producto.click()
        selector_de_producto = selenium.webdriver.support.ui.Select(
            navegador.find_element_by_id(
                'formRegistroGeneral:retroalimentacionView:' +
                'cmbClaveProducto_input'))
        selector_de_producto.select_by_visible_text(rango['clave'])
        esperar_a_servidor(navegador)

        #selector_de_origen.select_by_visible_text(
        #    'ESTADOS UNIDOS MEXICANOS')

        # Fecha
        #entrada_de_fecha = navegador.find_element_by_id(
        #    'formRegistroGeneral:retroalimentacionView:' +
        #    'calFechaEnvasado_input')
        #entrada_de_fecha.send_keys('')
        #esperar_a_servidor(navegador)
        #entrada_de_fecha = navegador.find_element_by_id(
        #    'formRegistroGeneral:retroalimentacionView:' +
        #    'calFechaEnvasado_input')
        #entrada_de_fecha.send_keys(datos['fecha'])
        #esperar_a_servidor(navegador)

        # Lote
        entrada_de_lote = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtLoteProduccion')
        entrada_de_lote.send_keys('')
        esperar_a_servidor(navegador)
        entrada_de_lote = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtLoteProduccion')
        entrada_de_lote.send_keys(rango['lote'])
        esperar_a_servidor(navegador)

        # Serie
        entrada_de_serie = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtSerie')
        entrada_de_serie.send_keys('')
        esperar_a_servidor(navegador)
        entrada_de_serie = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtSerie')
        entrada_de_serie.send_keys(datos['serie'])
        esperar_a_servidor(navegador)

        # Rango inicial
        entrada_rango_inicial = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtFolioDesde')
        entrada_rango_inicial.send_keys('')
        esperar_a_servidor(navegador)
        entrada_rango_inicial = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtFolioDesde')
        entrada_rango_inicial.send_keys(str(numero_actual))
        numero_actual += rango['cantidad'] - 1
        esperar_a_servidor(navegador)

        # Rango final
        entrada_rango_final = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtFolioHasta')
        entrada_rango_final.send_keys('')
        esperar_a_servidor(navegador)
        entrada_rango_final = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'txtFolioHasta')
        entrada_rango_final.send_keys(str(numero_actual))
        numero_actual += 1
        esperar_a_servidor(navegador)

        # Guardar rango
        boton_guardar_rango = navegador.find_element_by_id(
            'formRegistroGeneral:retroalimentacionView:' +
            'btnAgregarFolioListaRetro')
        boton_guardar_rango.click()
        esperar_a_servidor(navegador)
