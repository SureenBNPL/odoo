# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    property_customer_type = fields.Selection(
            string='Customer Type',
            selection=[('tenant', 'Tenant'),
                       ('land_lord', 'Land Lord'), ],
            required=False, )


    # ---------------- | Tenant | ------------------


    authorizedPerson = fields.Char(
        string='Authorized Person',
        required=False)

    commercialNumber = fields.Char(
        string=' Commercial Number',
        required=False)

    nationalId = fields.Char(
        string='National Id',
        required=False)

    tenantMobile = fields.Char(
        string=' Mobile',
        required=False)

    # ---------------- | Land Lord | ------------------


    faalLicense = fields.Char(
        string='Faal License',
        required=False)

    landlordAuthorizedPerson = fields.Char(
        string='Authorized Person',
        required=False)

    landlordMobile = fields.Char(
        string='Mobile',
        required=False)


