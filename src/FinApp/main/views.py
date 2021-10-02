import numpy as np
import pandas as pd
from django.http import Http404
from django.shortcuts import render
from .models import InputField, Category
from .forms import FieldForm, CatForm
from django.db.models import Sum, Count
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px


def index(request):
    """View for main page"""
    total_spend = InputField.objects.aggregate(Sum('amount'))['amount__sum']
    spends = InputField.objects.order_by('-id')
    cats = Category.objects.all()
    context = {'spends': spends,
               'title': 'Main',
               'cats': cats,
               'total': total_spend,
               'cat_selected': 0,
               }
    return render(request, 'main/index.html', context=context)


def calc(request):
    """View for add spend page"""
    message = ''
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            message = "data added"
        else:
            message = "Not valid form"
    form = FieldForm()
    context = {
        'form': form,
        'title': 'Add spend',
        'message': message
    }
    return render(request, 'main/calc.html', context=context)


def add_cat(request):
    """View for add category page"""
    message = ''
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            message = "New category created"
        else:
            message = "Not valid name"
    form = CatForm()
    context = {'form': form,
               'title': 'Add category',
               'message': message
               }
    return render(request, 'main/add_cat.html', context)


def show_category(request, cat_id):
    """View for category's page"""
    spends = InputField.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(spends) == 0:
        raise Http404()
    context = {'spends': spends,
               'cats': cats,
               'title': 'Display by category',
               'cat_selected': cat_id
               }
    return render(request, 'main/index.html', context=context)


def spend_by_date(request):
    """View for spends by date(day,month,year)"""
    spends = InputField.objects.order_by('-date')

    context = {'title': 'Display by date',
               'spends': spends,
               'cat_date_selected': 0
               }
    return render(request, 'main/spends_by_date.html', context=context)


def spend_by_day(request):
    """View for intervals in spends_by_date"""
    spends = InputField.objects.order_by('date__day')
    if len(spends) == 0:
        raise Http404()
    context = {'spends': spends,
               'title': 'Display by interval',
               'cat_date_selected': 1,
               }
    return render(request, 'main/day.html', context=context)


def spend_by_month(request):
    """View for intervals in spends_by_date"""
    spends = InputField.objects.order_by('date__month')
    if len(spends) == 0:
        raise Http404()
    context = {'spends': spends,
               'title': 'Display by interval',
               'cat_date_selected': 2,
               }
    return render(request, 'main/month.html', context=context)


def spend_by_year(request):
    """View for intervals in spends_by_date"""
    spends = InputField.objects.order_by('date__year')
    if len(spends) == 0:
        raise Http404()
    context = {'spends': spends,
               'title': 'Display by interval',
               'cat_date_selected': 3,
               }
    return render(request, 'main/year.html', context=context)


def about(request):
    """View for about spends page"""
    sc = Category.objects.annotate(Count('name'))
    select_cat = list(Category.objects.values_list('name', flat=True))
    # select_cat = Category.objects.values('name')
    lst_spends = []
    for el in sc:
        total_spend_by_cat = InputField.objects.filter(cat=el).aggregate(Sum('amount'))
        lst_spends.append(total_spend_by_cat)
    diagram = zip(select_cat, lst_spends)
    y_date = [1, 2, 3, 4, 5, 6, 7]
    df = pd.DataFrame(lst_spends)
    lst = df['amount__sum'].to_list()
    # lst = [i['amount__sum'] for el in lst_spends for i in el.values()]
    fig = go.Figure(go.Bar(y=lst, x=select_cat))
    context = {'select_cat': select_cat,
               'title': 'About spends',
               'lst': lst,
               'diagram': diagram,
               'fig': fig
               }
    return render(request, 'main/spend_by_cat.html', context=context)
