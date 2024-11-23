import unittest
from unittest.mock import ANY, Mock

from kauppa import Kauppa
from tuote import Tuote
from varasto import Varasto
from viitegeneraattori import Viitegeneraattori


class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista



    def test_ostoksen_paatyttya_tilisiirto_kutsutaan_oikein_yhdella_tuotteella(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu('Jasse', '98765')

        mock_pankki.tilisiirto.assert_called_with('Jasse', 42, '98765', ANY, 5)


    def test_ostoksen_paatyttya_tilisiirto_kutsutaan_oikein_kahdella_eri_tuotteella(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)
            if tuote_id == 2:
                return Tuote(2, 'leipä', 7)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu('Jasse', '98765')

        mock_pankki.tilisiirto.assert_called_with('Jasse', 42, '98765', ANY, 12)

    def test_ostoksen_paatyttya_tilisiirto_kutsutaan_oikein_kahdella_samalla_tuotteella(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu('Jasse', '98765')

        mock_pankki.tilisiirto.assert_called_with('Jasse', 42, '98765', ANY, 10)

    def test_ostoksen_paatyttya_tilisiirto_kutsutaan_oikein_loppuneella_tuotteella(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)
            if tuote_id == 2:
                return Tuote(2,'leipä', 7)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu('Jasse', '98765')

        mock_pankki.tilisiirto.assert_called_with('Jasse', 42, '98765', ANY, 5)

    def test_ostoksen_paatyttya_tilisiirto_kutsutaan_oikealla_summalla(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)
            if tuote_id == 2:
                return Tuote(2,'leipä', 7)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(1)
        kauppa.tilimaksu('Jasse', '98765')

        mock_pankki.tilisiirto.assert_called_with('Jasse', 42, '98765', ANY, 12)
        
    def test_ostoksen_aluksi_ostoskori_nollattu(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)
            if tuote_id == 2:
                return Tuote(2,'leipä', 7)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu('Jasse', '98765')

        mock_pankki.tilisiirto.assert_called_with('Jasse', 42, '98765', ANY, 7)

    def test_ostoksen_lopuksi_viitenumeroa_kasvatetaan(self):
        mock_pankki = Mock()
        mock_viitegeneraattori = Mock()

        mock_viitegeneraattori.uusi.return_value = 42

        mock_varasto = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)

        mock_varasto.saldo.side_effect = varasto_saldo
        mock_varasto.hae_tuote.side_effect = varasto_tuote


        kauppa = Kauppa(mock_varasto, mock_pankki, mock_viitegeneraattori)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu('Jasse', '98765')

        self.assertEqual(mock_viitegeneraattori.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu('Jasse', '98765')

        self.assertEqual(mock_viitegeneraattori.uusi.call_count, 2)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu('Jasse', '98765')

        self.assertEqual(mock_viitegeneraattori.uusi.call_count, 3)
