def register_viewsets(router, *args):
    for viewsets in args:
        for (name, viewset, basename) in viewsets:
            router.register(name, viewset, basename)