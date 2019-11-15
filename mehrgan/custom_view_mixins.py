class ExpressiveListModelMixin:
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'status': 'ok', 'data': {self.plural_name: response.data}}
        return response
