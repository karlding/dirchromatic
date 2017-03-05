class OutputWriter(object):
    def __init__(self, template, output_file):
        self._template = template
        self._fd = output_file

    def write(self, data):
        template = self._template.read()
        lines = '\n'.join(data)
        self._fd.write(template.replace('${data}', lines))
        #for line in data:
        #    self._fd.write("%s\n" % line)
