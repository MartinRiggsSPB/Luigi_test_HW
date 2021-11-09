import luigi


class WorldTask(luigi.Task):
    """Writes "world" to world.txt file"""
    filename = 'world.txt'

    def run(self):
        with self.output().open('w') as f:
            f.write('world')

    def output(self):
        return luigi.LocalTarget(self.filename)

# world = WorldTask()
# world.run()
