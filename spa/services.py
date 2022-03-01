from .models import SomeObj


def my_filter(condition, field, user_input):

    if field == 'name':

        if condition == 'eq':
            queryset = SomeObj.objects.filter(name=user_input)

        elif condition == 'icontains':
            queryset = SomeObj.objects.filter(name__icontains=user_input)

        elif condition == 'gt':
            queryset = SomeObj.objects.filter(name__gt=user_input)

        elif condition == 'lt':
            queryset = SomeObj.objects.filter(name__lt=user_input)

    elif field == 'qty':

        if condition == 'eq':
            queryset = SomeObj.objects.filter(qty=user_input)

        elif condition == 'icontains':
            queryset = SomeObj.objects.filter(qty__icontains=user_input)

        elif condition == 'gt':
            queryset = SomeObj.objects.filter(qty__gt=user_input)

        elif condition == 'lt':
            queryset = SomeObj.objects.filter(qty__lt=user_input)

    elif field == 'distance':

        if condition == 'eq':
            queryset = SomeObj.objects.filter(distance=user_input)

        elif condition == 'icontains':
            queryset = SomeObj.objects.filter(distance__icontains=user_input)

        elif condition == 'gt':
            queryset = SomeObj.objects.filter(distance__gt=user_input)

        elif condition == 'lt':
            queryset = SomeObj.objects.filter(distance__lt=user_input)

    return queryset