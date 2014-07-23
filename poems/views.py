# from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Poem


class PoemCreate(CreateView):
    model = Poem
    fields = ['title', 'body']
    success_url = '/poem/add/'


class PoemUpdate(UpdateView):
    model = Poem
    fields = ['title', 'body']


class PoemDelete(DeleteView):
    model = Poem
    # success_url = reverse_lazy('Poem-list')


class PoemList(ListView):
    queryset = Poem.objects.all().order_by('-created')
    # model = Poem


class PoemDetail(DetailView):
    model = Poem

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PoemDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['poem_list'] = Poem.objects.all()
        return context
