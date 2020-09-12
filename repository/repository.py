from django.forms.models import model_to_dict

class Repository:
    def __init__(self, model):
        self.model = model

    def list(self, parameters):
        return list(self.model.objects.filter(**parameters).values())

    def create(self, parameters):
        return self.model.objects.create(**parameters)

    def delete(self, object_id):
        self.model.objects.filter(id=object_id).delete()

    def update(self, object_id, parameters):
        self.model.objects.filter(id=object_id).update(**parameters)

    def read(self, parameters):
        try:
            return model_to_dict(self.model.objects.get(**parameters))
        except self.model.DoesNotExist as ex:
            pass