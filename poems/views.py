# from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import *
from .forms import PoemForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from favorite.models import Favorite
from django.contrib.contenttypes.models import ContentType


@login_required
def PoemCreate(request):
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('poems:poem_detail',
                                        kwargs={'pk': form.instance.pk,
                                        'list': 'user'}))
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
                                        kwargs={'pk': form.instance.pk,
                                        'list': 'user'}))
    else:
        form = PoemForm(instance=Poem.objects.get(pk=pk))

    return render(request, 'poems/poem_form.html', {
        'form': form,
    })


class PoemDelete(DeleteView):
    model = Poem
    success_url = reverse_lazy('poems:poem_list')


class PoemListBase(ListView):
    model = Poem
    paginate_by = 8
    page_kwarg = 'page'


class PoemList(PoemListBase):
    queryset = Poem.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(PoemList, self).get_context_data(**kwargs)
        context['front'] = True
        title = _('Last Works')
        context['title'] = title
        context['list'] = 'all'

        return context


class PoemListUser(PoemListBase):
    def get_context_data(self, *args, **kwargs):
        context = super(PoemListUser, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.args[0])
        if user == self.request.user:
            title = _('My Poems')
        else:
            title = _('Poems of %(user)s') % {'user': user}
        context['title'] = title
        context['list'] = 'user'
        return context

    def get_queryset(self):
        return Poem.objects.filter(user=self.args[0])\
            .order_by('-pub_date')


class PoemListFavorites(PoemListBase):
    template_name = "poems/poem_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PoemListFavorites, self).get_context_data(**kwargs)
        title = _('My Favorites')
        context['title'] = title
        context['list'] = 'favorite'
        return context

    def get_queryset(self):
        user = User.objects.get(pk=self.args[0])
        queryset = Favorite.objects.filter(
            user=user, target_content_type=ContentType.objects.get(
                app_label="poems", model="poem")).order_by('-timestamp')
        return [favorite.target for favorite in queryset]


class PoemListBook(PoemListBase):
    def get_context_data(self, *args, **kwargs):
        context = super(PoemListBook, self).get_context_data(**kwargs)
        book = Book.objects.get(pk=self.args[0])
        title = _('Poems of %(book)s') % {'book': book}
        context['title'] = title
        context['list'] = 'book'
        return context

    def get_queryset(self):
        return Poem.objects.filter(book=self.args[0])\
            .order_by('-pub_date')


class PoemListAuthor(PoemListBase):
    def get_context_data(self, *args, **kwargs):
        context = super(PoemListAuthor, self).get_context_data(**kwargs)
        author = Author.objects.get(pk=self.args[0])
        title = _('Poems of %(author)s') % {'author': author}
        context['title'] = title
        context['list'] = 'author'
        return context

    def get_queryset(self):
        return Poem.objects.filter(author=self.args[0])\
            .order_by('-pub_date')


class PoemDetail(DetailView):
    model = Poem

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PoemDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            if self.request.user.pk is self.object.user.pk:
                context['options'] = {'owner': True}
        context['list'] = self.kwargs['list']
        if self.kwargs['list'] == 'user':
            try:
                context['previus'] =\
                    self.object.get_previous_by_pub_date(user=self.object.user)
            except:
                pass
            try:
                context['next'] =\
                    self.object.get_next_by_pub_date(user=self.object.user)
            except:
                pass

        elif self.kwargs['list'] == 'author':
            try:
                context['previus'] =\
                    self.object.get_previous_by_pub_date(
                        author=self.object.author)
            except:
                pass
            try:
                context['next'] =\
                    self.object.get_next_by_pub_date(author=self.object.author)
            except:
                pass
        elif self.kwargs['list'] == 'book':
            try:
                context['previus'] =\
                    self.object.get_previous_by_pub_date(book=self.object.book)
            except:
                pass
            try:
                context['next'] =\
                    self.object.get_next_by_pub_date(book=self.object.book)
            except:
                pass
        elif self.kwargs['list'] == 'favorite':
            favorite_poem = Favorite.objects.get(
                user=self.request.user,
                target_object_id=self.object.pk,
                target_content_type=ContentType.objects.get(
                    app_label="poems", model="poem"))
            try:
                context['previus'] =\
                    favorite_poem.get_previous_by_timestamp(
                        user=self.request.user,
                        target_content_type=ContentType.objects.get(
                            app_label="poems", model="poem")).target
            except:
                pass
            try:
                context['next'] =\
                    favorite_poem.get_next_by_timestamp(
                        user=self.request.user,
                        target_content_type=ContentType.objects.get(
                            app_label="poems", model="poem")).target
            except:
                pass
        else:
            try:
                context['previus'] =\
                    self.object.get_previous_by_pub_date()
            except:
                pass
            try:
                context['next'] =\
                    self.object.get_next_by_pub_date()
            except:
                pass

        return context


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
