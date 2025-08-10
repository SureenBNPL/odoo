# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class RealEstateAPI(http.Controller):
    """
    This Controller For Lead
    - Submit Lead
    """

    @http.route('/leads', type='json', auth='public', csrf=False, method=['POST'],cors='*')
    def submit_lead(self, **kwargs):
        """
            Get The Lead From Portal
            And Create Contact ' Tenant And landlord '
            And After That Create Lead
        """
        try:
            data = kwargs or {}

            # ---------------- | Extract all fields | ----------------
            tenant_name = data.get("tenantName")
            authorized_person = data.get("authorizedPerson")
            tenant_mobile = data.get("tenantMobile")
            commercial_number = data.get("commercialNumber", "")
            national_id = data.get("nationalId", "")

            landlord_name = data.get("landlordName")
            landlord_authorized_person = data.get("landlordAuthorizedPerson")
            landlord_mobile = data.get("landlordMobile")
            faal_license = data.get("faalLicense")

            property_type = data.get("propertyType")
            found_property = data.get("foundProperty")
            yearly_rent = data.get("yearlyRent")



            # ---------------- | Validate fields | ----------------
            required_fields = {
                "tenantName": tenant_name,
                "authorizedPerson": authorized_person,
                "tenantMobile": tenant_mobile,
                "landlordName": landlord_name,
                "landlordAuthorizedPerson": landlord_authorized_person,
                "landlordMobile": landlord_mobile,
                "faalLicense": faal_license,
                "propertyType": property_type,
                "foundProperty": found_property,
                "yearlyRent": yearly_rent,
            }



            for field_name, value in required_fields.items():
                if not value:
                    return {
                        "status": "Error",
                        "message": f"Missing required field: {field_name}"
                    }

            env = request.env

            # ---------------- | Check/Create Tenant | ----------------
            tenant = env['res.partner'].sudo().search([
                ('nationalId', '=', national_id),
                ('tenantMobile', '=', tenant_mobile),
                ('commercialNumber', '=', commercial_number),
                ('property_customer_type', '=', 'tenant')
            ], limit=1)

            if not tenant:
                tenant = env['res.partner'].sudo().create({
                    "name": tenant_name,
                    "property_customer_type": "tenant",
                    "authorizedPerson": authorized_person,
                    "commercialNumber": commercial_number,
                    "nationalId": national_id,
                    "tenantMobile": tenant_mobile,
                    "phone": tenant_mobile,
                })

            # ---------------- | Check/Create Landlord | ----------------
            landlord = env['res.partner'].sudo().search([
                ('faalLicense', '=', faal_license),
                ('landlordMobile', '=', landlord_mobile),
                ('property_customer_type', '=', 'land_lord')
            ], limit=1)

            if not landlord:
                landlord = env['res.partner'].sudo().create({
                    "name": landlord_name,
                    "property_customer_type": "land_lord",
                    "faalLicense": faal_license,
                    "landlordAuthorizedPerson": landlord_authorized_person,
                    "landlordMobile": landlord_mobile,
                    "phone": landlord_mobile,
                })

            # ---------------- | Create Lead | ----------------
            lead = env['crm.lead'].sudo().create({
                "name":f'{property_type} - {tenant.name} - {landlord.name}',
                "propertyType": property_type,
                "foundProperty": found_property,
                "expected_revenue": yearly_rent,
                "tenant_id": tenant.id,
                "landlord_id": landlord.id,
            })

            return {
                "status": "Success",
                "message": "Lead created successfully.",
                "data": {
                    "lead_id": lead.id,
                    "tenant_id": tenant.id,
                    "landlord_id": landlord.id
                }
            }

        except Exception as e:
            return {
                "status": "Error",
                "message": f"Unhandled error: {str(e)}"
            }
