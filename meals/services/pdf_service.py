import pdfkit
#
# class ProductService:
#     def generate_pdf(self, parameters):
#         pdfkit.from_url('http://google.com', 'out.pdf')
from bottle import Bottle, template


class PdfService:
    def generate_pdf(self, meal):
        info = {'company_name': 'meal.code',
                'card_number': 'meal.card_number',
                'meal_name': meal.name,
                'recipe_number': 'meal.code',
                'notes': meal.notes,
                'describe': meal.describe,
                'storage': meal.storage,
                'serving': meal.serving,
                'expiry': meal.expiry,
                }

        result = template('/home/indre_segaloviciute/Saitynas/project/templates/sample2.html', info)
        result += self.generate_table(meal.products.all())
        result += template('/home/indre_segaloviciute/Saitynas/project/templates/footer1.html', info)
        print(result)
        pdfkit.from_string(result, 'outt.pdf')  # Is your requirement?
        # pdfkit.from_string('MicroPyramid', 'micro.pdf')

    def generate_table(self, products):
        info = {
            'name': 'REEEE',
            'bruto': 'Bruto',
            'neto': 'Neto',
            'proteins': 'Baltymai',
            'fats': 'Riebalai',
            'carbs': 'Angliavandeniai',
            'kcal': 'Kcal',
        }
        table = ''

        for product in list(products):
            info = {
                'name': product.name,
                'bruto': product.bruto,
                'neto': product.neto,
                'proteins': product.proteins,
                'fats': product.fats,
                'carbs': product.carbs,
                'kcal': product.kcal,
            }
            row = template('/home/indre_segaloviciute/Saitynas/project/templates/product1.html', info)

            table += row
        info = {
            'name': 'Viso',
            'bruto': '',
            'neto': '',
            'proteins': '',
            'fats': '',
            'carbs': '',
            'kcal': '',
        }
        table = template('/home/indre_segaloviciute/Saitynas/project/templates/product1.html', info)

        return table



