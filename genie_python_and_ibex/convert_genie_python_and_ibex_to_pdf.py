import logging
import os
from rst2pdf.createpdf import RstToPdf


class PDFGenerator(object):

    REST_EXTENSION = ".rest"
    PYTHON_EXTENSION = ".py"
    LOG_DIR = 'logs'
    OUTPUT_DIR = 'output'

    def __init__(self):
        self._initialise_logging()

    def _initialise_logging(self):
        from datetime import datetime as dt
        logger = logging.getLogger('pdf_generator')
        logger.setLevel(logging.DEBUG)

        if not os.path.exists('logs'):
            os.mkdir('logs')

        fh = logging.FileHandler(
            os.path.join(PDFGenerator.LOG_DIR, 'pdf_generator_{0}.log'.format(dt.now().strftime("%y_%m_%d_%H_%M_%S"))))
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        self.logger = logger

    def create(self):

        for path in self.get_source_files():

            self.logger.info("Reading {0}".format(path))
            try:
                raw_text = open(path, "r").readlines()
            except Exception as e:
                self.logger.error("Unknown error reading {0}: {1}".format(path, e.message))

            self.logger.info("Formatting {0}".format(path))
            try:
                formatted_text = self.format_rst(raw_text)
            except Exception as e:
                self.logger.error("Unknown error formatting {0}: {1}".format(path, e.message))

            output = os.path.join(PDFGenerator.OUTPUT_DIR,
                                  path.replace(PDFGenerator.REST_EXTENSION, PDFGenerator.PYTHON_EXTENSION))
            self.logger.info("Creating pdf of {0} at {1}".format(path, output))
            try:
                RstToPdf.createPdf(text=formatted_text,output=output)
            except Exception as e:
                self.logger.error("Unknown error creating pdf of {0}: {1}".format(path, e.message))

    def get_source_files(self):
        self.logger.info("Getting source files from: {0}".format(os.getcwd()))
        files = [f for f in os.getcwd() if f.endswith(PDFGenerator.REST_EXTENSION)]
        self.logger.info("Found {0} restructured text files for conversion".format(len(files)))
        return files

    def format_rst(self, text):
        return text


if __name__ == "__main__":
    PDFGenerator().create()
