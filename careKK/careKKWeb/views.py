from django.shortcuts import render
from django.http import HttpResponse
from .caraDeCacaExpress.game import *
from .caraDeCacaExpress.Game.players import *
from .caraDeCacaExpress.Game.GameObjets import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
def home(request):
    return render(request,'careKKWeb/home.html')


realPlayer=None
player2=None
deck0=None
gamePvIA0=None

def PvsIA(request):
    realPlayer=player(hand([]),openField([]),closeField([]))
    player2=goodDeterministicPlayer(hand([]),openField([]),closeField([]))
    deck0=deck([card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('3',3,3,"3pica.png","cardsBack.png"),card('3',3,3,"3pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('14',14,14,"Apica.png","cardsBack.png"),card('14',14,14,"Apica.png","cardsBack.png")])
    gamePvIA0=gamePvIA([realPlayer,player2],deck0,4,4)


    gamePvIA0.repartirCartas()    
    
    p1CloseField=realPlayer.getCloseField().getCardsBackImg()
    p1OpenField=realPlayer.getOpenField().getCardsImg()
    p1Hand=realPlayer.getHand().getCardsImg()

    p2CloseField=player2.getCloseField().getCardsBackImg()
    p2OpenField=player2.getOpenField().getCardsImg()
    p2Hand=player2.getHand().getCardsBackImg()

    return render(request,'careKKWeb/PvsIA.html',{"p1CloseField":p1CloseField,"p2CloseField":p2CloseField,"p1OpenField":p1OpenField,"p2OpenField":p2OpenField,"p1Hand":p1Hand,"p2Hand":p2Hand})

@csrf_exempt
def probando(request):
    return JsonResponse({"f":"funciono"})