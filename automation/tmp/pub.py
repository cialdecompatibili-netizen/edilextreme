import sys
sys.path.insert(0, r"C:\Users\mirco\Desktop\cmspush_multisite")
from publish import pubblica_articolo

articoli = []

articoli.append(("Pulizia, manutenzione e installazione canne fumarie", r"""Una canna fumaria intasata o mal installata non e solo un problema di tiraggio: e un rischio concreto per la sicurezza di chi vive in casa. Fuliggine, detriti e nidi di volatili possono ostruire il condotto e favorire il ritorno di fumi in ambiente.

EdilExtreme interviene su fune per la pulizia, la manutenzione e l'installazione di canne fumarie poste in quota, senza bisogno di ponteggi o piattaforme aeree. Raggiungiamo il comignolo direttamente dall'alto, riducendo tempi e costi rispetto a un intervento tradizionale.

## Cosa controlliamo

Verifichiamo lo stato interno del condotto, la tenuta dei giunti e la presenza di eventuali ostruzioni. In caso di nuova installazione, valutiamo il corretto dimensionamento e posizionamento del comignolo per garantire un tiraggio efficiente in ogni stagione.

## Perche non rimandare

Un condotto pulito e ben mantenuto significa un impianto di riscaldamento piu sicuro ed efficiente, che sia una stufa a pellet o un caminetto tradizionale. Consigliamo un controllo periodico, soprattutto prima dell'avvio della stagione fredda.

Richiedi un sopralluogo gratuito: interveniamo rapidamente, ovunque si trovi il tuo camino."""))

articoli.append(("Riparazione e pulizia grondaie", r"""Le grondaie intasate sono una delle cause piu comuni di infiltrazioni e muffa sulle facciate. Quando l'acqua piovana non defluisce correttamente, tende a tracimare o a ristagnare, danneggiando intonaci, cornicioni e murature nel tempo.

EdilExtreme esegue interventi di pulizia, manutenzione e sostituzione di grondaie e pluviali operando su fune, senza montare impalcature. I nostri tecnici raggiungono direttamente il punto interessato, rimuovendo foglie, detriti e ostruzioni in tempi rapidi.

## Un intervento preventivo che conviene

Programmare una pulizia periodica delle grondaie e un'azione a basso costo che evita danni ben piu ingenti: muffa sulle pareti interne, distacchi di intonaco, infiltrazioni nei solai. Se il problema e gia in corso, valutiamo anche la sostituzione dei tratti danneggiati.

## Quando intervenire

I segnali da non ignorare sono aloni di umidita sotto i cornicioni, acqua che scende lungo la facciata invece che nel pluviale, e vegetazione che cresce nel canale di gronda. Prima si interviene, minore e il danno da riparare.

Contattaci per un sopralluogo gratuito e senza impegno."""))

articoli.append(("Installazione e manutenzione dissuasori per piccioni", r"""I piccioni sui cornicioni non sono solo un fastidio estetico: i loro escrementi corrodono superfici e coperture, e i nidi possono ostruire grondaie e canne fumarie, aggravando altri problemi dell'edificio.

EdilExtreme installa e mantiene sistemi dissuasori anti-volatili su cornicioni, balconi e coperture, operando su fune senza ponteggi. Interveniamo direttamente sui punti dove i piccioni si posano, con soluzioni discrete e durature.

## Le soluzioni che utilizziamo

A seconda della superficie e dell'esposizione, valutiamo spuntoni anti-atterraggio, reti di protezione o cavi a bassa tensione, scegliendo la combinazione piu efficace senza alterare l'estetica dell'edificio.

## Un problema che si aggrava nel tempo

Piu a lungo si rimanda l'intervento, maggiore e l'accumulo di sporco e il rischio di danni a facciate e coperture. Un intervento tempestivo protegge l'edificio e riduce i costi di pulizia futuri.

Richiedi un sopralluogo gratuito: valutiamo insieme la soluzione piu adatta al tuo edificio."""))

articoli.append(("Montaggio isolanti", r"""Un edificio disperso termicamente costa di piu da riscaldare d'inverno e da raffrescare d'estate. Intervenire sull'isolamento di facciate e coperture e uno degli investimenti che incide maggiormente sull'efficienza energetica di un immobile.

EdilExtreme installa isolanti termici e acustici operando su fune, senza il bisogno di montare ponteggi. Questo permette di intervenire su facciate e coperture con cantieri molto piu rapidi e meno invasivi rispetto ai metodi tradizionali.

## Dove interveniamo

Lavoriamo su cappotti termici puntuali, isolamento di cornicioni e sottotetti, e interventi mirati nei punti di dispersione piu critici, individuati durante il sopralluogo iniziale.

## I vantaggi della tecnica su fune

Zero impalcature significa zero ingombro a terra e zero permessi comunali per il cantiere. I condomini continuano a usare balconi e spazi comuni durante tutta la durata dei lavori, con un impatto minimo sulla vita quotidiana.

Richiedi un sopralluogo gratuito per valutare dove il tuo edificio disperde piu calore."""))

articoli.append(("Montaggio sistemi di sicurezza su fune", r"""Molti edifici non dispongono di punti di ancoraggio sicuri per gli interventi di manutenzione futuri, costringendo ogni volta a montare ponteggi anche per lavori minori.

EdilExtreme installa linee vita e sistemi di ancoraggio permanenti in quota, pensati per rendere piu semplici e sicuri tutti gli interventi di manutenzione successivi, sia per il nostro team che per altri operatori qualificati.

## Perche installarli

Un sistema di sicurezza permanente riduce i costi e i tempi di ogni futuro intervento su facciate e coperture, eliminando la necessita di allestire un cantiere completo ogni volta.

## Come lavoriamo

L'installazione avviene direttamente in quota, valutando i punti di ancoraggio piu idonei in base alla struttura dell'edificio e alle normative di sicurezza vigenti in materia di lavori in altezza.

Contattaci per un sopralluogo gratuito e senza impegno."""))

for titolo, corpo in articoli:
    excerpt = corpo.strip().split("\n")[0][:160]
    try:
        pubblica_articolo("edilextreme", titolo, "servizi", excerpt, corpo)
        print("OK:", titolo)
    except Exception as e:
        print("SALTATO:", titolo, "->", e)
