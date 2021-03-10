from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.views.generic import DetailView, ListView
from .models import SportNew, Category
# Create your views here.

class CategoryListView(ListView):
    model = Category
    # queryset = Category.objects.filter(active=True)
    template_name = 'sportnew/category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'sportnew/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        sportnew_set = obj.sportnew_set.all()
        default_sportnew = obj.default_category.all()
        sportnews = (sportnew_set | default_sportnew).distinct().filter(active=True)
        context['sportnews'] = sportnews
        return context

class SportNewDetailView(DetailView):
    model = SportNew
    template_name = 'sportnew/sportnew_details.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(SportNewDetailView, self).get_context_data(*args, **kwargs)
    #     instance = self.get_object()
    #     context["related"] = sorted(SportNew.objects.get_related(instance)[:6], key= lambda x: random.random())
    #     return context

class SportNewsListView(ListView):
    model = SportNew
    queryset = SportNew.objects.filter(active=True)
    template_name = 'sportnew/sportnew_list.html'

    
    def get_context_data(self, *args, **kwargs):
        context = super(SportNewsListView, self).get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get("q")
        return context
        
    def get_queryset(self, *args, **kwargs):
        qs = super(SportNewsListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains = query) |
                Q(details__icontains = query)|
                Q(writer__icontains = query)
            )
        return qs
    
