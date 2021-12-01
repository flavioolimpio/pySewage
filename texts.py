class Texts:
    def __init__(self):
        pass

    def text1(self):
        TEXT1 = """
        This application consists of predicting the number of people infected with Sars-Cov-2 from viral detection in wastewater. 
        The user can simulate an automatic or manual prediction according to the equation: 
        NIP = \frac{VGC*FR}{\alpha*\beta*\gamma}
        where:
        NIP: number of infected people
        VGC: Viral genomic copies detected in wastewater (viral gene load/L).
        FR: Wastewater flow rate (L/day).
        alpha: Viral load in the stool (viral gene copies/g stool).
        beta: Daily production of stool per capita (g stool/capita.day).
        gamma: % of COVID-19 patients who shed virus in their stool.
        
        To start the simulation, the user must add a csv file (download template) with the viral load detected in the wastewater (VGC) and the flow rate (FR). 
        Then, for automatic simulation, the calculation will be performed according to the alpha, beta and standard gamma parameters. 
        For manual simulation, the user must add the values of alpha, beta and gamma parameters.
        To reduce uncertainties regarding the equation's variables, the web application employs Monte Carlo simulation on the alpha, beta and gamma variables.
        
        """

        return TEXT1

    def text3(self):
        TEXT3 = """
        ## How to run
        The user to estimate the prevalence of infection using 
        Monte Carlo Simulation due to the uncertainty of the variables (see Equation bellow). 
        On the Simulation interface the user can choose between automatic or manual simulation. 
        For both cases, the user must add genomic copies per liter of sewage (csv file), and wastewater flow rate input (liters per second per day). 
        The user can change some variables such as α, β, and ε (see Equation below) when manual mode is selected. 
        
        ## About
        pySewage was designed to facilitate the automatic researchers to prediction and analyze of viral RNA concetration of SARS-CoV-2
        using Monte Carlo Simulation. The tools are designed to be quick and simple users with few clicks
        can make the prediction. The tools are rigorous enough to have applications in academic research

        ## Supporters
        """

        return TEXT3
    
