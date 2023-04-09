from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView
from .models import Topic, Question, Comment


def index(request):
    main_topics = Topic.objects.filter(parent_topic__isnull=True)
    questions = Question.objects.all().order_by('-id')[:3]
    return render(request, template_name='forum/index.html', context={'main_topics': main_topics, 'questions': questions})


def card(request):
    return render(request, template_name='forum/cards.html')


class QuestionList(ListView):
    template_name = 'forum/list_questions.html'
    context_object_name = 'questions'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_topics'] = Topic.objects.filter(parent_topic__isnull=True)

        return context

    def get_queryset(self):
        queryset = Question.objects.annotate(comment_count=Count('comment')).all().order_by('-id')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


def topic_detail_views(request, slug):
    main_topics = Topic.objects.filter(parent_topic__isnull=True)
    topic = Topic.objects.get(slug=slug)
    questions = Question.objects.annotate(comment_count=Count('comment')).filter(topic__slug=slug)

    # задайте количество элементов на странице
    per_page = 15
    paginator = Paginator(questions, per_page)

    # получите номер страницы из GET-параметра
    page_number = request.GET.get('page')

    # получите объекты в соответствии с номером страницы
    page_obj = paginator.get_page(page_number)

    return render(request, template_name='forum/topic_detail.html', context={
        'main_topics': main_topics,
        'questions': page_obj,
        'topic': topic})


def question_detail_view(request, slug):
    main_topics = Topic.objects.filter(parent_topic__isnull=True)
    question = Question.objects.get(slug=slug)
    comments = Comment.objects.filter(question=question)
    paginator = Paginator(comments, per_page=15)  # set number of comments per page
    page_number = request.GET.get('page')
    comments = paginator.get_page(page_number)
    return render(request, template_name='forum/question_detail.html', context={
        'main_topics': main_topics,
        'question': question,
        'comments': comments
    })










