from django.shortcuts import render
from levels.models import Level


def levelchart_index(request):
    context = build_context_data()
    return render(request, 'levelchart.html', context)


def build_context_data():
    levels_qs = Level.objects.all()

    #List of dates cor the x-axis labels
    value_date_set = set([l.value_date for l in levels_qs])
    value_date_list = (list(value_date_set)).sort()
    # value_date_list.sort()

    #Build the chart data
    datasets = []
    for level in levels_qs:
        dataset = next((d for d in datasets if d['label'] == level.label), None)
        if dataset is None:
            line_data_dict = dict.fromkeys(value_date_list)
            line_data_dict[level.value_date] = level.value
            dataset = {
                'label' : level.label, 
                'values_dic' : line_data_dict
            }
            datasets.append(dataset)
        else:
            dataset['values_dic'][level.value_date] = level.value
            
    context = {
        'dates' : value_date_list,
        'datasets' : datasets
    }
    return context
