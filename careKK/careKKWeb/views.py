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
    gamePvIA0=gamePvIA([realPlayer,player2],deck0,4,4)

    gamePvIA0.repartirCartas()
    p1CloseField=gamePvIA0.players[0].getCloseField().getCardsBackImg()
    p1OpenField=gamePvIA0.players[0].getOpenField().getCardsImg()
    p1Hand=gamePvIA0.players[0].getHand().getCardsImg()

    p2CloseField= gamePvIA0.players[1].getCloseField().getCardsBackImg()
    p2OpenField=gamePvIA0.players[1].getOpenField().getCardsImg()
    p2Hand=gamePvIA0.players[1].getHand().getCardsImg()

    return render(request,'careKKWeb/PvsIA.html',{"p1CloseField":p1CloseField,"p2CloseField":p2CloseField,"p1OpenField":p1OpenField,"p2OpenField":p2OpenField,"p1Hand":p1Hand,"p2Hand":p2Hand})

@csrf_exempt
def player1Play(request):
    global gamePvIA0
    i=request.POST['jugada']
    #the 0 represent the player number 0

    gamePvIA0.RealPlayerPlay(i,0)

    jugadas=gamePvIA0.players[1].think(gamePvIA0.gameState)

    iaField=gamePvIA0.IAPlayerPlay(1,jugadas)

    if jugadas=="out":
        return JsonResponse({"jugadaIa":jugadas,"newHand":gamePvIA0.players[1].getHand().getCardsImg()})
    else:
        return JsonResponse({"jugadaIa":jugadas,"iaField":iaField})