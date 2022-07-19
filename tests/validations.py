from unittest import TestCase
import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")

README_file_name = "README.txt"
new_file_name = "text.txt"

README_added_text = 'Added text for example\n'
Text_file_text = 'Example for a test file'


class TestValidations(TestCase):

    def test_README_file(self):
        try:
            with open('../'+README_file_name, 'r') as file:
                file_contents = file.readlines()
                logging.info("Succeeded reading file - " + README_file_name)
        except IOError as e:
            logging.error("Failed to read file - {}. Error message: {}".format(README_file_name, e))
        finally:
            file.close()

        result = file_contents[-1]
        assert result == README_added_text, "{} not include {}".format(README_file_name, README_added_text)
        logging.info("Testing method test_README_file succeeded")

    def test_added_text_file(self):
        try:
            with open('../'+new_file_name, 'r') as file:
                file_contents = file.readline()
                logging.info("Succeeded reading file - " + new_file_name)
        except IOError as e:
            logging.error("Failed to read file - {}. Error message: {}".format(new_file_name, e))
        finally:
            file.close()

        assert file_contents == Text_file_text, "{} content not equal to {}".format(new_file_name, Text_file_text)
        logging.info("Testing method test_added_text_file succeeded")
