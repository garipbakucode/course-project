from core.models import About


def header_and_footer(request):
    about = About.objects.first()
    context = {
        'context_about': about,
    }

    return context
