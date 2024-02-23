# -*- coding: utf-8 -*-
from odoo import models, fields, api

# clase Coordinador
# nombre obligatorio
# apellidos obligatorio
# teléfono
# dirección
# DNI obligatorio
# espacios
# eventos
class gestion_eventos_coordinador(models.Model):
    _name = 'gestion_eventos.coordinador'
    
    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del coordinador")
    apellidos = fields.Char(string= "Apellidos", required=True, help="Introduce los apellidos del coordinador")
    tlf = fields.Char(string="Teléfono", help="Introduce el teléfono del coordinador")
    direccion = fields.Char(string="Dirección", help="Introduce la dirección del coordinador")
    dni = fields.Char(string="DNI", required=True, help="Introduce el DNI del coordinador")
    espacios = fields.One2many("gestion_eventos.espacio", "coordinador", string="Espacios")
    eventos = fields.One2many("gestion_eventos.evento", "coordinador", string="Eventos")

# clase Espacio
# nombre obligatorio
# dirección obligatorio
# teléfono de contacto
# descripción
# tipo obligatorio
# coordinador obligatorio
# eventos 
class gestion_eventos_espacio(models.Model):
    _name = 'gestion_eventos.espacio'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del espacio")
    direccion = fields.Char(string="Dirección", required=True, help="Introduce la dirección del espacio")
    tlf_contacto = fields.Char(string="Teléfono contacto", help="Introduce un teléfono para contactar con el propietario")
    descripcion = fields.Text(string="Descripción", help="Introduce una descripción del espacio")
    tipo = fields.Selection([('0','Abierto'),('1','Cerrado'),('2','Mixto')], string="Tipo", required=True, default="0")
    coordinador = fields.Many2one("gestion_eventos.coordinador", string="Coordinador", required=True, ondelete="cascade")
    eventos = fields.One2many("gestion_eventos.evento", "espacio", string="Eventos")

# clase Evento
# nombre obligatorio
# fecha obligatorio
# precio entrada
# aforo 
# ganancia 
# coordinador obligatorio
# espacio obligatorio
class gestion_eventos_evento(models.Model):
    _name = 'gestion_eventos.evento'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del evento")
    fecha = fields.Date(string="Fecha de celebración", required=True, help="Introduce la fecha en la que tendrá lugar el evento")
    precio_entrada = fields.Float(string="Precio", help="Introduce el precio de la entrada al evento")
    aforo = fields.Integer(string="Aforo", help="Introduce el aforo que va a tener el evento")
    ganancia = fields.Float(string="Ganancia total", compute="_ganancia", store=True)
    coordinador = fields.Many2one("gestion_eventos.coordinador", string="Coordinador", required=True, ondelete="cascade") 
    espacio = fields.Many2one("gestion_eventos.espacio", string="Espacio", required=True, ondelete="cascade")

    @api.depends('precio_entrada','aforo')
    def _ganancia(self):
        for r in self:
            r.ganancia = r.precio_entrada * r.aforo

# estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')], string="Estado", default="0")

# class gestion_eventos(models.Model):
#     _name = 'gestion_eventos.gestion_eventos'
#     _description = 'gestion_eventos.gestion_eventos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
