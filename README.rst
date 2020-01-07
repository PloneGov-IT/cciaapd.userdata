==================
CCIAPD - User data
==================

Aggiunge campi extra per la registrazione degli utenti


Comuni
------

Uno dei campi, prevede una lista di comuni di Padova tra cui scegliere.

La lista è fissata nel file `comuni.py`.

Monkeypatch
-----------

Abbiamo dovuto patchare un metodo di formlib in monkey.py (definito in monkey.zcml) per problemi con l'encoding di caratteri con accenti.


Traduzioni
----------

Questo prodotto è stato tradotto nelle seguenti lingue:

- Italiano


Installazione
-------------

Installa camcomskin.padova aggiungendolo al tuo buildout::

    [buildout]

    ...

    eggs =
        cciaapd.userdata


e successivamente eseguendo ``bin/buildout``.

Al successivo avvio del sito troverete il tema disponibile tra i prodotti aggiuntivi del sito, con il nome "CCIAPD: User data".


Compatibilità
-------------

Questo prodotto è stato testato su Plone < 5.


Riconoscimenti
--------------

Sviluppato con il supporto di `Camera di commercio di Padova`__.

__ https://www.pd.camcom.it



Autori
------

Questo prodotto è stato sviluppato dal team di RedTurtle Technology.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
