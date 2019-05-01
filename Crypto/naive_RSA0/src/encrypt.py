from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# p = getPrime(4096)
# q = getPrime(4096)
# n = p*q
n = 944596184878910952264918828296871870994376550458945115258394945073107584173702035979973230660738361172630327621960496272454672732496422999339318188654471910204601330968390297103022738364727453337362198385251002236960101361661918040202036165339768333589056299376897058446389955288838710764178850224984753171552902646225195393795307799225080145564416518846048866414832903230025434101126213440635358354082571921482391685745196953112907788290024449151917565638975172221794083323226310103637529156335586642493986830583679585356467031606826827617520244699586917709280762416539492052960415875646461061269787826714805415719407221087523366347429333359466431951024125697105154441837446345192967298375846760211673136238685670211601498001633401811874044739557854971459770000139308371923735847079684245824356397244021681401775864249234917997277489502084003352067737512704561828201328136271068595038644102118722181194583347195668067691251053156220840731855978538205474623004325770244550226446024576598163764100913061480432121098722621268264322142727933890359031944994515107982197143613130852528978999516503811882849247180413723888824177891793657425942877252813443777922029275037093577669463729857468663658489607472053947326441347663621496156430849523996631737308378819965464124022271648488670669731106892874845122219171857492966317500709601623125149582459270404072727833367221848174325753417252797977803030663910071000796065921485761373667371881974231117477486326293345034509280337329047492102332373702712930729847860908590140794394632881909406664589754236514946602386985031822790567779817767019958733916063119461518028124370795047368353084536075775490812963807687102200929357009366333899423531761526876744777870474557826455433702707417271531300381976447015421648948070517562896827512141969785080788524266986421079341505034297071816437366004796821184678981587004159684554932368186347162273669162187460727526773012212684766172397948227142470918702258745950888367048702980907081253832252716151478583409465289751306792946525476362073790584748769901990112669651234570224592274776406113846028439177811364161864432548532595676882578421605785138198330175308016530275943081455043217677343220943801192914551421746043508948550034056364914497144799658963343027337311650776739829707498952269704646163521188348922635016117695339877218590073847253055931147657012328054539970661943972262728438050114088791918421154537588547802858806161521544516620844416104046169437332233466602499701081666671571
e = 3

s = open("flag", "rb").read()
a = bytes_to_long(s)
f = open("cipher", "wb")
f.write(long_to_bytes(pow(a, e, n)))