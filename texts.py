class Texts:
    def __init__(self):
        pass

    def text1(self):
        TEXT1 = """
        This application consists of predicting the number of people infected with Sars-Cov-2 from viral detection in wastewater. 
        The user can simulate an automatic or manual prediction according to the equation:
        """

        return TEXT1

    def text3(self):
        TEXT3 = """
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

        ## Supporters
        """

        return TEXT3
    
