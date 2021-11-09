import luigi


class HelloTask(luigi.Task):
    """Writes "hello" to hello.txt file"""
    filename = 'hello.txt'

    def run(self):
        # тут необходимо описать логику работы
        with self.output().open('w') as f:
            f.write('Hello')

    def output(self):
        return luigi.LocalTarget(self.filename)


# hello = HelloTask()
# hello.run()
