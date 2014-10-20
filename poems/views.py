# from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Poem


class PoemCreate(CreateView):
    model = Poem
    fields = ['title', 'body']
    success_url = '/poem/add/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PoemCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PoemCreate, self).dispatch(*args, **kwargs)


class PoemUpdate(UpdateView):
    model = Poem
    fields = ['title', 'body']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PoemUpdate, self).dispatch(*args, **kwargs)


class PoemDelete(DeleteView):
    model = Poem
    # success_url = reverse_lazy('Poem-list')


class PoemList(ListView):
    model = Poem
    paginate_by = 8
    page_kwarg = 'page'
    queryset = Poem.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super(PoemList, self).get_context_data(**kwargs)
            # Add in a QuerySet of all the books
            context['front'] = True
            context['content'] = {}
            context['content']['text'] = {
                'head': {
                    'title': 'Last Works',
                    'body': '<p class="info">\
                    Collaborative production of poetry and short stories</p>',
                    'img': 'img/content/home/work/pencil.svg'
                }}
            return context


class PoemDetail(DetailView):
    model = Poem

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PoemDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['poem_list'] = Poem.objects.all()
        return context
