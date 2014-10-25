# from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Poem
from .forms import PoemForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy


@login_required
def PoemCreate(request):
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('poems:poem_detail',
                                        kwargs={'pk': form.instance.pk}))
    else:
        form = PoemForm()

    return render(request, 'poems/poem_form.html', {
        'form': form,
    })


@login_required
def PoemUpdate(request, pk):
    if request.method == 'POST':
        form = PoemForm(request.POST, instance=Poem.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('poems:poem_detail',
                                        kwargs={'pk': form.instance.pk}))
    else:
        form = PoemForm(instance=Poem.objects.get(pk=pk))

    return render(request, 'poems/poem_form.html', {
        'form': form,
    })


# class PoemCreate(CreateView):
#     model = Poem
#     fields = ['title', 'body']
#     success_url = '/poem/add/'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(PoemCreate, self).form_valid(form)

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(PoemCreate, self).dispatch(*args, **kwargs)


# class PoemUpdate(UpdateView):
#     model = Poem
#     fields = ['title', 'body']

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(PoemUpdate, self).dispatch(*args, **kwargs)


class PoemDelete(DeleteView):
    model = Poem
    success_url = reverse_lazy('poems:poem_list')


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


class PoemListUser(ListView):
    model = Poem
    paginate_by = 8
    page_kwarg = 'page'

    def get_queryset(self):
        return Poem.objects.filter(user=self.request.user).order_by('-pub_date')


class PoemDetail(DetailView):
    model = Poem


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PoemDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['poem_list'] = Poem.objects.all()
        if self.request.user.is_authenticated():
            if self.request.user.pk is self.object.user.pk:
                context['options'] = {'owner': True}
        return context
