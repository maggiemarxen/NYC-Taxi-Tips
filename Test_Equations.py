import numpy
import pandas as pd
import Calculations
import unittest

#contains trips for the following locationID-> locationID
#1->2
#3->3
#4->5
#5->4
class Test_Equations(unittest.TestCase):

    def test_self(self): 

        zonedf = pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\mock_zones.csv")
        y_datadf = pd.read_csv(r"C:\Users\nick\Documents\GitHub\NYC-Taxi-Tips\mock_yellow_data.csv")
        
        # test converting Borough name to zones
        zone_id_dict = Calculations.init_zone_dict(zonedf)
        zone_list = Calculations.convert_zone_ID(zone_id_dict, "Cat")
        
        # data contains two zone IDs of 2 and 3
        self.assertTrue(zone_list == [2, 3])

        # test converting Borough name to zones
        zone_id_dict = Calculations.init_zone_dict(zonedf)
        zone_list = Calculations.convert_zone_ID(zone_id_dict, "Dog")
        #data contains zone ID of 1
        self.assertTrue(zone_list == [1, 5])

        # Tests to complete at later time
        #test computing an average cost between Boroughs, using all three transport methods
        #data contains two costs of 10 and 20. There is only one transit method
        # y_dict = Calculations.calc_dict_costs(y_datadf, "Dog", "Cat")
        # y_cost = Calculations.compute_one_method_cost("Dog", "Cat", zone_id_dict, y_dict)
        #self.assertTrue(Calculations.compute_avg_cost("Dog", "Cat") == 15)
        #test computing an average cost between Boroughs, using only one transport method
        #data contains one data piece where cost is 25
        #self.assertTrue(Calculations.compute_one_method_cost("Fish", "Dog", datadf) == 25)
    

if __name__ == '__main__':
    unittest.main()


