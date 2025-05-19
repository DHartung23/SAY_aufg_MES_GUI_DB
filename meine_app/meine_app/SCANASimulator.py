import math
import threading
import time
import random

import MES

class SCANASimulator:
    def __init__(self, mes : MES, updateZeit : int, updateWahrscheinlichkeit : int, mindestProzent : int, maximalProzent : int):
        self.__mes = mes
        self.__updateZeit = updateZeit
        self.__updateWahrscheinlichkeit = updateWahrscheinlichkeit
        self.__mindestProzent = mindestProzent
        self.__maximalProzent = maximalProzent

        self.__thread = threading.Thread( target=self.__run())
        self.__stopEvent = threading.Event()
        self.__started = False

    def start(self):
        if self.__started:
            raise RuntimeError("SCANASimulator is already running")

        self.__started = True
        self.__thread.start()

    def __run(self):
        while not self.__stopEvent.is_set():
            for produktionline in self.__mes.get_produktionslinie():
                for produktionsauftag in produktionline:

                    # Produktionsauftragsmenge nur aktualiesieren, wenn Status in "in Production" und
                    # updateWahrscheinlichkeit in dieser Runde erfüllt
                    if produktionsauftag.get_Status() == "in Production" and random.random() < self.__updateWahrscheinlichkeit:
                        #Prozentwert der in dieser Runde zu produzierten Einheiten in Abhängigkeit der avisierten Menge
                        produzierendeProzent = random.uniform(self.__mindestProzent, self.__maximalProzent)
                        produzierendeEinheiten = math.ciel( produzierendeProzent * produktionsauftag.getAvisierteMenge())


                        if produktionsauftag.getMenge() + produzierendeEinheiten > produktionsauftag.getAvisierteMenge():
                            produzierendeEinheiten = produktionsauftag.getAvisierteMenge() - produktionsauftag.getMenge()

                        produktionsauftag.produce_units(produzierendeEinheiten)

            # Warten bis zur nächsten Runden
            time.sleep(self.__updateZeit)

    def stop(self):
        self.__stopEvent.set()