from django.http import JsonResponse


def bad_request(request, exception=None):
    return JsonResponse(
        {
            "detail": "Bad request",
        },
        status=400,
    )


def permission_denied(request, exception=None):
    return JsonResponse(
        {
            "detail": "Permission denied",
        },
        status=403,
    )


def not_found(request, exception=None):
    return JsonResponse(
        {
            "detail": "Not found",
        },
        status=404,
    )


def server_error(request, exception=None):
    return JsonResponse(
        {
            "detail": "Server error",
        },
        status=500,
    )
