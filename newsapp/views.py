from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .forms import ContactForm
from .models import News, Category
from django.http import HttpResponse

# def ListPageView(request):
#     news_list = News.published.all()
#     context = {
#         'news_list': news_list,
#     }
#     return render(request, 'news_list.html', context)
class ListPageView(View):
    pass
def DetailPageView(request, slug):
    # try:
    #     news_detail = News.published.get(id=id)
    # except News.DoesNotExist:
    #     raise Http404('News not found')
    news_detail = get_object_or_404(News, slug=slug, status=News.Status.Published)
    context = {
        'news_detail': news_detail,
    }
    return render(request, 'news_detail.html', context)


class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        newslist = News.published.all().order_by('-published_time')[:5]
        latest_newslist = News.published.all().order_by('-published_time')[:5]
        local_news = News.published.filter(category__name='mahalliy').order_by('-published_time')[:6]
        xorij_news = News.published.filter(category__name='Xorij').order_by('-published_time')[:6]
        tehnologiya_news = News.published.filter(category__name='Tehnologiya').order_by('-published_time')[:6]
        sport_news = News.published.filter(category__name='sport').order_by('-published_time')[:6]
        xorij_news_one = News.published.filter(category__name='Xorij').order_by('-published_time').first()
        tehnologiya_news_one = News.published.filter(category__name='Tehnologiya').order_by('-published_time').first()
        sport_news_one = News.published.filter(category__name='sport').order_by('-published_time').first()
        context = {
            'news_list': newslist,
            'latest_newslist': latest_newslist,
            'categories': categories,
            'local_news': local_news,
            'xorij_news': xorij_news,
            'tehnologiya_news': tehnologiya_news,
            'sport_news': sport_news,
            'xorij_news_one': xorij_news_one,
            'tehnologiya_news_one': tehnologiya_news_one,
            'sport_news_one': sport_news_one,
        }
        return render(request, 'home.html', context)

#
# class ContactPageView(View):
#     def get(self, request):
#         return render(request, 'contact.html')
#
class ContactPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        forms_page = ContactForm()
        context = {
            'forms_page': forms_page,
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        forms_page = ContactForm(request.POST)
        if forms_page.is_valid():
            forms_page.save()
            return HttpResponse("<h1>Sizning xaabringiz yetib keldi</h1>")
        else:
            context = {
                'forms_page': forms_page,
            }
            return render(request, 'contact.html', context)
            # return self.render_to_response(request)

###local news
class LocalNewsViews(ListView):
    model = News
    template_name = 'local_news.html'
    context_object_name = 'local_news_list'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='mahalliy')
        return news

class TechnolgyNewsViews(ListView):
    model = News
    template_name = 'technolgy_news.html'
    context_object_name = 'technolgy_news_list'


    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Tehnologiya')
        return news

class XorijNewsViews(ListView):
    model = News
    template_name = 'xorij_news.html'
    context_object_name = 'xorij_news_list'


    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news

class SportNewsViews(ListView):
    model = News
    template_name = 'sport_news.html'
    context_object_name = 'sport_news_list'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='sport')
        return news

class UpdateNewsView(UpdateView):
    model = News
    template_name = 'crud/update_news.html'
    fields = ['title','body', 'image', 'category', 'status',]

class DeleteNewsView(DeleteView):
    model = News
    template_name = 'crud/delete_news.html'
    success_url = reverse_lazy('newsapp:home_page')

class CreateNewsView(CreateView):
    model = News
    template_name = 'crud/create_news.html'
    fields = ['title', 'body', 'image', 'category', 'status']