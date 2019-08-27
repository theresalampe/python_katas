import unittest
import python_katas.morse_decoder.main.Decoder as Decoder


class TestDecoder(unittest.TestCase):

    def test_should_return_value_for_one_morseInput(self):
        self.assertEqual(Decoder.encode_value(".-"), "A")
        self.assertEqual(Decoder.encode_value("-..."), "B")

    def test_should_return_word_for_multiple_morseInputs(self):
        self.assertEqual(Decoder.encode_word(".- -..."), "AB")
        self.assertEqual(Decoder.encode_word(".- -.-."), "AC")
        self.assertEqual(Decoder.encode_word(".... . -.--"), "HEY")
        self.assertEqual(Decoder.encode_word(".--- ..- -.. ."), "JUDE")

    def test_should_return_sentence_for_multiple_words(self):
        self.assertEqual(Decoder.encode_sentence(".... . -.--   .--- ..- -.. ."), "HEY JUDE")
        self.assertEqual(Decoder.encode_sentence(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")
        self.assertEqual(Decoder.encode_sentence(
            ".... .- .-.. .-.. --- / .. .... .-. / -.. .- / .-- .. . / --. . .... - / . ... / . ..- -.-. ...."),
            "HALLO IHR DA WIE GEHT ES EUCH")
        self.assertEqual(Decoder.encode_sentence(
            ".... .- .-.. .-.. --- / .. .... .-. / -.. .- --..-- / .-- .. . / --. . .... - / . ... / . ..- -.-. .... ..--.."),
            "HALLO IHR DA, WIE GEHT ES EUCH?")


if "__main__" == __name__:
    unittest.main()
