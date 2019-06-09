import quantum_negating_basis_states as qnbs
import oracle_abstract
import costum_exeptions as ce


class OracleSimple(oracle_abstract.Oracle):
    """
    A simple oracle which uses a quantum circuit composed by CNOT and H gates
    to implement the Oracle.
    """

    def get_circuit(self, qr, qc):
        try:
            if (self.n > 3):
                raise ce.ToManyQubits
            elif (self.x_star >= 2 ** self.n):
                raise ce.ValueOutOfRange
            else:
                qnbs.negating_basis_state(self.n, qc, qr, self.x_star)
        except ce.ToManyQubits as tmq:
            print('At the moment, the oracle works with up to 3 qubits.')
            exit(1)
        except ce.ValueOutOfRange as voor:
            print('x_star should be between 0 and 2**n - 1.')
            exit(1)




