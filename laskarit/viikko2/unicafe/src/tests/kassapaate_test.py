import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_olemassa(self):
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertAlmostEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_syo_edullisesti_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertAlmostEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_syo_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(430)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertAlmostEqual(self.kassapaate.syo_maukkaasti_kateisella(430), 30)

    def test_syo_maukkaasti_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertAlmostEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_syo_edullisesti_kortilla_maksu_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_maksu_epaonnistuu(self):
        kortti = Maksukortti(200)

        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_maksu_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_maksu_epaonnistuu(self):
        kortti = Maksukortti(200)

        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_kortille_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.00)

    def test_lataa_kortille_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        