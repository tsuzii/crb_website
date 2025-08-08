from django.shortcuts import render
from .models import Vacancy


def vacancies_list(request):
    # Жёсткий порядок категорий
    category_order = [
        'high_med_education',
        'secondary_med_education',
        'high_education',
        'secondary_education',
        'other',
    ]

    # Создаём словарь: {значение: метка}
    category_labels = dict(Vacancy.CATEGORY_CHOICES)

    grouped_vacancies = []

    for cat_value in category_order:
        cat_label = category_labels.get(cat_value, cat_value)
        vacancies = Vacancy.objects.filter(
            category=cat_value,
            is_active=True
        ).order_by('title')

        grouped_vacancies.append({
            'category_label': cat_label,
            'vacancies': vacancies
        })

    context = {
        'grouped_vacancies': grouped_vacancies
    }
    return render(request, 'vacancies/vacancies.html', context)
