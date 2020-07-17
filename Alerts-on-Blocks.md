      # check setting mobiles and emails
        g.alerts.set_sms(["123456", "789"])
        g.alerts.set_email(["a@b", "c@d"])

        # enable alert and check still in range
        g.alerts.set_range(self.block_name, -10.0, 20.0, 2.0, 2.1)
        g.alerts.enable(self.block_name, True)
        
        # now make out of range
        g.alerts.set_range(self.block_name, 10.0, 20.0, 2.0, 2.1)
        
        # now make in range
        g.alerts.set_range(self.block_name, -10.0, 20.0, 2.0, 2.1)

        # now disable alerts, but put out of range
        g.alerts.enable(self.block_name, False)
        g.alerts.set_range(self.block_name, 10.0, 20.0, 2.0, 2.1)