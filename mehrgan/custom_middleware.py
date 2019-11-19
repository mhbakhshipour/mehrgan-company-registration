from django.http import QueryDict
from django.utils.html import strip_tags

from mehrgan import settings


def input_sanitizer_middleware(get_response):
    def convert_input_data(data):
        new_query_dict = QueryDict('', mutable=True)
        for key, values in data.items():
            if key not in settings.WHITELIST_STRIP_TAG_PARAMETERS:
                for value in values:
                    new_query_dict.appendlist(key, strip_tags(value))
        return new_query_dict

    def strip_tag_http_data(request, attribute):
        data = dict(getattr(request, attribute))
        new_query_dict = convert_input_data(data)
        new_query_dict._mutable = False
        setattr(request, attribute, new_query_dict)

    def middleware(request):
        url = request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
        if 'admin' not in url:
            strip_tag_http_data(request, 'POST')
            strip_tag_http_data(request, 'GET')
        response = get_response(request)

        return response

    return middleware


request_ip = None


def set_request_ip_globally(ip):
    global request_ip
    request_ip = ip


def get_current_request_ip():
    global request_ip
    return request_ip


def global_identifier_extractor_middleware(get_response):
    def extract_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    def middleware(request):
        set_request_ip_globally(extract_ip(request))
        response = get_response(request)
        return response

    return middleware
