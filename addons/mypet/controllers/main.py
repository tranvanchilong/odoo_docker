import odoo
import logging
import json

_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    ... # code nhu tren

    @odoo.http.route(['/pet/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def pet_handler(self, dbname, id, **kw):
        model_name = "my.pet"
        try:
            print("a")
            registry = odoo.modules.registry.Registry(dbname)
            print(f"registry:{registry}")
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                print(f"env:{env}")
                rec = env[model_name].search([('id', '=', int(id))], limit=1)
                print(f"rec:{rec.name}")
                response = {
                    "status": "ok",
                    "content": {
                        "name": rec.name,
                        "nickname": rec.nickname,
                        "description": rec.description,
                        "age": rec.age,
                        "weight": rec.weight,
                        "dob": rec.dob.strftime('%d/%m/%Y'),
                        "gender": rec.gender,
                    }
                }
            print(json.dumps(response))
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)