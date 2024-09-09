from odoo import fields,models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Estate(models.Model):
    _name = "estate"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    fecha = datetime.today()+relativedelta(months=3)
    date_availability = fields.Date(name="Availability",default=fecha,copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east','East'),('west','West')],
        help="Orientation of the view in the garden")
    active=fields.Boolean(default=False)
    state=fields.Selection(
        string="State",
        selection=[("new","New"),("offer_received","Offer Received"),("offer_accepted","Offer Accepted"),("sold","Sold"),("canceled","Canceled")],
        default="new",
        required=True,
        copy=False)
    