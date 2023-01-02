from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (name,jobTitle,agencyID,agency,hireDate,annualSalary,grossPay) = line.split('\t')
        annualSalary = float(annualSalary)
        if (annualSalary >= 100000.00):
        	yield 'High', 1
        elif (annualSalary >= 50000.00 and annualSalary <= 99999.99)	:
        	yield 'Medium', 1
        elif (annualSalary >= 0.00 and annualSalary <= 49999.99):
        	yield 'Low', 1

    def combiner(self, jobTitle, counts):
        yield jobTitle, sum(counts)

    def reducer(self, jobTitle, counts):
        yield jobTitle, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()


