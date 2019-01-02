from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from leaderboard.models import Leaderboard, HeroInfo


# Create your views here.
def index(request):
    boardlist=Leaderboard.objects.all()
    # template=loader.get_template('leaderboard/index.html')
    # context=RequestContext(request,{'boardlist':boardlist})
    # return HttpResponse(template.render(context))
    return render(request,'leaderboard/index.html',context={'boardlist':boardlist})
def detail(request,id):
    board = Leaderboard.objects.get(pk=id)
    print(board)
    print(board.pk)
    heros=board.heroinfo_set.all()
    return render(request,'leaderboard/detail.html',
                  context={
                      'board':board,
                      'heros':heros
                  })