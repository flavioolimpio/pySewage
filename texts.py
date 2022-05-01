class Texts:
    def __init__(self):
        pass

    def text1(self):
        TEXT1 = """
        This application consists of the prediction of people infected by SARS-CoV-2 from viral load present in wastewater samples. 
        The user will be able to simulate an automatic or manual prediction according to the equation:
        """

        return TEXT1
        
    def text1_1(self):
        TEXT1_1 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>pySewage website</h1>
        <p> pySewage - a program that permits of the prediction of people infected by SARS-CoV-2.
        <h2 style='text-align: justify; color: black;'>Citation</h2>
        Please cite the following reference when publishing results obtained with pySewage:<br>
        (i) Sousa, A. R.V., et al. (2022). “pySewage”: a hybrid approach to predict the number of SARS-CoV-2 infected people from wastewater in Brazil. Environmental Science and Pollution Research, X,X, 2022</a>
        </p>
        </body>
        """
        return TEXT1_1

    def text2(self):
        TEXT2 = """
        where:                                                             
        NIP: number of infected people;                                     
        VGC: Viral genomic copies detected in wastewater (viral gene load/L);    
        FR: Wastewater flow rate (L/day);                          
        α: Viral load in the stool (viral gene copies/g stool);          
        β: Daily production of stool per capita (g stool/capita.day);       
        γ: % of COVID-19 patients who shed virus in their stool.
        
        To start the simulation, the user must add a csv file (download template below) 
        with the viral load detected in the wastewater (VGC) and the flow rate (FR). 
        For automatic simulation, the calculation will be performed according to the 
        standard parameters of alpha, beta, and gamma. For manual simulation, 
        the user must add the values of alpha, beta, and gamma parameters. 
        To reduce uncertainties regarding the equation's variables, 
        the web application employs Monte Carlo simulation in alpha, beta and gamma variables.
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
