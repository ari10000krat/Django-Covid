from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    return render(request, 'covid/index.html')


def about(request):
    categoryArr = ['#', 'Country', 'Total Cases',
                   'Total Deaths', 'Total Recovered']
    statisticsArr = [
        ['1', 'USA', '21,865,323', '370,071', '13,025,931'],
        ['2', 'India', '10,405,097', '150,470', '10,026,751'],
        ['3', 'Brazil', '7,874,539', '199,044', '7,036,530'],
        ['4', 'Russia', '3,332,142', '60,457', '2,709,452'],
        ['5', 'UK', '2,836,801', '77,346', '1,345,824'],
        ['6', 'France', '2,705,618', '66,565', '198,756'],
        ['7', 'Turkey', '2,283,931', '22,070', '2,164,040'],
        ['8', 'Italy', '2,201,945', '76,877', '1,556,356'],
        ['9', 'Spain', '1,982,544', '51,430', '1,405,456'],
        ['10', 'Germany', '1,848,621', '38,436', '1,474,048'],
        ['11', 'Colombia', '1,719,771', '44,723', '1,569,578'],
        ['12', 'Argentina', '1,676,171', '43,976', '1,474,048'],
        ['13', 'Mexico', '1,479,835', '129,987', '1,119,968'],
        ['14', 'Poland', '1,356,882', '30,241', '1,095,616'],
        ['15', 'Iran', '1,268,263', '55,933', '1,050,533'],
        ['16', 'South Africa', '1,149,591', '31,368', '929,239'],
        ['17', 'Ukraine', '1,009,493', '19,505', '773,214']]

    covidDict = {
        'categoryArr': categoryArr,
        'statisticsArr': statisticsArr,
        'arrLenght': range(0, len(statisticsArr)),
    }

    return render(request, 'covid/about.html', covidDict)


def contact(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../index")

        else:
            error = "Form validation isn't completed"

    form = ArticleForm()
    data = {
        'form': form,
        'error': error,

    }
    return render(request, 'covid/contact.html', data)


def comments(request):
    comments = Article.objects.order_by('-date')
    return render(request, 'covid/comments.html', {'comments': comments})


class CommentsDetailView(DetailView):
    model = Article
    template_name = 'covid/details_view.html'
    context_object_name = 'article'


class CommentsUpdateView(UpdateView):
    model = Article
    template_name = 'covid/contact.html'
    context_object_name = 'article'
    form_class = ArticleForm


class CommentsDeleteView(DeleteView):
    model = Article
    template_name = 'covid/comment_delete.html'
    success_url = '/comments'
    context_object_name = 'article'
    form_class = ArticleForm
