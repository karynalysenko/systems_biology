from cobra.io import read_sbml_model
model = read_sbml_model('iML1515.xml')
envcond = {'EX_glc__D_e': (-15.0, 100000.0),
           'EX_o2_e':(0,1000)}

#from mewpy.simulation import get_simulator
#simul = get_simulator(model, envcond=envcond)

# Define the target
PRODUCT_ID = 'EX_mal__L_e'
BIOMASS_ID = 'BIOMASS_Ec_iML1515_core_75p37M'

#Optimization objectives
from mewpy.optimization.evaluation import  BPCY, TargetFlux, WYIELD, BPCY_FVA
evaluator_1 = WYIELD(BIOMASS_ID, PRODUCT_ID, alpha=1)
evaluator_2 = WYIELD(BIOMASS_ID, PRODUCT_ID)
#WYIELD(BIOMASS_ID, PRODUCT_ID)
#TargetFlux(PRODUCT_ID)
#BPCY_FVA(BIOMASS_ID, PRODUCT_ID)

from mewpy.problems import GKOProblem
problem = GKOProblem(model, fevaluation = [evaluator_1, evaluator_2], envcond=envcond, candidate_max_size=5)

from mewpy.optimization import EA
ea = EA(problem, max_generations= 50, visualizer=True)
final_pop = ea.run()
print(final_pop)
gene_list = open('del_five_gene_list.txt', 'w')
for i in final_pop:
    gene_list.write(str(i) + '\n')

from mewpy.utils.constants import ModelConstants
ModelConstants.RESET_SOLVER = True