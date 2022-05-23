class Texts:
    def __init__(self):
        pass

    def text1(self):
        TEXT1 = """
        <p style='text-align: justify; color: black;'> This application consists of the prediction of people infected by SARS-CoV-2 from viral load present in wastewater samples. 
        The user will be able to simulate an automatic or manual prediction according to the equation: </p>
        """

        return TEXT1
        
    def text1_1(self):
        TEXT1_1 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>pySewage website</h1>
        <p> pySewage - a program that permits of the prediction of people infected by SARS-CoV-2.
        <h2 style='text-align: justify; color: black;'>Citation</h2>
        Please cite the following reference when publishing results obtained with pySewage:<br>
        (i) DE SOUSA, Adriano Roberto Vieira, et al. “pySewage”: a hybrid approach to predict the number of SARS-CoV-2-infected people from wastewater in Brazil. Environmental Science and Pollution Research, 2022, 1-10, <a href="https://doi.org/10.1007/s11356-022-20609-z"target="_blank">https://doi.org/10.1007/s11356-022-20609-z</a>
        </p>
        </body>
        """
        return TEXT1_1

    def text2(self):
        TEXT2 = """
        <p style='text-align: justify; color: black;'>
        where:<br>                     
        NIP: number of infected people;<br> 
        VGC: Viral genomic copies detected in wastewater (viral gene load/L);<br>
        FR: Wastewater flow rate (L/day);<br>
        α: Viral load in the stool (viral gene copies/g stool);<br>
        β: Daily production of stool per capita (g stool/capita.day);<br>
        γ: % of COVID-19 patients who shed virus in their stool.<br>
        
        <p style='text-align: justify; color: black;'> To start the simulation, the user must add a csv file (download template below) 
        with the viral load detected in the wastewater (VGC) and the flow rate (FR). 
        For automatic simulation, the calculation will be performed according to the 
        standard parameters of alpha, beta, and gamma. For manual simulation, 
        the user must add the values of alpha, beta, and gamma parameters. 
        To reduce uncertainties regarding the equation's variables, 
        the web application employs Monte Carlo simulation in alpha, beta and gamma variables.</p>
        """

        return TEXT2
    
    def text3(self):
        TEXT3 = """
        ## Supporters
        """

        return TEXT3
    

    def text4(self):
        TEXT4 = """
        This web platform is free and open source and you are very welcome to contribute.
        This Application has GNU GPL license. All source code can be accessed [here](https://github.com/flavioolimpio/pySewage).
        """
        
        return TEXT4
