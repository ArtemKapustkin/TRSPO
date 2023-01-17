import numpy as np
import pprint
import time
from mpi4py import MPI


class Method:
    @staticmethod
    
    def is_in_circle(points):
        return np.square(points).sum(axis=1) <= 1


    def est_pi_value(self, comm, points_amt):
        data = None

        if rank == 0:
            count, reminder = divmod(points_amt, processes_amt)
            subset = [count * i for i in range(1, processes_amt + 1)]
            subset[-1] += reminder
            data = subset

        data = comm.scatter(data, root=0)
        start_t = time.time()
        points = np.random.rand(data, 2)
        in_circle = self.is_in_circle(points).astype(float).sum()
        pi = 4 * in_circle / data

        local_result = {   
            'PI': pi,
            'Points': data,
            'ID number': comm.Get_rank(),
            'Time': time.time() - start_t,
        }

        global_result = comm.gather(local_result, root=0)
        if rank == 0:
            return global_result


if __name__ == '__main__':
    mpi = MPI.COMM_WORLD
    rank = mpi.Get_rank()
    processes_amt = mpi.Get_size()


    method = Method()
    results = method.est_pi_value(mpi, 100000)
    if rank == 0:
        for result in results:
            print("Pi value: ", result['PI'], ", points: ", result['Points'], ", id: ", result['ID number'], ", time:", result['Time'], "\n")