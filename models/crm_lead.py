# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritLead(models.Model):
    _inherit = 'crm.lead'

    # ---------------- | Property | ------------------

    propertyType = fields.Selection(
        string='Property Type',
        selection=[('residential', 'Residential'),
                   ('commercial', 'Commercial'), ],
        required=False, )

    foundProperty = fields.Selection(
        string='Found Property',
        selection=[('yes', 'Yes'),
                   ('no', 'No'), ],
        required=False, )

    # ---------------- | Tenant | ------------------

    tenant_id = fields.Many2one(
        comodel_name='res.partner',
        string='Tenant',
        domain=[('property_customer_type', '=', 'tenant')],
        required=False
    )

    authorizedPerson = fields.Char(
        related='tenant_id.authorizedPerson',
        required=False)

    commercialNumber = fields.Char(
        related='tenant_id.commercialNumber',
        required=False)

    nationalId = fields.Char(
        related='tenant_id.nationalId',
        required=False)

    tenantMobile = fields.Char(
        related='tenant_id.tenantMobile',
        required=False)

    # ---------------- | Land Lord | ------------------
    landlord_id = fields.Many2one(
        comodel_name='res.partner',
        string='Land Lord',
        domain=[('property_customer_type', '=', 'land_lord')],
        required=False)

    faalLicense = fields.Char(
        related='landlord_id.faalLicense',
        required=False)

    landlordAuthorizedPerson = fields.Char(
        related='landlord_id.landlordAuthorizedPerson',
        required=False)

    landlordMobile = fields.Char(
        related='landlord_id.landlordMobile',
        required=False)


