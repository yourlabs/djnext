from django.urls import reverse


def menu(request):
    return dict(
        menu=[
            dict(
                title='Create artist',
                url=reverse('artist_create'),
            ),
            dict(
                title='List artist',
                url=reverse('artist_list'),
            ),
        ]
    )
