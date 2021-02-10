import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_lisataan_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_lisataan_liikaa_saldoa_Vapaa_tila_ei_negatiivinen(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_ottamisen_jalkeinen_saldo_oikea(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo - self.varasto.ota_varastosta(2), 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ota_varastosta_negatiivinen_saldo(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), 0.0)
    
    def test_ota_varastosta_liian_suuri_maara(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 7)
        
    def test_saldo_kun_otetaan_liian_suuri_maara(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)
        self.assertAlmostEqual(self.varasto.saldo, 0) 

    
    def test_tulostaa_oikean_saldon(self):
        self.varasto.lisaa_varastoon(4)
        self.varasto.ota_varastosta(2)
        teksti = self.varasto.__str__()
        self.assertEqual(teksti,"saldo = 2, vielä tilaa 8")
    
    def test_alustetaan_tilavuus_negatiivisella_syotteella(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)
    
    def test_alustetaan_alkusaldo_negatiivisella_syotteella(self):
        self.varasto = Varasto(1, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
