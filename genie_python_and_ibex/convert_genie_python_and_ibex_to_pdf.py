import logging
import os
import re
from rst2pdf.createpdf import RstToPdf


class PDFGenerator(object):

    REST_EXTENSION = ".rest"
    PDF_EXTENSION = ".pdf"
    LOG_DIR = 'logs'
    OUTPUT_DIR = 'output'

    def __init__(self):
        self._initialise_logging()
        self._initialise_output()

    def _initialise_logging(self):
        from datetime import datetime as dt
        logger = logging.getLogger('pdf_generator')
        logger.setLevel(logging.DEBUG)

        if not os.path.exists(PDFGenerator.LOG_DIR):
            os.mkdir(PDFGenerator.LOG_DIR)

        fh = logging.FileHandler(
            os.path.join(PDFGenerator.LOG_DIR, 'pdf_generator_{0}.log'.format(dt.now().strftime("%y_%m_%d_%H_%M_%S"))))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(fh)

        self.logger = logger

    def _initialise_output(self):
        if not os.path.exists(PDFGenerator.OUTPUT_DIR):
            os.mkdir(PDFGenerator.OUTPUT_DIR)
        self.converter = RstToPdf(stylesheets=['training.style'])

    def create(self):
        outputs = []
        for path in self.get_source_files():

            try:
                raw_text = open(path, "r").readlines()
            except Exception as e:
                self.logger.error("Unknown error reading {0}: {1}".format(path, e))

            try:
                formatted_text = self.format_rst(raw_text)
            except Exception as e:
                self.logger.error("Unknown error formatting {0}: {1}".format(path, e))

            output = os.path.join(PDFGenerator.OUTPUT_DIR,
                                  path.replace(PDFGenerator.REST_EXTENSION, PDFGenerator.PDF_EXTENSION))
            try:
                self.converter.createPdf(text=formatted_text, output=output)
            except Exception as e:
                print e
                self.logger.error("Unknown error creating pdf of {0}: {1}".format(path, e))
            else:
                outputs.append(output)

    def get_source_files(self):
        return [f for f in os.listdir(os.getcwd()) if f.endswith(PDFGenerator.REST_EXTENSION)]

    def format_rst(self, text):

        # Remove lines starting "Next:", "Previous:" and transitions
        text = [l for l in text if not any(l.startswith(s) for s in [
            "**Next**:", "**Previous**:", "--------",
            "[[Solution|genie_python-and-Ibex-(Exercise-solutions)]]",
        ])]

        # Correct image paths
        path_snippet = "genie_python_and_ibex"
        text = [l.replace("{0}/".format(path_snippet), "") for l in text]

        formatted = os.linesep.join(text)

        # Replace links with their description text
        p = re.compile('\[\[([^\|]*)\|([^\|]*)\]\]', re.VERBOSE)
        formatted = p.sub(r'\1', formatted)

        return formatted


if __name__ == "__main__":
    PDFGenerator().create()
