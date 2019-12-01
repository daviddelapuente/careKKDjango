from django.shortcuts import render
from django.http import HttpResponse
from .caraDeCacaExpress.game import *
from .caraDeCacaExpress.Game.players import *
from .caraDeCacaExpress.Game.GameObjets import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
def home(request):
    return render(request,'careKKWeb/home.html')

realPlayer=player(hand([]),openField([]),closeField([]))
player2=goodDeterministicPlayer(hand([]),openField([]),closeField([]))
deck0=deck([card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('3',3,3,"3pica.png","cardsBack.png"),card('3',3,3,"3pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('14',14,14,"Apica.png","cardsBack.png"),card('14',14,14,"Apica.png","cardsBack.png")])


def PvsIA(request):
    global gamePvIA0
    global realPlayer
    global deck0
    realPlayer=player(hand([]),openField([]),closeField([]))
    player2=goodDeterministicPlayer(hand([]),openField([]),closeField([]))
    deck0=deck([card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('2',2,2,"2pica.png","cardsBack.png"),card('3',3,3,"3pica.png","cardsBack.png"),card('3',3,3,"3pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('7',7,7,"7pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('10',10,10,"10pica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('11',11,11,"Jpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('13',13,13,"Kpica.png","cardsBack.png"),card('14',14,14,"Apica.png","cardsBack.png"),card('14',14,14,"Apica.png","cardsBack.png")])
    gamePvIA0=gamePvIA([realPlayer,player2],deck0,5,4)

    gamePvIA0.repartirCartas()
    p1CloseField=gamePvIA0.players[0].getCloseField().getCardsBackImg()
    p1OpenField=gamePvIA0.players[0].getOpenField().getCardsImg()
    p1Hand=gamePvIA0.players[0].getHand().getCardsImg()

    p2CloseField=player2.getCloseField().getCardsBackImg()
    p2OpenField=player2.getOpenField().getCardsImg()
    p2Hand=player2.getHand().getCardsBackImg()

    return render(request,'careKKWeb/PvsIA.html',{"p1CloseField":p1CloseField,"p2CloseField":p2CloseField,"p1OpenField":p1OpenField,"p2OpenField":p2OpenField,"p1Hand":p1Hand,"p2Hand":p2Hand})

@csrf_exempt
def player1Play(request):
    global gamePvIA0
    i=int(request.POST['jugada'][13:])
    print(gamePvIA0.players[0].getHand().getCards()[i].getValue())
    return JsonResponse({"f":"funciono"})