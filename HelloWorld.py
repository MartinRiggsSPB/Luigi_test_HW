from Hello import *
from World import *

#python -m luigi --module HelloWorld HelloWorldTask --local-scheduler  -- в консоли для запуска планировщика и задач



class HelloWorldTask(luigi.Task):
    def requires(self):
        return {
            'a': HelloTask(),
            'b': WorldTask()
        }

    def run(self):
        # hello, world = self.input()
        # with self.output().open('w') as output:
        #     with hello.open() as fh, world.open() as fw:
        #         output.write('{} {}\n'.format(fh.read(), fw.read()))
        hello = self.input()['a']
        world = self.input()['b']
        fh = hello.open()
        fw = world.open()
        with self.output().open('w') as f:
            f.write('{} {}\n'.format(fh.read(), fw.read()))
            # with hello.open() as fh, world.open() as fw:
            #     f.write('{} {}\n'.format(fh.read(), fw.read()))

    def output(self):
        return luigi.LocalTarget('hello_world.txt')


