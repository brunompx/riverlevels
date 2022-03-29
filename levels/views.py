from django.shortcuts import render
from levels.models import Level


def levelchart_index(request):
    
    context = build_context_data()

    return render(request, 'levelchart.html', context)




def build_context_data():
    levels = Level.objects.all()

    value_date_set = set([l.value_date for l in levels])
    value_date_list = list(value_date_set)
    value_date_list.sort()
    context = {
        'dates' : value_date_list
    }

    datasets = []
    for level in levels:
        dataset = next((d for d in datasets if d['label'] == level.label), None)
        if dataset is None:
            line_data_dict = dict.fromkeys(value_date_list)
            line_data_dict[str(level.value_date)] = level.value
            dataset = {
                'label' : level.label, 
                'values_dic' : line_data_dict
            }
            datasets.append(dataset)
        else:
            dataset['values_dic'][str(level.value_date)] = level.value

    for ds in datasets:
        print("---------------------------------")
        print("---------------------------------")
        # ds['values_list'] = ds['values_dic'].values()
        ds['values_list'] = [v for v in ds['values_dic'].values() if v != None]
        for k, v in ds['values_dic'].items():
            print(k, v)
            
    context = {
        'dates' : value_date_list,
        'datasets' : datasets
    }


    #datasets list
        #dataset dic
            #label srt 
            #values_dic dic
            #values_list list
    return context
