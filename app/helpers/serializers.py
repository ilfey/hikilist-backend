from rest_framework import serializers


class CurrentUserIdDefault(serializers.CurrentUserDefault):

    def __call__(self, serializer_field):
        return super().__call__(serializer_field).id
