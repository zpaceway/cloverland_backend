import json


def submission(request):
    data = request.body
    body_dict = json.loads(data.decode("utf-8")) if data else {}

    return {
        **body_dict,
        **request.POST.dict(),
        **request.GET.dict(),
    }
